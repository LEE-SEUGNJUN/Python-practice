##code-11을 실행할때마다 그림이 임의로 뒤섞여서 나타나게 하기
import random
from tkinter import *
from typing import List
## 전역변수 선언 부분##
btnList=[None] * 9 ##버튼들을 리스트로 선언하기위해 리스트선언
fnameList = ["cat.gif","dog.gif","nuguri.gif","hipo.gif","rebit.gif","elephant.gif","saseum.gif","panda.gif","pig.gif"]
##사진들의 이름을 리스트선언
photoList=[None]*9 ##fnameList를 이미지화 시킨 것들을 리스트로 담기위한 리스트 선언
i,k,xPos,yPos,num=[0] *5 ##필요한 변수들0으로 초기화
##메인코드 부분##
window=Tk() ##윈도우 반환
window.geometry("210x210") ##윈도창 가로 210 세로 210으로 설정 
random.shuffle(fnameList) ## frameList를 섞어줘 이미지명 리스트를 셔플하여 photoList,btnList에 영향을 준다.
for i in range(0,9): ##인덱스 0부터 8까지 
    photoList[i]=PhotoImage(file="gif\\"+fnameList[i]) ##gif\그림파일이름 으로 이미지 파일을 생성하여 PhotoList리스트에 하나씩 저장
    btnList[i]=Button(window, image = photoList[i]) ##버튼을 만드는데 버튼은 이미지모양의 버튼을 생성
## 반복문이 끝나고 random.shuffle(photoList) : 버튼 리스트를 셔플해도 이미지가 섞인다.
for i in range(0,3): ## 3행3열로 사진을 배치
    for k in range(0,3):
        btnList[num].place(x=xPos,y=yPos) ##위젯을 고정위치에 배정하기위해 pack대신 place를 사용.
        xPos+=70  ##1행엔 0,0  0,70  0,140에 배치
        num+=1 ##인덱스 하나씩 증가
    xPos=0 ## 다시 x 좌표 초기화하고 
    yPos+=70 ## y좌표는 행에 배치가 끝날때마다 1행씩밑으로 설정
window.mainloop() 