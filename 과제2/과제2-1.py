from random import random

num = int(random() * 1000)	  # 무작위 숫자 생성

while num < 100:
    num = int(random()*1000)

while True:
    guess = int(input("세 자리 숫자를 입력하세요: "))
    
    if guess < 100 or guess > 999:
        print("숫자는 세 자리로 입력해야 합니다.")
        continue
    
    if guess > num:
        print("큽니다. 더 작은 수를 입력하세요.")
    elif guess < num:
        print("작습니다. 더 큰 수를 입력하세요.")
    else:
        print("맞췄습니다.")
        break

