##code 11-04를 수정해서 다음과 같이 앞에 각 행 번호를 출력해보자.
inFp=None # 입력파일
inList,inStr= [] , "" ##readlines()는 해당data1.txt파일의 모든내용을 
##줄바꿈을 기준으로 리스트로반환해주기때문에 빈 리스트 변수하나 생성. 
i=1

inFp=open("C:/Temp/data1.txt", "r", encoding="utf-8")

inList=inFp.readlines()
for k in range (len(inList)): ##줄바꿈 기준으로 List에 담기므로 3줄이니까 3개의 원소가있는것이다. 고로 길이는 3이니까 0,1,2 3번 반복
    print("%d:%s"%(i,inList[k]),end="") ## 앞에는 i를 붙여번호를 부여하고 k를이용해 인덱스를 for문으로 하나씩올린다. 원소(한줄씩)하나씩 출력될것이다
    i+=1

inFp.close()