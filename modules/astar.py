import yaml

way_left_N = [[4, 4, 4, 4, 4, 3, 0, 0, 0, 4],
              [4, 4, 4, 4, 4, 3, 0, 0, 0, 4],
              [4, 4, 4, 4, 4, 3, 0, 0, 0, 4],
              [4, 4, 4, 4, 4, 3, 0, 0, 0, 4],
              [4, 4, 4, 4, 4, 3, 0, 0, 0, 4],
              [4, 4, 4, 3, 3, 3, 0, 0, 0, 4],
              [0, 0, 0, 2, 3, 3, 0, 0, 0, 4],
              [0, 0, 0, 0, 3, 3, 0, 0, 0, 4],
              [3, 0, 0, 0, 3, 3, 0, 0, 0, 4],
              [4, 0, 0, 0, 3, 3, 0, 0, 0, 4]]

way_left_E = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [1, 1, 1, 1, 2, 2, 2, 3, 4, 4],
              [0, 0, 0, 0, 0, 0, 0, 0, 3, 4],
              [0, 0, 0, 1, 1, 1, 0, 0, 3, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 2, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 1, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 0, 4]]

way_left_S = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [1, 1, 1, 1, 2, 2, 2, 3, 4, 4],
              [0, 0, 0, 0, 0, 0, 0, 0, 3, 4],
              [0, 0, 0, 1, 1, 1, 0, 0, 3, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 2, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 1, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 0, 4]]

way_left_W = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [1, 1, 1, 1, 2, 2, 2, 3, 4, 4],
              [0, 0, 0, 0, 0, 0, 0, 0, 3, 4],
              [0, 0, 0, 1, 1, 1, 0, 0, 3, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 2, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 1, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
              [4, 3, 3, 3, 3, 3, 0, 0, 0, 4]]

curve_left_n = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                [1, 1, 1, 1, 2, 2, 2, 3, 4, 4],
                [0, 0, 0, 0, 0, 0, 0, 0, 3, 4],
                [0, 0, 0, 1, 1, 1, 0, 0, 3, 4],
                [4, 3, 3, 3, 3, 3, 0, 0, 2, 4],
                [4, 3, 3, 3, 3, 3, 0, 0, 1, 4],
                [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
                [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
                [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
                [4, 3, 3, 3, 3, 3, 0, 0, 0, 4]]

curve_left_e = [[4, 4, 4, 4, 3, 2, 0, 0, 0, 4],
                [4, 4, 4, 4, 3, 2, 0, 0, 0, 4],
                [4, 4, 4, 4, 3, 2, 0, 0, 0, 4],
                [4, 4, 4, 4, 3, 2, 0, 0, 0, 4],
                [4, 4, 4, 4, 3, 2, 0, 0, 0, 4],
                [4, 3, 3, 3, 3, 3, 0, 0, 0, 4],
                [1, 1, 1, 1, 1, 1, 0, 0, 0, 4],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                [0, 0, 0, 0, 0, 0, 0, 0, 3, 4],
                [4, 3, 3, 3, 2, 2, 0, 0, 0, 4]]

curve_left_s = [[4, 0, 0, 0, 3, 4, 4, 4, 4, 4],
                [4, 0, 0, 0, 3, 4, 4, 4, 4, 4],
                [4, 0, 0, 0, 3, 4, 4, 4, 4, 4],
                [4, 0, 0, 0, 3, 4, 4, 4, 4, 4],
                [4, 0, 0, 0, 3, 4, 4, 4, 4, 4],
                [4, 0, 0, 0, 3, 3, 3, 3, 3, 3],
                [4, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                [4, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                [4, 3, 2, 0, 0, 0, 0, 0, 0, 0],
                [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]

curve_left_w = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                [4, 3, 2, 1, 0, 0, 0, 0, 0, 0],
                [4, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                [4, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [4, 0, 0, 0, 3, 3, 3, 3, 3, 4],
                [4, 0, 0, 0, 3, 4, 4, 4, 4, 4],
                [4, 0, 0, 0, 3, 4, 4, 4, 4, 4],
                [4, 0, 0, 0, 3, 4, 4, 4, 4, 4],
                [4, 0, 0, 0, 3, 4, 4, 4, 4, 4],
                [4, 0, 0, 0, 3, 4, 4, 4, 4, 4]]

straight_e = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
              [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
              [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]

straight_n = [[4, 3, 3, 3, 2, 2, 0, 0, 0, 4],
              [4, 3, 3, 3, 2, 2, 0, 0, 0, 4],
              [4, 3, 3, 3, 2, 2, 0, 0, 0, 4],
              [4, 3, 3, 3, 2, 2, 0, 0, 0, 4],
              [4, 3, 3, 3, 2, 2, 0, 0, 0, 4],
              [4, 3, 3, 3, 2, 2, 0, 0, 0, 4],
              [4, 3, 3, 3, 2, 2, 0, 0, 0, 4],
              [4, 3, 3, 3, 2, 2, 0, 0, 0, 4],
              [4, 3, 3, 3, 2, 2, 0, 0, 0, 4],
              [4, 3, 3, 3, 2, 2, 0, 0, 0, 4]]

straight_s = [[4, 0, 0, 0, 2, 2, 3, 3, 3, 4],
              [4, 0, 0, 0, 2, 2, 3, 3, 3, 4],
              [4, 0, 0, 0, 2, 2, 3, 3, 3, 4],
              [4, 0, 0, 0, 2, 2, 3, 3, 3, 4],
              [4, 0, 0, 0, 2, 2, 3, 3, 3, 4],
              [4, 0, 0, 0, 2, 2, 3, 3, 3, 4],
              [4, 0, 0, 0, 2, 2, 3, 3, 3, 4],
              [4, 0, 0, 0, 2, 2, 3, 3, 3, 4],
              [4, 0, 0, 0, 2, 2, 3, 3, 3, 4],
              [4, 0, 0, 0, 2, 2, 3, 3, 3, 4]]

straight_w = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
              [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
              [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
              [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
              [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def a_star(maze, start, end):
    """

    :param maze:
    :param start:
    :param end:
    :return:

    """
    # startNode endNode
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # openList, ClosedList
    open_list = []
    closed_list = []

    # openList
    open_list.append(start_node)

    # endNode
    while open_list:

        current_node = open_list[0]
        current_idx = 0

        # openList
        # currentNode openList
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_idx = index

        # openList closedList
        open_list.pop(current_idx)
        closed_list.append(current_node)

        # current.position
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                x, y = current.position
                maze[x][y] = 7
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        children = []

        #
        #
        #   N.W   N   N.E
        #     \   |   /
        #      \  |  /
        #    W----Cell----E
        #        / | \
        #      /   |  \
        #   S.W    S   S.E

        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            node_position = (
                current_node.position[0] + newPosition[0],  # X
                current_node.position[1] + newPosition[1])  # Y

            # Range
            range_criteria = [
                node_position[0] > (len(maze) - 1),
                node_position[0] < 0,
                node_position[1] > (len(maze[len(maze) - 1]) - 1),
                node_position[1] < 0,
            ]

            if any(range_criteria):
                continue

            if maze[node_position[0]][node_position[1]] > 300:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        # loop
        for child in children:
            # closed List check
            if len([closedChild for closedChild in closed_list if closedChild == child]) > 0:
                continue

            # f, g, h
           # print(maze[child.position[0]][child.position[1]])
            child.g = current_node.g + maze[child.position[0]][child.position[1]]
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + \
                      ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # open List check
            if len([openNode for openNode in open_list
                    if child == openNode and child.g > openNode.g]) > 0:
                continue

            open_list.append(child)


def print_path(maze, path):
    map = ''
    for coord in path:
        maze[coord[0]][coord[1]] = 'P'
    for i in maze:
        for j in i:
            if j < 5:
                map += " "
            else:
                map += str(j)
        map += '\n'
    return map


def load_map(name):
    with open('maps/{}.yaml'.format(name), 'r') as map_file:
        map_file = yaml.load(map_file, Loader=yaml.FullLoader)

    return map_file['tiles']


x = load_map('udem1')


def create_map(mapdata):
    print('start map')
    data = []
    mod = 15
    for m in mapdata:
        for i in range(0, 10):
            row = []
            for t in m:
                if t == 'floor' or t == 'asphalt' or t == 'grass':
                    for o in range(10):
                        row.append(100)
                else:
                    if t == 'straight/E':
                        for l in straight_e[i]:
                            row.append(l * mod)
                    elif t == 'straight/W':
                        for l in straight_w[i]:
                            row.append(l * mod)
                    elif t == 'straight/N':
                        for l in straight_n[i]:
                            row.append(l * mod)
                    elif t == 'straight/S':
                        for l in straight_s[i]:
                            row.append(l * mod)
                    elif t == 'curve_left/S':
                        for l in curve_left_s[i]:
                            row.append(l * mod)
                    elif t == 'curve_left/N':
                        for l in curve_left_n[i]:
                            row.append(l * mod)
                    elif t == 'curve_left/E':
                        for l in curve_left_e[i]:
                            row.append(l * mod)
                    elif t == 'curve_left/W':
                        for l in curve_left_w[i]:
                            row.append(l * mod)
                    else:
                        for o in range(10):
                            row.append(1 * mod)

            print(row)
            data.append(row)
    return data


# star_map = create_areas(load_map('udem1'))


def main(start, end):
    star_map = create_map(load_map('udem1'))

    start_x = start[0]
    start_y = start[1]

    start = (start_y, start_x)

    end_x = end[0]
    end_y = end[1]

    end = (end_y, end_x)

    # print(star_map[end_y][end_x])
    # star_map[y_e][x_e] = 'X'
    # print(star_map[end_y])
    print('activ astar')
    path = a_star(star_map, start, end)
    print(path)

    return path


def find_way(maze, start, end, cost):
    # path = search(maze,cost, start, end)
    return True
