import random

KOREAN = "가나다라마바사아자차카타파하"

num = int(input("닉네임 길이: "))

nickname = ""
for i in range(num):
    random_char = random.choice(KOREAN)
    nickname += random_char

print(nickname)
