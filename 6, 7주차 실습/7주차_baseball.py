# from random import random
from random import randint

answer = n1 = n2 = n3 = 0

# 중복되는 숫자 체크
while n1 == n2 or n1 == n3 or n2 == n3:
    # answer = int(random()*1000)
    # if answer < 100: continue
    answer = randint(100, 999)
    n1 = answer // 100       # 100의 자리 숫자
    n2 = (answer // 10) % 10 # 10의 자리 숫자
    n3 = answer % 10         # 1의 자리 숫자

#print(answer)

while True:
    strike = ball = 0
    num = int(input("Input 3-digit number: "))
    #print(num)
    if num < 100 or num > 999:
        print("Not 3-digit number!")
        continue
    else:
        n1 = num // 100
        n2 = (num // 10) % 10
        n3 = num % 10
        if n1 == n2 or n1 == n3 or n2 == n3:
            print("Each digit must have a different number.")
            continue

    # 정답의 각 자리수 숫자
    a1 = answer // 100
    a2 = (answer // 10) % 10
    a3 = answer % 10

    # 입력한 숫자의 각 자리수 숫자
    n1 = num // 100
    n2 = (num // 10) % 10
    n3 = num % 10

    # 스트라이크 여부 검사
    if a1 == n1:
        strike = strike + 1
    if a2 == n2:
        strike = strike + 1
    if a3 == n3:
        strike = strike + 1

    # 볼 여부 검사
    if a1 == n2:
        ball = ball + 1
    if a1 == n3:
        ball = ball + 1
    if a2 == n1:
        ball = ball + 1
    if a2 == n3:
        ball = ball + 1
    if a3 == n1:
        ball = ball + 1
    if a3 == n2:
        ball = ball + 1

    # 스트라이크, 볼 카운트 표시
    print(f"{strike} strike {ball} ball")

    # 정답을 맞췄으면 종료
    if strike == 3:
        print("Correct!")
        print("Finish game.")
        break
