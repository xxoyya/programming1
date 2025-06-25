# 리스트에 계수값 저장
list_coefficients = []
n = 0

while True:

    if n < 2:
        degree = int(input("차수 입력(2~4) : "))

        for i in range(degree, -1, -1):
            num = int(input("%d 차 계수 입력 : " % i))
            list_coefficients.append(num)

        x = int(input("x값 입력 : "))

        sum_result = 0
        result_string = ""

        # 1차부터 n차 계산
        for i in range(degree, 0, -1):
            tmp = 1
            result_string += ("%dx^%d + " % (list_coefficients[i], i))
            
            tmp *= list_coefficients[i]
            for j in range(i):
                tmp *= x

            sum_result += tmp

        # 0차 계산
        sum_result += list_coefficients[0]

        result_string += ("%d, x=%d -> %d" % (list_coefficients[0], x, sum_result))

        print(result_string)

        n += 1
