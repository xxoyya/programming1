Ma = [[1,0,0],
      [0,1,0],
      [0,0,1]]

Mb = [[9,8,7],
      [6,5,4],
      [3,2,1]]

Madd = [[0,0,0],
        [0,0,0],
        [0,0,0]]

Msub = [[0,0,0],
        [0,0,0],
        [0,0,0]]

Mmult = [[0,0,0],
         [0,0,0],
         [0,0,0]]

print('A = ', end = '')
for x in range(0,3):
    print('\t', Ma[x])

print()
print('B = ', end = '')
for x in range(0,3):
    print('\t', Mb[x])

print()
print('A+B = ', end = '')
for x in range(0,3):
    for y in range(0,3):
        Madd[x][y] = Ma[x][y] + Mb[x][y]
    print('\t', Madd[x])

print()
print('A-B = ', end = '')
for x in range(0,3):
    for y in range(0,3):
        Msub[x][y] = Ma[x][y] - Mb[x][y]
    print('\t', Msub[x])

print()
print('A*B = ', end = '')
for x in range(0,3):
    for y in range(0,3):
        for k in range(0,3):
            Mmult[x][y] += Ma[x][k] * Mb[k][y]
    print('\t', Mmult[x])
