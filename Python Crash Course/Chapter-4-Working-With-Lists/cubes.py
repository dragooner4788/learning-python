cubes = list(range(1, 11))

for cube in cubes:
    print(cube ** 3)


cubes = [print(cube ** 3) for cube in range(1, 11)]
