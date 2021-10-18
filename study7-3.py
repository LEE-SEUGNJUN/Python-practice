##4행 5열의 2차원 리스트를 만들고 3의 배수가 들어가도록 입력하고 출력하기

list1=[] ##1차원list가 될 변수
list2=[] ##2차원list가 될 변수
Value=0
for i in range(0,4,1): #바깥for문은 행을 책임진다 
    for k in range(0,5,1): #안쪽for문은 
        list1.append(Value) ##초깃값 0을넣고 
        Value+=3 ## 3의 배수를 넣으려고하니까 3씩 증가시켜준다
    list2.append(list1) ##안쪽for문을 다넣으면 한 행에 다 대입시켜준다
    list1=[] ##list2리스트에 리스트를 넣어주고(2차원리스트를 만들어주고) 한행이 끝나면 초기화
    
for i in range(0,4): 
    for k in range(0,5):
        print(list2[i][k],end=" ") ##i가(행이) 고정될때 열에 해당하는 숫자들이 가로로 프린트
    print("") # 안쪽 for문이 다 끝나고 행이 바뀔때 다음줄로
