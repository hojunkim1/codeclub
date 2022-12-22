Kind = ['물', '콜라', '사이다', '밀키스', '초코라떼', '토레타']
Price = [500, 800, 800, 1000, 1000, 1200]

Have_Money = int(input("돈을 투입하시오 : "))

for i in range(0, 6):
    print(Kind[i], end=' = ')
    print(Price[i], end='원\n')

select = input("위의 중에서 하나를 고르시오 : ")

if select in Kind:
    search = Kind.index(select)
    if Price[search] <= Have_Money:
        print(Kind[search] + "이 나왔습니다")
        change = str(Have_Money - Price[search])
        print("잔돈은 " + change + "원 입니다.")
    else:
        print("돈이 부족합니다")
else:
    print("없는 메뉴를 입력하셨습니다.")
