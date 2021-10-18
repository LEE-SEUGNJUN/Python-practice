## while문으로 시작값 끝값 증가값 사용자가 입력하여 합계 구하기 
start,end,plus,sum=0,0,0,0
start=int(input("시작 값을 입력하세요 : "))
end= int(input("끝 값을 입력하세요 : "))
plus = int(input("증가 값을 입력하세요 : "))
while(start <= end): ##시작값이 끝값보다 커질시 반복문 종료
    sum = sum + start ##sum에 시작값을 넣고 시작
    start+=plus ## start에는 증가값plus를 반복문이 한번 끝날때마다 더한다
print("시작값:%d,끝값=%d,증가값=%d, 시작값부터 끝 값까지의 합계=%d" %(start,end,plus,sum))
    
    

    