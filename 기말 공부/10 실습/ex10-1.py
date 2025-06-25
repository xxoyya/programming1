def transpose(x):
    return list(zip(*x))

def issymmetric(x):
    y = transpose(x)
    for row in range(0, len(x)):
        for col in range(0, len(x)):
            if row == col: continue
            if x[row][col] != y[row][col]: return False

    return True

def matrix_mult(x,y):
    result = []
    for i in range(0, len(x)):
        result.append([])
        for j in range(0, len(x)):
            result[i].append(0)
            for k in range(0, len(x)):
                result[i][j] += x[i][k] * y[k][j]

    return result

x = [[1,2],
     [3,4]]

y = [[1,0],
     [0,1]]

print(x)
print(f"x 는 대칭행렬? {issymmetric(x)}")
print(y)
print(f"y 는 대칭행렬? {issymmetric(y)}")

print(x)
print(transpose(x))
u = matrix_mult(x, transpose(x))
print(u)
print(issymmetric(u))

        
