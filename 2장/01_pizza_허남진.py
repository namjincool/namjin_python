# 작성일 : 2023년 09월 13일
# 작성자 : 학과 학번 이름
# 설명 : 피자의 면적을 구하시오. 피자의 반지름이 필요, 피자의 반지름은 입력을 받아 계산할거
from math import pi
#PI=3.14 3.14는 상수이므로 대문자로 변수 생성
length=int(input("피자의 반지름을 입력해주세요>>>>"))
print("피자의 면적은?",round(length**2*pi,2))
