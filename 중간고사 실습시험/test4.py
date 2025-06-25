long_str = input("길이가 50 이상인 문자열을 입력하세요: ")

# 초기화
uppercase_count = 0
lowercase_count = 0
whitespace_count = 0
num_count = 0
special_count = 0

# 각 문자열을 확인하면서 카테고리에 해당하는 개수 증가
for char in long_str:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isspace():
        whitespace_count += 1
    elif char.isdigit():
        num_count += 1
    else:
        special_count += 1

# 결과 출력
print("대문자 개수:", uppercase_count)
print("소문자 개수:", lowercase_count)
print("공백문자 개수:", whitespace_count)
print("숫자 개수:", num_count)
print("특수문자 개수:", special_count)
