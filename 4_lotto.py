# 랜덤한 숫자를 얻기 위해 불러오는 기능
import random

# 로또 번호 저장하는 리스트와 랜덤한 숫자를 선언 : 데이터 저장 (선언)
lotto = []
rnd_num = random.randint(1, 45)

# 랜덤으로 생성한 숫자가 로또 번호 안에 있는지 체크 : 데이터 변형 (명령)
for i in range(6):
    while rnd_num in lotto:
        rnd_num = random.randint(1, 45)
    lotto.append(rnd_num)

# 로또 번호는 정렬되서 나오기에 정렬 : 데이터 변형 (명령)
lotto.sort()

# 로또 번호 출력 : 데이터 사용 (출력)
print("로또 번호 : ", end='')
for result in lotto:
    print(result, end=' ')
