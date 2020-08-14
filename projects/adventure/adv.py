from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# MY CODE STARTS HERE
def opp_dir(dir):
    if dir == 'n':
        return 's'
    if dir == 'w':
        return 'e'
    if dir == 's':
        return 'n'
    if dir == 'e':
        return 'w'
    raise KeyError('Incorrect direction')

cur_room = world.starting_room
connections_map = {}
stack = []
path_rooms = []
# this will be the main method by which I add rooms to the map
connections_map[cur_room.id] = {d: '?' for d in cur_room.get_exits()}
stack.append(cur_room)
# print(connections_map[cur_room.id])
while len(connections_map) < len(room_graph):
    # Depth-first traverse through
    cur_room = stack[len(stack) - 1]
    path_rooms.append(cur_room.id)
    # print(cur_room.id)
    # update connection map
    if cur_room.id not in connections_map:
        # place ? where adjacent rooms are
        connections_map[cur_room.id] = {d: '?' for d in cur_room.get_exits()}

    # connect it to the room you were just at
    prev_room = stack[len(stack)-2]
    for d in prev_room.get_exits():
        if prev_room.get_room_in_direction(d).id == cur_room.id:
            connections_map[cur_room.id][opp_dir(d)] = prev_room.id
            connections_map[prev_room.id][d] = cur_room.id

    # move in a direction that hasn't been explored yet
    for d in cur_room.get_exits():
        if connections_map[cur_room.id][d] == '?':
            new_room = cur_room.get_room_in_direction(d)
            stack.append(new_room)
            break
        
    # dead end: can't go any further without backtracking
    # get all exits in the room that haven't been visited already
    # if all exits have been visited, the list will be empty
    # this loop stops when the list isn't empty
    starting_room = cur_room
    # print(cur_room.id, connections_map[cur_room.id])
    if len(connections_map) < len(room_graph):
        # print(cur_room.id)
        while not [d for d in cur_room.get_exits() if connections_map[cur_room.id][d] == '?']:
            # first iter check: don't double up traversals
            # print(cur_room.id)
            if starting_room.id != cur_room.id:
                path_rooms.append(cur_room.id)
            stack.pop()
            cur_room = stack[len(stack) - 1]

# print(path_rooms)
# turn path_rooms into traversal_path
for i in range(len(path_rooms) - 1):
    for d in connections_map[path_rooms[i]]:
        if connections_map[path_rooms[i]][d] == path_rooms[i + 1]:
            traversal_path.append(d)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
