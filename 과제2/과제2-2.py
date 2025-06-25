# from random import random

three = None

while three != 0:
    # num = int(random()*1000)
    num = 465
    three = int(input("세 자리 숫자를 입력하세요"))

    if three < 100 or three > 999:
        print("숫자는 세 자리로 입력해야 합니다.")
        continue
    if three > num:
        print("큽니다. 더 작은 수를 입력하세요")
        continue
    if three < num:
        print("작습니다. 더 큰 수를 입력하세요")
        continue
    elif three == num:
        print("맞췄습니다.")
        break
