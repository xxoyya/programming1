n = int(input("숫자를 입력하세요: "))
print(n)
while(n > 1):
    if n%2 == 0:
        n //= 2
    else:
        n *= 3
        n += 1
        # n = n*3 +1

    #if n%2 == 1:
    #    n *= 3
    #    n += 1
    #else:
    #    n //= 2

    #match n%2:
    #    case 0:
    #        n //= 2
    #    case 1:
    #        n *= 3
    #        n += 1
    print(n)
