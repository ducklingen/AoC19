import itertools

europa = ((-1, 0, 2), (0,0,0))
io = ((2, -10, -7), (0,0,0))
ganymede = ((4,-8,8), (0,0,0))
callisto = ((3,5,-1), (0,0,0))

moons = [europa, io, ganymede, callisto]

for i in range(3):
    for j in range(3):
        if j > i:
            for k in range(2):
                if moons[i][0][k] > moons[j][0][k]:
                    moons[i][1][k] = moons[i][1][k] - 1
                    moons[j][1][k] = moons[j][1][k] + 1
                elif moons[i][0][k] < moons[j][0][k]:
                    moons[i][1][k] = moons[i][1][k] + 1
                    moons[j][1][k] = moons[j][1][k] - 1

print(moons)