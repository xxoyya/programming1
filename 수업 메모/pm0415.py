



'''
marks = [
    {"id": 22, "mark":66},
    {"id": 37, "mark":48},
    {"id": 152, "mark":80},
    {"id":883, "mark":75},
    {"id": 12, "mark":55}
]

for item in marks:
    mark = item ["mark"]
    if mark >= 60:
        print(f"{item["id"]}번 학생은 합격입니다.")
    else:
        print(f"{item["id"]}번 학생은 불합격입니다.")
'''



'''
a = 100
while a < 1000:
    print("최수빈내거하자ㅜㅜ")
    a = a + 100
'''



'''
score = None

while score != 0:
    score = int(input("점수를 입력하세요"))
    if score < 0 or score > 100:
        print("잘못된 점수입니다. 다시 입력하세요.")
        continue
    if score == 0:
        print("프로그램 종료")
        break
    if score > 100:
        print("잘못된 점수입니다")
        continue
    elif score > 90:
        print("A학점입니다")
        break
'''



'''
num = None
while num != 0:
    num = int(input("점수를 입력하세요"))
    if num == 666:
        print("악마의 숫자입니다")
        break
'''



'''
num = 0
while num < 100:
    print(f"count: {num}")
    num += 1
'''



'''
num = 0
count = 0
while num < 100:
    count += 1
    num += count
    print(f"{count}: {num}")
'''