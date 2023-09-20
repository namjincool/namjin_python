# 작성일 : 2023년 09월 20일
# 작성자 : 컴소부 201895101 허남진
# 설명 : if ~ else
# random 을 이용한 가위바위보 게임.
# random 함수로 생성된 정수를 가지고 게임을 진행합니다 (0:가위 ,1:바위 ,2: 보)
from random import randrange

print("********************가위 바위 보 게임 시작***********************")
user=int(input("가위 바위 보에서 무엇을 낼지 숫자로 입력해주세요 (0:가위 , 1: 바위 , 2:보)"))
computer=randrange(3) # 0~2까지 랜덤으로 번호 생성

if computer == 0:
    print("가위")
elif computer ==1:
    print("바위")
else :
    print("보")
    