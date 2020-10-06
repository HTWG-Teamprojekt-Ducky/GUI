# coding=utf-8
import threading

import numpy as np
from gym import spaces

from lokalisierung.Ducky_map import DuckieMap
from lokalisierung.MCL import MCL
from gym_duckietown import logger
from gym_duckietown.simulator import Simulator
from Observer import Publisher


class DuckietownEnv(Simulator, threading.Thread, Publisher):
    """
    Wrapper to control the simulator using velocity and steering angle
    instead of differential drive motor velocities
    """

    def __init__(
            self,
            gain=1.0,
            trim=0.0,
            radius=0.0318,
            k=27.0,
            limit=1.0,
            line=None,
            GUI=None,
            **kwargs
    ):
        Publisher.__init__(self)
        Simulator.__init__(self, **kwargs)
        logger.info('using DuckietownEnv')
        threading.Thread.__init__(self)
        self.action_space = spaces.Box(
            low=np.array([-1, -1]),
            high=np.array([1, 1]),
            dtype=np.float32
        )

        # Should be adjusted so that the effective speed of the robot is 0.2 m/s
        self.gain = gain

        self.line = line

        # Directional trim adjustment
        self.trim = trim

        self.register(GUI)

        # Wheel radius
        self.radius = radius

        # Motor constant
        self.k = k

        # Wheel velocity limit
        self.limit = limit

    def global_angle_arr(self, point, i):
        t = self.cur_angle
        x = self.cur_pos[0]
        y = self.cur_pos[2]
        print("nächster punkt", point[i][1] / 10, point[i][0] / 10)
        rot = np.arctan2((y - point[i][0] / 10), (point[i][1] / 10 - x))
        if t is None:
            t = 0
        a = rot - t
        a = (a / abs(a)) * (abs(a) % (2 * np.pi))
        print(i, "t = ", t, "rot = ", rot, "a = ", a)
        if (a >= np.pi):
            a = -2 * np.pi + a
            return a
        if (a < -np.pi):
            a = 2 * np.pi + a
            return a
        return a

    def global_angle(self, point):
        t = self.cur_angle
        x = self.cur_pos[0]
        y = self.cur_pos[2]
        rot = np.arctan2((y - point[1]), (point[0] - x))
        a = rot - t
        a = (a / abs(a)) * (abs(a) % (2 * np.pi))
        print(i, "t = ", t, "rot = ", rot, "a = ", a)
        if (a >= np.pi):
            a = -2 * np.pi + a
            return a
        if (a < -np.pi):
            a = 2 * np.pi - a
            return a
        return a

    def loca_angle(rad, dist):
        w = 10
        tile_size = 1
        return rad - (tile_size / 20 - dist) * w

    def run(self):
        print("asd", self.line[0][1], self.line[0][0])
        io = 0
        self.cur_pos = [self.line[0][1] / 10, 0, self.line[0][0] / 10]
        self.cur_angle = np.pi / 2

        my_map = DuckieMap("maps/udem1.yaml")
        particle_number = 25
        mcl = MCL(particle_number, my_map, self)
        mcl.spawn_particle_list(self.cur_pos, self.cur_angle)
        step_counter = 0
        newAStar = False
        while True:
            if io == len(self.line):
                newAStar = True
                continue
            if newAStar:
                print('new aStar starts')
                self.cur_pos = [self.line[0][1] / 10, 0, self.line[0][0] / 10]
                self.cur_angle = np.pi / 2
                mcl.spawn_particle_list(self.cur_pos, self.cur_angle)
                newAStar = False
            lane_pose = self.get_lane_pos2(self.cur_pos, self.cur_angle)
            print("self.cur_pose =")
            print(self.cur_pos)
            print("\n")
            distance_to_road_center = lane_pose.dist
            angle_from_straight_in_rads = lane_pose.angle_rad
            print("dist = ", distance_to_road_center, " rad = ", angle_from_straight_in_rads)

            speed = 0.2
            tol = 0.15
            if (abs(self.cur_pos[0] - self.line[io][1] / 10) <= tol and abs(self.cur_pos[2] - self.line[io][0] / 10) <= tol):
                io = io + 1
                if (io == len(self.line)):
                    io = 0
                    self.line = []
                    print('length of line', len(self.line))
                    continue
            steering = self.global_angle_arr(self.line, io)
            obs, reward, done, info = self.step([speed, steering])
            mcl.integrate_movement([speed, steering])
            step_counter += 1
            mcl.integrate_measurement(distance_to_road_center, angle_from_straight_in_rads)
            if step_counter % 2 == 0:
                # start = time.time()
                arr_chosenones, possible_location, possible_angle = mcl.resampling()
                self.dispatch([arr_chosenones, self.cur_pos, self.cur_angle])
                # end = time.time()
                # duration = end - start
                print("posloc and robot position", possible_location, self.cur_pos)
                print('possible angle and robot angle', possible_angle, self.cur_angle)
                mcl.weight_reset()

            # obs, reward, done, info = self.step([speed, loca_angle(angle_from_straight_in_rads, distance_to_road_center)])
            # obs, reward, done, info = self.step([speed, 0])
            # total_reward += reward
            print("info = ", info)
            # print('Steps = %s, Timestep Reward=%.3f, Total Reward=%.3f' % (self.step_count, reward, total_reward))

            self.render()

    def step(self, action):
        vel, angle = action

        # Distance between the wheels
        baseline = self.unwrapped.wheel_dist

        # assuming same motor constants k for both motors
        k_r = self.k
        k_l = self.k

        # adjusting k by gain and trim
        k_r_inv = (self.gain + self.trim) / k_r
        k_l_inv = (self.gain - self.trim) / k_l

        omega_r = (vel + 0.5 * angle * baseline) / self.radius
        omega_l = (vel - 0.5 * angle * baseline) / self.radius

        # conversion from motor rotation rate to duty cycle
        u_r = omega_r * k_r_inv
        u_l = omega_l * k_l_inv

        # limiting output to limit, which is 1.0 for the duckiebot
        u_r_limited = max(min(u_r, self.limit), -self.limit)
        u_l_limited = max(min(u_l, self.limit), -self.limit)

        vels = np.array([u_l_limited, u_r_limited])

        obs, reward, done, info = Simulator.step(self, vels)
        mine = {}
        mine['k'] = self.k
        mine['gain'] = self.gain
        mine['train'] = self.trim
        mine['radius'] = self.radius
        mine['omega_r'] = omega_r
        mine['omega_l'] = omega_l
        info['DuckietownEnv'] = mine
        return obs, reward, done, info


class DuckietownLF(DuckietownEnv):
    """
    Environment for the Duckietown lane following task with
    and without obstacles (LF and LFV tasks)
    """

    def __init__(self, **kwargs):
        DuckietownEnv.__init__(self, **kwargs)

    def step(self, action):
        obs, reward, done, info = DuckietownEnv.step(self, action)
        return obs, reward, done, info


class DuckietownNav(DuckietownEnv):
    """
    Environment for the Duckietown navigation task (NAV)
    """

    def __init__(self, **kwargs):
        self.goal_tile = None
        DuckietownEnv.__init__(self, **kwargs)

    def reset(self):
        DuckietownNav.reset(self)

        # Find the tile the agent starts on
        start_tile_pos = self.get_grid_coords(self.cur_pos)
        start_tile = self._get_tile(*start_tile_pos)

        # Select a random goal tile to navigate to
        assert len(self.drivable_tiles) > 1
        while True:
            tile_idx = self.np_random.randint(0, len(self.drivable_tiles))
            self.goal_tile = self.drivable_tiles[tile_idx]
            if self.goal_tile is not start_tile:
                break

    def step(self, action):
        obs, reward, done, info = DuckietownNav.step(self, action)

        info['goal_tile'] = self.goal_tile

        # TODO: add term to reward based on distance to goal?

        cur_tile_coords = self.get_grid_coords(self.cur_pos)
        cur_tile = self._get_tile(self.cur_tile_coords)

        if cur_tile is self.goal_tile:
            done = True
            reward = 1000

        return obs, reward, done, info
