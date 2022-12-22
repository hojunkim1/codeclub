temp = int(input("현재 온도를 입력하시오 : "))
check = input("입력한 온도가 화씨라면 F를 섭씨라면 C를 입력하세요 : ")

if (check == 'F') or (check == 'f'):
    f_temp = temp
    c_temp = (f_temp - 32) * (5 / 9)
    print(f"화씨 온도 {f_temp}는 섭씨 온도로 {c_temp} 입니다")

else:
    c_temp = temp
    f_temp = (c_temp * (9 / 5)) + 32
    print(f"섭씨 온도 {c_temp}는 화씨 온도로 {f_temp} 입니다")
