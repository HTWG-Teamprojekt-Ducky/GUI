import astar, yaml

def load_map(name):
    with open('../maps/{}.yaml'.format(name), 'r') as map_file:
        map_file = yaml.load(map_file, Loader=yaml.FullLoader)
    
    return map_file['tiles']

x = load_map('udem1')
print(x, '\n\n')
def create_areas(mapdata):
    data = []
    
    for m in mapdata:
        row = []
        for t in m:
            if t == 'floor' or t == 'asphalt':
                for i in range(10):
                    row.append(1)
            else:
                for i in range(10):
                    row.append(0)
        
        for i in range(10):
            data.append(row)
            
    return data
    
    
star_map = create_areas(load_map('udem1'))


maze = [
        
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0]
            
            
            ]
    
start = [15, 15] # starting position
end = [15,30] # ending position
cost = 1 # cost per movement


way = astar.find_way(star_map, start, end, cost)
print(way)