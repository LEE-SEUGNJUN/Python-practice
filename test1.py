import turtle
import random
from tkinter.simpledialog import *
import math
 
## 전역 변수 선언 부분 ##
inStr = ''
swidth, sheight = 300, 300 ##스크린창 크기 설정
tX, tY, txtSize = 0, 0, 20 
radius, angle, radian = 100, 0, 0 ##반지름, 글자가 쓰여지는 각도, 라디안 초기화
 
## 메인 코드 부분 ##
if __name__=="__main__": 
    turtle.title('거북이 원그리며 글씨쓰기') ##제목
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50) ##프로그램창 크기 설정
    turtle.screensize(swidth, sheight) ##스크린사이즈
    turtle.penup() ##펜을 든다 ( 이상태로 펜 이동시 글씨 안쓰여짐)
    
    inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력') ##쓸 글씨 입력받음
    
    angle = 360 / len(inStr)    # 문자열의 개수로 각도 설정 ## 글자가 많으면 많을수록 각도는 줄어든다 
    
    for ch in inStr :
        radian = 3.14*angle/180   # 라디안 구하기
    
        tX = radius*math.cos(radian)   # 좌표 구하기
        tY = radius*math.sin(radian)
        r = random.random(); g = random.random(); b = random.random()
    
        turtle.goto(tX, tY)
    
        turtle.pencolor((r, g, b))
        turtle.write(ch, font=('맑은 고딕', txtSize,  'bold'))
    
        angle += 360 / len(inStr)   # 각도만큼 반시계로 회전
    
    turtle.done()