##code 11-07을 수정해서 파일명도 입력받아 보자.
outFp=None
outStr=""
filename=input("파일명을 입력하세요 : ") ##파일명을 입력
outFp=open(filename,"w",encoding="utf-8") ##파일명 입력받은변수를 오픈파일명으로 씀

while True:
    outStr=input("내용입력 : ") ## 내용을 적음.
    if outStr != "" : ##만약 공백이아니라면, 쓴값이 있다면
        outFp.write(outStr+"\n") ##적고나서 한줄enter함
    else: ##공백이라면 (enter만 치면 종료)
        break ##반복문 종료 !.
outFp.close()
print("----정상적으로 파일에 씀 ----")