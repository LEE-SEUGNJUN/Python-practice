##10개의 숫자를 입력받고 합계를 나오게하는 코드
aa=[] ## aa라는 배열 생성
i=0
sum=0
while (True): ##무한 반복
    a=int(input("값을 입력하시오 : "))
    aa.append(a) ## a에 입력한 숫자를 aa배열에 인덱스 [0] 부터[n]까지 순차적으로 추가
    sum = sum+ aa[i] ##aa 배열의 값을 받을때마다 sum에 더한다
    i+=1 ## i 는 1씩늘어나고 
    if i == 10 : ##i가 10이 되면
        break ##반복문 종료 
print(sum) ## sum을 한번에
