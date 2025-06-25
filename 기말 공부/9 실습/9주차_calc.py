def add(a,b): return a+b
def sub(a,b): return a-b
def mult(a,b): return a*b
def div(a,b): return a/b
def power(a,b): return a**b

while True:
    expr = input("계산식을 입력하세요: ")
    
    if expr == '0':
        print("프로그램을 종료합니다.")
        break

    expr_components = expr.split()
    if len(expr_components) < 3:
        print("잘못된 표현식입니다.")
        print()
        continue

    left_operand = float(expr_components[0])
    op = expr_components[1]
    right_operand = float(expr_components[2])

    match op:
        case '+':
            print(expr, '=', add(left_operand, right_operand))
        case '-':
            print(expr, '=', sub(left_operand, right_operand))
        case '*':
            print(expr, '=', mult(left_operand, right_operand))
        case '/':
            if right_operand == 0:
                print("0으로 나눌 수 없습니다.")
            else:
                print(expr, '=', div(left_operand, right_operand))
        case '^':
            print(expr, '=', power(left_operand, right_operand))
        case _:
            print("잘못된 계산식입니다.")
    print()