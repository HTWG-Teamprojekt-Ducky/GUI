import numpy
import yaml

way_left_N = [['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
                ['N', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
                ['N', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
                ['N', 'S', 'S', 'S', 'N', 'N', 'N', 'N', 'N', 'X'],
                ['X', 'S', 'S', 'S', 'N', 'N', 'N', 'N', 'N', 'X'],
                ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
                ['S', 'S', 'S', 'S', 'N', 'N', 'N', 'N', 'N', 'X'],
                ['S', 'S', 'S', 'S', 'N', 'N', 'N', 'N', 'N', 'X'],
                ['S', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
                ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X']]

way_left_E = [['X', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'X'],
                ['W', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'X'],
                ['W', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'X'],
                ['W', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'X'],
                ['X', 'X', 'X', 'X', 'X', 'E', 'E', 'E', 'E', 'X'],
                ['X', 'X', 'X', 'X', 'E', 'E', 'E', 'E', 'E', 'X'],
                ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
                ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

way_left_S = [['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
                ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'S'],
                ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'S'],
                ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'S'],
                ['X', 'S', 'S', 'S', 'X', 'X', 'X', 'X', 'X', 'X'],
                ['X', 'S', 'S', 'S', 'S', 'S', 'X', 'X', 'X', 'X'],
                ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['X', 'S', 'S', 'S', 'S', 'X', 'X', 'X', 'X', 'X']]

way_left_W = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                ['X', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X', 'X'],
                ['X', 'W', 'W', 'W', 'X', 'X', 'X', 'X', 'X', 'X'],
                ['X', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'E'],
                ['X', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'E'],
                ['X', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'E'],
                ['X', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'X']]

curve_left_n = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'X'],
                ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'X'],
                ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'X'],
                ['X', 'X', 'X', 'X', 'X', 'X', 'N', 'N', 'N', 'X'],
                ['X', 'X', 'X', 'X', 'X', 'X', 'N', 'N', 'N', 'X'],
                ['S', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
                ['S', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
                ['S', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
                ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X']]

curve_left_e = [['X', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'X'],
                ['W', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'X'],
                ['W', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'X'],
                ['W', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'X'],
                ['X', 'X', 'X', 'X', 'X', 'E', 'E', 'E', 'E', 'X'],
                ['X', 'X', 'X', 'X', 'E', 'E', 'E', 'E', 'E', 'X'],
                ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
                ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
                ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'X'],
                ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

curve_left_s = [['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
                ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'S'],
                ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'S'],
                ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'S'],
                ['X', 'S', 'S', 'S', 'X', 'X', 'X', 'X', 'X', 'X'],
                ['X', 'S', 'S', 'S', 'S', 'S', 'X', 'X', 'X', 'X'],
                ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
                ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

curve_left_w = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                ['X', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                ['X', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                ['X', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                ['X', 'W', 'W', 'W', 'W', 'X', 'X', 'X', 'X', 'X'],
                ['X', 'W', 'W', 'W', 'X', 'X', 'X', 'X', 'X', 'X'],
                ['X', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'E'],
                ['X', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'E'],
                ['X', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'E'],
                ['X', 'W', 'W', 'W', 'X', 'X', 'E', 'E', 'E', 'X']]

straight_w = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
              ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
              ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

straight_n = [['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X']]

straight_s = [['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X'],
              ['X', 'S', 'S', 'S', 'X', 'X', 'N', 'N', 'N', 'X']]

straight_e = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
              ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
              ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


class Vertex:
    def __init__(self, position=None):
        self.position = position

    def getIndex(self):
        return self.position[0] * 80 + self.position[1]

    def __str__(self):
        return str((self.position[0], self.position[1]))


def shortest(maze, start, end):
    kl = []
    d = []
    p = []
    number_of_vertices = (len(maze)) * (len(maze[0]))
    print("number_of_vertices", number_of_vertices)
    for x in range(0, number_of_vertices):
        d.append(200000)
        p.append(None)
    d[start.getIndex()] = 0
    kl.append(start)
    print("start::", kl[0])

    while len(kl) > 0:
        v = find_min_h(kl, end, d)
        kl.remove(v)
        print("next vertex", v.position)
        if v.getIndex() == end.getIndex():
            print("find way")
            return p
        for x in get_adjacent_vertices(v, (len(maze) - 1), (len(maze[len(maze) - 1]) - 1), maze):
            if d[x.getIndex()] == 200000:
                kl.append(x)
            cost = d[v.getIndex()] + 1  # maze[x.position[0]][x.position[1]]
            if cost < d[x.getIndex()]:
                p[x.getIndex()] = v
                d[x.getIndex()] = cost
    print("no way")
    return p


def find_min_h(kl, end, d):
    low = 20000000
    v = None
    for x in kl:
        h = numpy.sqrt(((x.position[0] - end.position[0]) ** 2) + ((x.position[1] - end.position[1]) ** 2))
        if low > d[x.getIndex()] + h:
            low = d[x.getIndex()] + h
            v = x
    return v


def get_adjacent_vertices(current_node, max_x, max_y, maze):
    list_of_vertices = []

    #
    #
    #   N.W   N   N.E
    #     \   |   /
    #      \  |  /
    #    W----Cell----E
    #        / | \
    #      /   |  \
    #   S.W    S   S.E

    # for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
    adjacent_vertices = []
    # (y,x)
    print('maze value at y = ', current_node.position[0], 'x =', current_node.position[1], 'value =' , maze[current_node.position[0]][current_node.position[1]])
    if maze[current_node.position[0]][current_node.position[1]] == 'S':
        adjacent_vertices = [(0, -1), (1, 0), (0, 1), (1, -1), (1, 1)]
    elif maze[current_node.position[0]][current_node.position[1]] == 'N':
        adjacent_vertices = [(0, 1), (-1, 0), (0, -1), (-1, 1), (-1, -1)]
    elif maze[current_node.position[0]][current_node.position[1]] == 'E':
        adjacent_vertices = [(0, 1), (1, 0), (-1, 0), (1, 1), (-1, 1)]
    elif maze[current_node.position[0]][current_node.position[1]] == 'W':
        adjacent_vertices = [(0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1)]

    for newPosition in adjacent_vertices:
        # for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        node_position = (
            current_node.position[0] + newPosition[0],  # X
            current_node.position[1] + newPosition[1])  # Y
        v = Vertex(node_position)
        # Range
        range_criteria = [
            node_position[0] > max_x,
            node_position[0] < 0,
            node_position[1] > max_y,
            node_position[1] < 0,
        ]

        if any(range_criteria):
            continue

        # if maze[node_position[0]][node_position[1]] > 30:
        #    continue
        list_of_vertices.append(v)
    return list_of_vertices


def create_path(list_of_vertices, start, end):
    path = []
    previous = end
    print("number of element in p", len(list_of_vertices))
    if list_of_vertices[end.getIndex()] is None:
        return []
    while start.getIndex() != previous.getIndex():
        path.append(previous.position)
        previous = list_of_vertices[previous.getIndex()]
    path.append(start.position)
    path.reverse()

    return path


def load_map(name):
    with open('maps/{}.yaml'.format(name), 'r') as map_file:
        map_file = yaml.load(map_file, Loader=yaml.FullLoader)

    return map_file['tiles']


x = load_map('udem1')


def create_map(mapdata):
    print('start map')
    data = []
    mod = 1
    for m in mapdata:
        for i in range(0, 10):
            row = []
            for t in m:
                if t == 'floor' or t == 'asphalt' or t == 'grass':
                    for o in range(10):
                        row.append(200)
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
                    elif t == '3way_left/E':
                        for l in way_left_E[i]:
                            row.append(l * mod)
                    elif t == '3way_left/S':
                        for l in way_left_S[i]:
                            row.append(l * mod)
                    elif t == '3way_left/W':
                        for l in way_left_W[i]:
                            row.append(l * mod)
                    elif t == '3way_left/N':
                        for l in way_left_N[i]:
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

    print('a star active')
    print(star_map, start, end)

    v = shortest(star_map, Vertex(start), Vertex(end))
    print('v =', v)
    s = Vertex(start)
    e = Vertex(end)
    if len(v) > 0:
        p = create_path(v, s, e)
        for x in p:
            print(x)
        print("length of my path", len(p))
        return p
    return []

