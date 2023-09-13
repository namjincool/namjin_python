# 작성일 : 2023년 09월 13일
# 작성자 : 학과 학번 이름
# 설명 : 직각 삼각형 빗변의 길이를 구하시오 (밑변과 높이를 입력)
from math import sqrt
length, height=map(int,input().split()) # 밑변과 높이입력
result=(length**2+height**2)
print(result**0.5)
print(sqrt(result)) 