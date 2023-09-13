# 작성일 : 2023년 09월 13일
# 작성자 : 학과 학번 이름
# 설명 : 90페이지 문제 3.9 평균 시속과 이동시간을 입력받아 이동시간은 시,뷴,초 단위로 출력 , 이동한 거리를 계산하여 출력
# 거리 = 속도 * 시간

# 이동 시간 , 이동 거리 

km=float(input("평균 시속을 입력 >>>"))
h=float(input("이동 시간을 입력 >>"))
# 시간과 분 계산
hours = int(h)  # 시간 부분
decimal_part = h - hours  # 소수점 이하 부분
minutes = int(decimal_part * 60)  # 분으로 변환
seconds = int((decimal_part * 60 - minutes) * 60) #초로 변환

print("평균 시속은?>>",km,"km/h")
print("이동 시간 {} 시간 {} 분 {} 초" .format(hours,minutes,seconds))
print("이동 거리 :",km*h,"km")