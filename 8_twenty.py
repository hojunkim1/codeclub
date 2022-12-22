# 스무고개 예시 : 데이터 저장(선언)
List = ['딸기', '사과', '바나나', '귤', '소방차', '루돌프 사슴코', '스쿨버스', '달']

# 예시 출력
for a in range(0, 8):
    print(List[a])
print("위의 예시 중에 하나를 생각해 주세요")

# 질문 입력
question = input("먹을 수 있습니까? (Y / N) : ")
# 각 질문에 따라 스무고개의 예시 데이터를 변형한 후 저장 : 데이터 변형 (명령)
if (question == "Y") or (question == "y") or (question == "네"):
    List = List[:4]
else:
    List = List[4:]

question = input("빨간색입니까? (Y / N) : ")
if (question == "Y") or (question == "y") or (question == "네"):
    List = List[:2]
else:
    List = List[2:]

question = input("동그란 모양입니까? (Y / N) : ")
if (question == "Y") or (question == "y") or (question == "네"):
    Final = List[1]
else:
    Final = List[0]

# 질문이 진행된 후에 예상된 답을 print함수로 출력 : 데이터 사용 (출력)
print("당신이 생각한 답은 : " + Final + "입니다.")
