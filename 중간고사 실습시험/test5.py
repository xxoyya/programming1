degree = int(input("차수 입력(2~4) : "))

list = []
sum = 0
str = ""

x = int(input("x값 입력 : "))

# 1~n차 계산
for i in range(0, len(list)-1):
    tmp = 1
    str += ("%dx^%d+" % (list[i], (degree-i)))

    tmp *= list[i]
    for j in range(degree-i):
        tmp *= x

    sum += tmp
      
    # 0차 계산
    sum += list[degree]
      
    str += ("%d " % list[degree])
    str += (", x=%d -> %d" % (x, sum))



# 리스트에 계수값 저장
for i in range(degree, -1, -1):
    num = int(input("%d 차 계수 입력 : " % i))
    list.append(num)

