def add_mul(choice, *args):
    if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)  # 순서 맞음

result = add_mul('mul', 1,2,3,4,5)
print(result)  # 순서 맞음

result = add_mul(choice='add', 1,2,3,4,5)
print(result)  # 순서 틀림

result = add_mul(1,2,3,4,5, choice='add')
print(result)  # 순서 틀림
