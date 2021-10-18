import turtle ##tutle.함수 를 사용할수있다
import random ##랜덤값을 받기위해 random 라이브러리를 import
##좌클릭 함수선언##
def ScreenLeftClick(x,y): ##좌클릭을 하면 생기는 이벤트의 함수
    global r,g,b  ##함수밖에서 0으로 초기화한 전역변수 r,g,b를 그대로 가져와 쓰겠단 의미의 global
    r = random.random() ## 0~1사이의 임의의 수 부여
    g = random.random() ## 0~1사이의 임의의 수 부여
    b = random.random() ## 0~1사이의 임의의 수 부여
    tSize = random.randrange(1, 10) ##거북이 사이즈를 1~10의 임의의 크기로 랜덤설정한걸 tSize변수에 넣기
    turtle.shapesize(tSize) ##랜덤으로 입력받은 tSize를 실제 사이즈에 적용
    tAngle = random.randrange(0,360) ##거북이의 각도를 랜덤입력받아 변수 tAngle에 넣음
    turtle.left(tAngle) ##랜덤입력받은 tAngle을 적용
    turtle.color(r,g,b) ## 임의의 값 r,g,b로 색상을 적용
    turtle.penup()  ##커서를 올림
    turtle.goto(x,y) ## x,y좌료포 이동
    turtle.stamp() ##도장을 찍음

r,g,b = 0,0,0 ##전역변수
turtle.title('연습문제 8번') ##창 제목
turtle.shape('turtle') ##거북이로 설정 
turtle.onscreenclick(ScreenLeftClick, 1) ##스크린을 클릭하면 함수가 발동되도록 해줌(함수호출)
turtle.done() ## 실행하자마자 창이 꺼지기때문에 일시정지 함수를 이용해 창을 계속열어둔다