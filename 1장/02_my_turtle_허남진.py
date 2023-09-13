# 작성일 : 2023년 09월 13일
# 작성자 : 학과 학번 이름
# 설명 : 터틀 그리기

import turtle as t # 터틀 모듈을 사용하기 위한 준비
#turtle 클래스 객체를 t로 생성. (별명)

t.shape('turtle') # 모양
t.speed(2) # 속도 조절 

#선 그리기 
#t.forward(200) # 200 픽셀 이동.

#정삼각형 그리기 (세변의 길이가 같고, 크기가 같다)
# t.forward(200) #그려
# t.left(120) # 왼쪽으로 120도 틀어
# t.forward(200) 
# t.left(120)
# t.forward(200)
# t.left(120)

#반복문으로 별 그리기
for _ in range (5):
    t.forward(100) #그려
    t.left(144) # 왼쪽으로 120도 틀어
t.mainloop() # 그림판 사라지지 않는 코드
