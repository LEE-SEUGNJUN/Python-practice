import sqlite3
data1,data2,data3,data4="","","",""
con,cur=[None] * 2
con=sqlite3.connect("C:/sqlite/sqlite-tools-win32-x86-3360000/sqlite-tools-win32-x86-3360000/naverDB")
cur=con.cursor() ##커서 연동 (sqlite와 파이썬 통로 연결)
cur.execute("select * from productTable;") ##sql 실행문
print("  pCode    pName   price mount") 
print("===================================")
while True:
    row = cur.fetchone() ##한행씩 튜플형식으로 받아옴
    if row==None :
        break
    ##튜플 안에 인덱스를 변수에 각각 저장한다.
    data1=row[0] 
    data2=row[1]
    data3=row[2]
    data4=row[3]
    print("%5s %5s %5d %5d" % (data1,data2,data3,data4)) ##변수들 한번에 한줄에 출력
    
## con.commit() ## sql문을 저장할 필요가없다. 파이썬에서만 출력할것이기때문에
con.close() ## DBc connect 종료