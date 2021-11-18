##cpde 11-08을 수정해서 두 파일 모두 파일명을 입력받아보자.

inFp,outFp=None,None
inStr=""
inFilename=input("복사할 파일경로와 파일이름을 입력하세요 : ")
outFilename=input("붙여넣기할 파일경로와 파일이름을 입력하세요 : ")
inFp=open(inFilename,"r",encoding="utf-8") ## 읽기 모드로 파일 오픈
outFp=open(outFilename,"w",encoding="utf-8") ## 쓰기 모드로 파일 오픈

inList = inFp.readlines() ##inList에 inFp파일을 리스트형태로 모든내용 반환
for inStr in inList: ## 리스트의 원소(한줄씩)를 하나씩 inStr에 반환 
    outFp.writelines(inStr) ##리스트의 한줄씩 outFp에 씀.

inFp.close() ##파일을 둘다 닫음
outFp.close()
print("---파일이 정상적으로 복사 되었음---")