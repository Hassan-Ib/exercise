location = {0: {'desc': 'you are sitting in front of your pc learning python',
                'exits': {},
                'newExit': {}},
            1: {'desc': 'you are standing at the end of a road',
                'exits': {'W': 2, 'E': 3, 'S': 4, 'Q': 0, 'N': 5},
                'newExit': {'2': 2, '3': 3, '4': 4, '5': 5}},
            2: {'desc': 'you are at the top of a hill',
                'exits': {'N': 5, 'Q': 0},
                'newExit': {'5': 5}},
            3: {'desc': 'you are inside a building, a well house for a small stream',
                'exits': {'W': 1, 'Q': 0},
                'newExit': {'1': 1}},
            4: {'desc': 'you are in a vally beside a stream',
                'exits': {'N': 1, 'W': 2, 'Q': 0},
                'newExit': {'1': 1, '2': 2}},
            5: {'desc': 'you are in the forest',
                'exits': {'W': 2, 'S': 1, 'Q': 0},
                'newExit': {'2': 2, '1': 1}},
            'words': {'WEST': 'W',
                      'NORTH': 'N',
                      'SOUTH': 'S',
                      'EAST': 'E',
                      'QUIT': 'Q',
                      'ROAD': '1',
                      'HILL': '2',
                      'BUILDING': '3',
                      'VALLY': '4',
                      'FOREST': '5'}}

# exit = {0: {'Q': 0},
#         1: {'W': 2, 'E': 3, 'S': 4, 'Q': 0, 'N': 5},
#         2: {'N': 5, 'Q': 0},
#         3: {'W': 1, 'Q': 0},
#         4: {'N': 1, 'W': 2, 'Q': 0},
#         5: {'W': 2, 'S': 1, 'Q': 0}}

# f_exit = {1: {'2': 2, '3': 3, '4': 4, '5': 5},
#           2: {'5': 5},
#           3: {'1': 1},
#           4: {'1': 1, '2': 2},
#           5: {'2': 2, '1': 1}}

# words = {'WEST': 'W',
#          'NORTH': 'N',
#          'SOUTH': 'S',
#          'EAST': 'E',
#          'QUIT': 'Q',
#          'ROAD': '1',
#          'HILL': '2',
#          'BUILDING': '3',
#          'VALLY': '4',
#          'FOREST': '5'}

# print(location[1]['exits'])
# print(location[1].keys())
# print(location[1])
loc = 1
while True:
    available_exit = ', '.join(location[loc]['exits'].keys())
    print(location[loc]['desc'])

    if loc == 0:
        break
    else:
        allExit = location[loc]['exits'].copy()
        allExit.update(location[loc]['newExit'])

    direction = input('Available exits are ' + available_exit + ' ').upper()
    print()
    if len(direction) > 1:
        word = direction.split()
        for i in word:
            if i in location['words']:
                direction = location['words'][i]

    if direction in allExit:
        loc = allExit[direction]
    else:
        print('you cannot go in that direction')


