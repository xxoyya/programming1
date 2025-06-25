print('<서울버스터미널>')
dest = input('행선지를 입력하세요: ')
time = None
fare = None
match dest:
    case '대전':
        time = 2
        fare = 20000
    case '대구':
        time = 3
        fare = 30000
    case '광주':
        time = 3
        fare = 35000
    case '부산':
        time = 4
        fare = 40000

if time == None and fare == None:
    print("운행하지 않는 행선지입니다.")
else:
    print(f"{dest}까지 소요시간은 {time}시간, 요금은 {fare}원 입니다.")
        
