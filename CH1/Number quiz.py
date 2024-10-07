import random

a = random.randrange(1, 11)

print("1과 10 사이의 숫자를 하나 정했습니다.")
print("이 숫자는 무엇일까요?")

while 1:
    N = int(input("예상 숫자: "))

    if 11 > N and N > a:
        print("정답보다 큽니다. 다시 입력하세요")
    elif 11 > N and N < a:
        print("정답보다 작습니다. 다시 입력하세요.")
    elif a == N:
        print("정답입니다!")
        coin = input("게임을 다시 하시겠습니까?(y/n): ")
        if coin == 'y':
            a = random.randrange(1, 11)
            continue
        elif coin == 'n':
            break
    else:
        print("정답은 1과 10사이의 수입니다. 다시 잘 생각해보세요.")