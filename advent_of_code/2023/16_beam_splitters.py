## 16th task of advent of code
from utils.inputs import get_data_set, get_test_data_set
from collections import defaultdict

data = get_data_set(2023,16)

EAST = 1
WEST = 2
NORTH = 3
SOUTH = 4

def move_beam(x, y, direction):
    if direction == EAST:
        return x+1, y
    elif direction == WEST:
        return x-1, y
    elif direction == NORTH:
        return x, y-1
    elif direction == SOUTH:
        return x, y+1
    else:
        raise NotImplementedError 

def get_energized_squares(grid, beam_directions=[(0,0,EAST)]):
    cache = defaultdict(lambda: 0)
    energised_field = defaultdict(lambda: 0)

    nrows = len(data)
    ncols = len(data[0])
    while len(beam_directions) > 0:

        next_beam_directions = []
        last_10_steps = [0]*10

        for x, y, direction in beam_directions:

            # If this beam already was in this direction, it won't energize new tiles anymore
            if (x, y, direction) in cache:
                continue

            # If out of bounds, skip this direction
            if (direction==EAST) and  (x > (ncols-1)):
                continue
            if (direction==WEST) and  (x < 0):
                continue
            if (direction==NORTH) and  (y < 0):
                continue
            if (direction==SOUTH) and  (y > (nrows -1) ):
                continue
    
            # Energise fields, and also cache this direction, as it will be solved in this run
            energised_field[(x, y)] += 1
            cache[(x, y, direction)] +=1


            # Cases when beams direction wont change
            if data[y][x] == '.' or ((data[y][x]=='|')  and (direction in (SOUTH, NORTH))) or ((data[y][x]=='-')  and (direction in (EAST, WEST))):
                next_x, next_y = move_beam(x, y, direction)
                next_beam_directions.append((next_x, next_y, direction))
            
            # Cases when beams will take 90 deg turns
            elif data[y][x] == "\\":                
                if direction == EAST:
                    next_x, next_y = move_beam(x, y, SOUTH)
                    next_beam_directions.append((next_x, next_y, SOUTH))    
                elif direction == WEST:
                    next_x, next_y = move_beam(x, y, NORTH)
                    next_beam_directions.append((next_x, next_y, NORTH))    
                elif direction == SOUTH:
                    next_x, next_y = move_beam(x, y, EAST)
                    next_beam_directions.append((next_x, next_y, EAST))    
                elif direction == NORTH:
                    next_x, next_y = move_beam(x, y, WEST)
                    next_beam_directions.append((next_x, next_y, WEST))     
            
            # Cases when beams will take 90 deg turns
            elif data[y][x] == "/":        
                if direction == EAST:
                    next_x, next_y = move_beam(x, y, NORTH)
                    next_beam_directions.append((next_x, next_y, NORTH))    
                elif direction == WEST:
                    next_x, next_y = move_beam(x, y, SOUTH)
                    next_beam_directions.append((next_x, next_y, SOUTH))    
                elif direction == SOUTH:
                    next_x, next_y = move_beam(x, y, WEST)
                    next_beam_directions.append((next_x, next_y, WEST))    
                elif direction == NORTH:
                    next_x, next_y = move_beam(x, y, EAST)
                    next_beam_directions.append((next_x, next_y, EAST))     
            
            # Cases when beam will split
            elif data[y][x] == "|" and direction in (EAST, WEST):        
                next_x, next_y = move_beam(x, y, NORTH)
                next_beam_directions.append((next_x, next_y, NORTH))    
                next_x, next_y = move_beam(x, y, SOUTH)
                next_beam_directions.append((next_x, next_y, SOUTH))    
           
            # Cases when beam will split
            elif data[y][x] == "-" and direction in (SOUTH, NORTH):        
                next_x, next_y = move_beam(x, y, EAST)
                next_beam_directions.append((next_x, next_y, EAST))    
                next_x, next_y = move_beam(x, y, WEST)
                next_beam_directions.append((next_x, next_y, WEST))    
            
            # Should never trigger
            else:
                raise NotImplementedError
        
        beam_directions = next_beam_directions
        last_10_steps.insert(0,len(energised_field))
        last_10_steps = last_10_steps[0:10]

        if len(set(last_10_steps)) == 1:
            return len(energised_field)
    return len(energised_field)

# Part 1
result = get_energized_squares(data, beam_directions=[(0,0,EAST)])

print(result)


# Part 2
dists = []
for start_x in range(0,len(data)):
    dists.append(get_energized_squares(data, beam_directions=[(start_x, 0, SOUTH)]))
for start_y in range(0,len(data[0])):
    dists.append(get_energized_squares(data, beam_directions=[(0, start_y, EAST)]))
for start_x in range(0,len(data)):
    dists.append(get_energized_squares(data, beam_directions=[(start_x, len(data[0])-1, NORTH)]))
for start_y in range(0,len(data[0])):
    dists.append(get_energized_squares(data, beam_directions=[(len(data)-1, start_y, WEST)]))

print(max(dists))