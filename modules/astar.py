import yaml


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def aStar(maze, start, end):
    # startNode endNode
    startNode = Node(None, start)
    startNode.g = startNode.h = startNode.f = 0
    endNode = Node(None, end)
    endNode.g = endNode.h = endNode.f = 0

    # openList, ClosedList
    openList = []
    closedList = []

    # openList
    openList.append(startNode)

    # endNode
    while openList:

        currentNode = openList[0]
        currentIdx = 0

        # openList
        # currentNode openList
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIdx = index

        # openList closedList
        openList.pop(currentIdx)
        closedList.append(currentNode)

        # current.position
        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                x, y = current.position
                maze[x][y] = 7
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        children = []
        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            nodePosition = (
                currentNode.position[0] + newPosition[0],  # X
                currentNode.position[1] + newPosition[1])  # Y

            # Range
            rangeCriteria = [
                nodePosition[0] > (len(maze) - 1),
                nodePosition[0] < 0,
                nodePosition[1] > (len(maze[len(maze) - 1]) - 1),
                nodePosition[1] < 0,
            ]

            if any(rangeCriteria):
                continue

            if maze[nodePosition[0]][nodePosition[1]] != 0:
                continue

            newNode = Node(currentNode, nodePosition)
            children.append(newNode)

        # loop
        for child in children:
            # closed List check
            if len([closedChild for closedChild in closedList if closedChild == child]) > 0:
                continue

            # f, g, h
            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) ** 2) + \
                      ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g + child.h

            # open List check
            if len([openNode for openNode in openList
                    if child == openNode and child.g > openNode.g]) > 0:
                continue

            openList.append(child)


def print_path(maze, path):
    map = ''
    for coord in path:
        maze[coord[0]][coord[1]] = 'P'
    for i in maze:
        for j in i:
            if j == 0:
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


def create_areas(mapdata):
    data = []

    for m in mapdata:
        row = []
        for t in m:
            if t == 'floor' or t == 'asphalt' or t == 'grass':
                for i in range(10):
                    row.append(1)
            else:
                for i in range(10):
                    row.append(0)

        for i in range(10):
            data.append(row)

    return data


star_map = create_areas(load_map('udem1'))


def main(start, end):
    star_map = create_areas(load_map('udem1'))

    start_x = start[0]
    start_y = start[1]

    start = (start_y, start_x)

    end_x = end[0]
    end_y = end[1]

    end = (end_y, end_x)

    # print(star_map[end_y][end_x])
    # star_map[y_e][x_e] = 'X'
    # print(star_map[end_y])

    path = aStar(star_map, start, end)
    print(path)

    return path


def find_way(maze, start, end, cost):
    # path = search(maze,cost, start, end)
    return True
