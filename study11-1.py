##code 11-02를 수정하여 앞에 각 행번호를 출력해보자.
inFp=None # 입력파일
inStr="" #읽어 온 문자열
i=0 ## 문장하나하나에 번호를 새길 변수
inFp=open("C:/Temp/data1.txt", "r", encoding="utf-8") ## encoding을 안써주니까 cp949 에러가 납니다 전..

while True : ##텍스트의 문장 한줄씩 받아오기
    inStr = inFp.readline()
    i+=1
    if inStr == "" : ##만약 그 줄에 글이 없다면 반복문 종료.
        break
    print("%d:%s" %(i,inStr),end="") ##문장하나씩 받은걸 한줄씩 출력하기
inFp.close() ##open 을 했으니 close를 사용