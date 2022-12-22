import random

# 암호화 키 (알파벳) 선언
alpha = "abcdefghajklmnopqrstuvwxyz"
alpha = list(alpha)

# 복호화 키 선언
decrypt_key = "abcdefghajklmnopqrstuvwxyz"
decrypt_key = list(decrypt_key)

# 복호화 키 순서 섞기
random.shuffle(decrypt_key)

# 평문 선언
plain = input("평문: ")
plain = list(plain)

# 평문 데이터 변형
for x in range(len(plain)):
    # 비어있는 칸 치환하기
    if plain[x] == ' ':
        plain[x] = '-'

    # 암호화
    for y in range(len(decrypt_key)):
        if plain[x] == decrypt_key[y]:
            plain[x] = alpha[y]
            break

# 출력
for i in plain:
    print(i, end="")
print()
