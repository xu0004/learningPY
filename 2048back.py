import random


def new_game(n):
    map = []

    for i in range(n):
        map.append([0] * n)
    return map


def add_two(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    while(mat[a][b] != 0):
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    mat[a][b] = 2
    return mat


def status(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 2048:
                return 'win'
    for i in range(len(map) - 1):
        for j in range(len(map[0]) - 1):
            if map[i][j] == map[i + 1][j] or map[i][j + 1] == map[i][j]:
                return 'not over'
    for i in range(len(map)):  # check for any zero entries
        for j in range(len(map[0])):
            if map[i][j] == 0:
                return 'not over'
    for k in range(len(map) - 1):  # to check the left/right entries on the last row
        if map[len(map) - 1][k] == map[len(map) - 1][k + 1]:
            return 'not over'
    for j in range(len(map) - 1):  # check up/down entries on last column
        if map[j][len(map) - 1] == map[j + 1][len(map) - 1]:
            return 'not over'
    return 'lose'


def reverse(map):
    new = []
    for i in range(len(map)):
        new.append([])
        for j in range(len(map[0])):
            new[i].append(map[i][len(map[0])-j-1])
    print(map)
    return new


def transpose(map):
    new = []
    for i in range(len(map[0])):
        new.append([])
        for j in range(len(map)):
            new[i].append(map[j][i])
    return new


a = new_game(5)
print(a)
