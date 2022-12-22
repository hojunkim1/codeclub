import random

question = random.randint(1, 100)
print("숫자 게임에 오신 것을 환영합니다.")
guess = int(input("1~100 사이의 숫자를 맞춰 보세요 :"))

while True:
    if guess == question:
        print("정답을 맞췄습니다.")
        break
    elif guess > question:
        print("정답보다 큼")
        guess = int(input("1~100 사이의 숫자를 맞춰 보세요 :"))
    else:
        print("정답보다 작음")
        guess = int(input("1~100 사이의 숫자를 맞춰 보세요 :"))

print("게임 종료")
