Ma = [[1,0,0],
      [0,1,0],
      [0,0,1]]

Mb = [[9,8,7],
      [6,5,4],
      [3,2,1]]

def print_matrix(m):
    for x in range(0,len(m)):
        print('\t', m[x])

print('A = ', end = '')
print_matrix(Ma)
print()
print('B = ', end = '')
print_matrix(Mb)
print()

def matrix_add(a, b):
    result = []
    length = len(a)

    for x in range(0,length):
        result.append([])
        for y in range(0,length):
            result[x].append(0)
            result[x][y] = a[x][y] + b[x][y]
    
    return result
    
print('A+B = ', end = '')
print_matrix(matrix_add(Ma, Mb))
print()

def matrix_sub(a, b):
    result = []
    length = len(a)

    for x in range(0,length):
        result.append([])
        for y in range(0,length):
            result[x].append(0)
            result[x][y] = a[x][y] - b[x][y]
    
    return result

print('A-B = ', end = '')
print_matrix(matrix_sub(Ma, Mb))
print()

def matrix_mult(a, b):
    result = []
    length = len(a)

    for x in range(0,length):
        result.append([])
        for y in range(0,length):
            result[x].append(0)
            for k in range(0,length):
                result[x][y] += a[x][k] * b[k][y]
    
    return result

print('A B = ', end = '')
print_matrix(matrix_mult(Ma, Mb))
print()

a=[[1,2],[3,4]]
b=[[4,3],[2,1]]

print_matrix(matrix_mult(a,b))
