# 작성일 : 2023년 09월 20일
# 작성자 : 컴소부 201895101 허남진
# 설명 : if ~ else
# random 을 이용한 가위바위보 게임.
# random 함수로 생성된 정수를 가지고 게임을 진행합니다 (0:가위 ,1:바위 ,2: 보)
from random import randrange

print("********************가위 바위 보 게임 시작***********************")
player1=input("player1의 이름 >>>")
player2=input("player2의 이름 >>>")

num1=randrange(3)
num2=randrange(3)

print(f"{player1}" ,end=" ")
if num1 == 0:
    print("은(는) 가위를 냈습니다")
elif num1 ==1:
    print("은(는) 바위를 냈습니다")
else :
    print("은(는) 보를 냈습니다")

print(f"{player2}",end=" ")
if num2 == 0:
    print("은(는) 가위를 냈습니다")
elif num2 ==1:
    print("은(는) 바위를 냈습니다")
else :
    print("은(는) 보를 냈습니다")

if abs(num1-num2)>1:
    if num1>num2:
        print(f"{player2}가 이겼습니다")
    else :
        print(f"{player1}가 이겼습니다")
else :
    if num1>num2:
        print(f"{player1}가 이겼습니다")
    elif num1==num2:
        print("비겼습니다") 
    else :
        print(f"{player2}가 이겼습니다")