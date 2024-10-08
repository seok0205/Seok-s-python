import random

RandomNum = random.randrange(1, 11) #무작위의 정수를 1에서 11사이에서 지정.

print("1과 10 사이의 숫자를 하나 정했습니다.")
print("이 숫자는 무엇일까요?")

while 1:    #정답이 틀리면 계속 입력받아야 함. while 반복 사용.
    N = int(input("예상 숫자: "))   #정답 입력.

    if 11 > N and N > RandomNum:    #if-elif-else문에서는 입력 받은 정답 판단 후 상황에 맞는 문장 출력.
        print("정답보다 큽니다. 다시 입력하세요")
    elif 11 > N and N < RandomNum:
        print("정답보다 작습니다. 다시 입력하세요.")
    elif RandomNum == N:    #만약 정답일 경우,
        print("정답입니다!")
        coin = input("게임을 다시 하시겠습니까?(y/n): ")    #게임 재시작 여부 변수 coin에 yes or no 입력.
        if coin == 'y': #y면 RandomNum다시 정하고 while문의 처음으로 돌아감. 재반복.
            RandomNum = random.randrange(1, 11)
            continue
        elif coin == 'n':   #n이라면 그대로 종료.
            break
    else:   #숫자 입력 범위가 벗어나면 안내문 출력.
        print("정답은 1과 10사이의 수입니다. 다시 잘 생각해보세요.")