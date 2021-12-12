import turtle
import random
##전역변수 설정##
myTurtle, tX, tY, tColor, tSize, tShape, tSum = [None] * 7
playerTurtles = [] ##리스트 생성
swidth, sheight = 500, 500 ##스크린 사이즈 적절한 크기로 설정
if __name__ == "__main__" : ##메인함수 시작
    turtle.title('거북 리스트 활용(정렬)') ##프로그램 제목
    turtle.setup(width = swidth + 50, height = sheight + 50) ##프로그램크기 
    turtle.screensize(swidth, sheight) ##스크린창크기wq
    for i in range(0, 10) : ##10번반복
        myTurtle = turtle.Turtle('turtle') #터틀로 설정
        tX = random.randrange(-swidth / 2, swidth / 2)##X좌표는 좌-250,250 사이에 랜덤 => 즉 스크린상아무곳이나 랜덤
        tY = random.randrange(-sheight / 2, sheight / 2) ##y좌표도 마찬가지
        r = random.random(); g = random.random(); b = random.random() #색깔로 쓸 변수인데 랜덤으로 설정
        tSize = random.randrange(1, 3) ##거북이 크기도1~2 둘중하나로 랜덤
        tSum = tX + tY ##좌표의 크기를 합친 변수 (크기가 작은애 부터 정렬 해야하기 때문에)
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b, tSum]) ##plyerTurtles는 2차원 리스트가 됨
    sortedTurtles = sorted(playerTurtles, key = lambda turtles : turtles[7], reverse = True)

##plyerTurtles의 각원소를 lambda(익명함수)의 매개변수 turtles로 받아서 
##좌표가 작은 거북이부터 정렬하여 선을 그리기로 했으므로 
##인덱스7번 (tSum)을 key로하여 playerTurtles를 오름차순으로 정렬하고(sort) 그순서를 역순으로 뒤집는다(reverse)
    
    for index, tList in enumerate(sortedTurtles): ##enumerate는 인덱스와 원소값을 튜플형태로 같이 나오게해줌 그걸 index,tLiST 변수로 받는다
        myTurtle = tList[0] ##미리 만들어둔 myTurtle이란 객체에 tList(reverse)값대입 
        myTurtle.color((tList[4], tList[5], tList[6])) ##tList[4],[5],[6]은 r,g,b로 랜덤으로 임의값을 받은것인데 색깔로 정의한다.
        myTurtle.pencolor((tList[4], tList[5], tList[6])) ## 펜컬러도 마찬가지로 임의의 랜덤인 색깔이다
        myTurtle.turtlesize(tList[3]) ##거북이 크기는 인덱스3번인 tSize를 받아와서 설정
        myTurtle.penup() ##펜을 들어올린다 (거북이 이동시 선을 그리지 않는다.)
        if index == 0 : ##첫번째 거북이는 이전 거북이가 없기때문에 해당 뒤치로 이동만한다.
            myTurtle.goto(tList[1], tList[2])
            continue ## 첫번째 거북이가 끝나면 반복문 위로 다시 올라가고 
        
        myTurtle.goto(tList[1], tList[2]) ## 선을 그으며 임의의 자신의 위치로 이동한다.
        myTurtle.pendown() ##펜을 다시 내리며,(이젠 goto로 움직이면 선을 그리면서 움직인다.)
        myTurtle.goto(sortedTurtles[index-1][1], sortedTurtles[index-1][2]) ##2번째 거북이부터는 이전 거북이의 위치로 이동하고
turtle.done()