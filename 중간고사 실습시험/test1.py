original_matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# 바뀐 결과를 저장할 빈 리스트 생성
TR = []

# 행과 열 바꾸는 반복문
for col in range(len(original_matrix[0])):
    new_row = []
    for row in original_matrix:
        new_row.append(row[col])
    TR.append(new_row)

# 결과 출력
for row in TR:
    print(row)

