import yaml
from timeit import repeat

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
    # startNode와 endNode 초기화
    startNode = Node(None, start)
    startNode.g = startNode.h = startNode.f = 0
    endNode = Node(None, end)
    endNode.g = endNode.h = endNode.f = 0

    # openList, ClosedList 초기화
    openList = []
    closedList = []

    # openList에 시작 노드 추가
    openList.append(startNode)

    # endNode를 찾을 때까지 실행
    while openList:

        # 현재 노드 지정
        currentNode = openList[0]
        currentIdx = 0

        # 이미 같은 노드가 openList에 있고, f 값이 더 크면
        # currentNode를 openList안에 있는 값으로 교체
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIdx = index

        # openList에서 제거하고 closedList에 추가
        openList.pop(currentIdx)
        closedList.append(currentNode)

        # 현재 노드가 목적지면 current.position 추가하고
        # current의 부모로 이동
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
        # 인접한 xy좌표 전부
        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            # 노드 위치 업데이트
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

            # 장애물이 있으면 다른 위치 불러오기
            if maze[nodePosition[0]][nodePosition[1]] != 0:
                continue

            newNode = Node(currentNode, nodePosition)
            children.append(newNode)

        # 자식들 모두 loop
        for child in children:
            # 자식이 closedList에 있으면 check
            if len([closedChild for closedChild in closedList if closedChild == child]) > 0:
                continue

            # f, g, h값 업데이트
            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) ** 2) + \
                      ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g + child.h

            # 자식이 openList에 있으면 check
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

    print(star_map[end_y][end_x])

    #star_map[y_e][x_e] = 'X'
    print(star_map[end_y])

    path = aStar(star_map, start, end)
    print(path)

    return path





def find_way(maze, start, end, cost):
    #path = search(maze,cost, start, end)
    return True