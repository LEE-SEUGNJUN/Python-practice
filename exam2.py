import turtle; import random ;import sqlite3; import time
##전역 변수 선언 부분##
swidth, sheight,pSize, exitCount=300,300,3,0
r,g,b,angle,dist,curX,curY=[0]*7
DBroot="C:/sqlite/sqlite-tools-win32-x86-3360000/sqlite-tools-win32-x86-3360000/turtleDB"
lineid=0
num=0
##DB연결 및 테이블 생성 ##
con=sqlite3.connect(DBroot) ##DB연결
cur=con.cursor()##통로생성
cur.execute("drop table if exists turtleTable;")##만약 turtleTable이 기존에 있었다면 drop.(한번 실행하면 테이블이 생성되기때문에 두번째엔 지우고해줘야한다)
cur.execute("create table turtleTable(선분ID int,색상R int,색상G int,색상B int,순번 int, X좌표 int,Y좌표 int);")##테이블생성
##메인코드 부분##
turtle.title("거북이 이동좌표 DB에 저장하기")
turtle.shape("turtle")
turtle.pensize(pSize)
turtle.setup(width=swidth+30,height=sheight+30)
turtle.screensize(swidth,sheight)
lineid=1 ##선분아이디 1로 초기화 
while True: ##짧은 선분 마다 색깔,각도,전진길이 등등 초기화시켜주기
    global num1,num2
    r=random.random() ##색깔임의로 저장
    g=random.random()
    b=random.random()
    turtle.color((r,g,b))
    angle=random.randrange(0,360) ##각도 랜덤설정
    dist=random.randrange(1,100) ##앞으로 얼마나 나가아갈지 랜덤설정
    turtle.left(angle); turtle.forward(dist) ##왼쪽으로 angle각도만큼 틀고, 앞으로 dist만큼 전진
    curX=turtle.xcor(); curY=turtle.ycor(); ##현재 turtule의 좌표를 받아 저장
    if (-swidth/2 <= curX and curX <=swidth/2) and(-sheight/2 <=curY and curY <= sheight/2) :
       num+=1
       sql = "insert into turtleTable values('" +str(lineid)+ "','" +str("%.2f"%r)+ "' , '" +str("%.2f"%g) + "' , '" +str("%.2f"%b)+ "' , '" +str(num)+ "','" +str("%.2f"%curX)+ "','" +str("%.2f"%curY)+ "')"
       cur.execute(sql)
       num1 = round(turtle.xcor()) ##반올림
       num2 = round(turtle.ycor()) ##반올림
    else: ##밖으로나가면 펜들고 다시 중앙으로 가서 다시 펜 내리고 그리기 시작
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        lineid+=1 ##밖으로 나가면 선분아이디는 하나 up
        num=0 ## 선분마다의 횟수는 초기화
        exitCount+=1 ##밖으로 나간횟수 하나 up
        if exitCount >=3: ##5번 밖으로 나가면 DB연결을 저장하고 종료 그리기종료
            con.commit()
            break
print("선분ID 색상R 색상G 색상B 순번 x좌표 y좌표")

cur.execute("SELECT * FROM turtleTable")
while True:
    row = cur.fetchone()

    if row == None:
        break;

    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    data5 = row[4]
    data6 = row[5]
    data7 = row[6]
    print("%6d %5s %5s %5s %5s %5s %5s" % (data1, data2, data3, data4, data5, data6, data7))


turtle.clear() ##그리기를 종료한후에 그림을 다 clear시킴
time.sleep(3)
sql = "SELECT * FROM turtleTable WHERE 선분ID = 3" ##DB에서 선분ID가 5인ROW만 조회한단 문장을 sql변수에저장
cur.execute(sql) ##sql변수를 넣어서 그것을 실행
rows = cur.fetchall() ## 그 조회 결과를 한번에 튜플을 리스트화 시켜서 가져옴
turtle.penup()
turtle.pencolor(r,g,b)
turtle.goto(num1, num2) 
turtle.pendown()
turtle.goto(rows[len(rows)-1][5], rows[len(rows)-1][6]) ##fetchall한거에서 len(rows)=마지막인덱스, 즉 5번선분의 마지막 선의 x,y좌료포 이동
## 현재 lineid=6이니까## 
print("--------------------------------역순으로 출력------------------------------------")
print("선분ID 색상R 색상G 색상B 순번 X좌표 y좌표")
for i in range(lineid-1, -1, -1): ##선분id 5부터 1까지 역순으로 그리기 2중 for문
    sql = "SELECT * FROM turtleTable WHERE 선분ID = ('" + str(i) + "')" ##선분아이디 조회
    cur.execute(sql)
    rows = cur.fetchall() ## 리스트안에 튜플형식으로 다 받아옴
    turtle.penup() ## 펜올리고 
    
    for g in range(len(rows)-1, -1, -1): ##선분 ID마다 선들이 역순으로 그려지고 펜컬러가 바뀜
        turtle.goto(rows[g][5], rows[g][6]) 
        turtle.down()
        turtle.pencolor((rows[g][1], rows[g][2], rows[g][3]))
        a=[]
        for item in rows[g] :  ##rows 안에 데이터값 하나하나를 item변수에 받아서 
            a.append(item) ## a리스트에 추가하고 
            i+=1
        ## sql 문으로 다시 역순으로 테이블에 추가한다
        sql="insert into turtleTable values('"+str(a[0])+"','"+str(a[1])+"','"+str(a[2])+"','"+str(a[3])+"','"+str(a[4])+"','"+str(a[5])+"','"+str(a[6])+"')"
        cur.execute(sql)
        ##역순 테이블을 print문으로 출력한다
        print("%6d %5s %5s %5s %5s %5s %5s" % (a[0], a[1], a[2], a[3], a[4], a[5], a[6]))
        
        
    turtle.goto(0, 0) ##
con.commit()
con.close() ##DB연결 종료
turtle.done() ##터틀 종료