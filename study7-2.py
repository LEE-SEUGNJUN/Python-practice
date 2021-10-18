##aa리스트에 3의배수를 200개 넣고 bb에 역순으로 넣어주기
aa,bb=[],[] ## aa,bb배열 생성 
i=0
k=0
while True: ##무한반복 
    
    if  i % 3 ==0 : ## i가 3의 배수가 되면 
        aa.append(i) ##그 i에 해당하는 숫자를 aa배열에 넣고
    if len(aa)==200 : ##aa배열의 원소 갯수가200개가되면(aa[0]~aa[199])
        break ## 반복문 종료
    i+=1
    
while True :
    k+=1
    bb.append(aa[200-k]) ##bb배열에는 aa[199] 부터해서 aa[0] 까지 값 추가
    if len(bb) == 200: ## 200개가 다 채워지면 aa배열의 역순으로 bb에는 추가돼있음
        break 
print(bb[0],bb[199],aa[0],aa[199]) ## bb[0] = aa[199], bb[199]= aa[0]이다
    