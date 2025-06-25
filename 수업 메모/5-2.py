# 첫 번째 입력에 대한 변수
sum_result_1 = 0
result_string_1 = ""

# 두 번째 입력에 대한 변수
sum_result_2 = 0
result_string_2 = ""

n = 0

while True:

    if n < 2:
        degree = int(input("차수 입력(2~4) : "))

        list_coefficients = []

        for i in range(degree, -1, -1):
            num = int(input("%d 차 계수 입력 : " % i))
            list_coefficients.append(num)

        x = int(input("x값 입력 : "))

        if n == 0:
            # 1차부터 n차 계산
            for i in range(degree, 0, -1):
                tmp = 1
                result_string_1 += ("%dx^%d + " % (list_coefficients[i], i))
                
                tmp *= list_coefficients[i]
                for j in range(i):
                    tmp *= x

                sum_result_1 += tmp

            # 0차 계산
            sum_result_1 += list_coefficients[0]

            result_string_1 += ("%d, x=%d -> %d" % (list_coefficients[0], x, sum_result_1))

            print("첫 번째 입력 결과:", result_string_1)

        elif n == 1:
            # 1차부터 n차 계산
            for i in range(degree, 0, -1):
                tmp = 1
                result_string_2 += ("%dx^%d + " % (list_coefficients[i], i))
                
                tmp *= list_coefficients[i]
                for j in range(i):
                    tmp *= x

                sum_result_2 += tmp

            # 0차 계산
            sum_result_2 += list_coefficients[0]

            result_string_2 += ("%d, x=%d -> %d" % (list_coefficients[0], x, sum_result_2))

            print("두 번째 입력 결과:", result_string_2)

        n += 1

        if n == 2:
            # 두 번째 입력 결과와 첫 번째 입력 결과를 곱하여 출력
            print("다항식 곱셈 값:", sum_result_1 * sum_result_2)
            break
