##code10-12를 수정하여 버튼 사이에 파일명을 표시해보자.
##code10-12에서 수정부분만 주석처리 하였다
from tkinter import *
##전역변수 부분##
fnameList = ["cat.gif","dog.gif","nuguri.gif","hipo.gif","rebit.gif","elephant.gif","saseum.gif","panda.gif","pig.gif"]
photoList=[None] * 9; num=0
##함수 선언 부분##
def clickNext():
    global num; 
    num +=1;
    if num > 8:
        num=0
    label1.configure(text=fnameList[num])## num인덱션에 따라서 label1의 텍스트 속성을 변경해준다
    photo=PhotoImage(file="gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image= photo
def clickPrev():
    global num
    num-=1
    if num<0:
        num=8
    label1.configure(text=fnameList[num])##num인덱션에 따라서 label1의 텍스트 속성을 변경해준다
    photo=PhotoImage(file="gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image= photo
##메인코드부분##
window=Tk()
window.geometry("700x500")
window.title("사진 앨범보기")
btnPrev=Button(window,text="<< 이전",command=clickPrev)
btnNext=Button(window,text="다음 >>",command=clickNext)
window.bind("<Up>",clickNext)
window.bind("<Down>",clickPrev)
photo=PhotoImage(file="gif/"+fnameList[0])
pLabel=Label(window,image=photo)
label1=Label(window,text=fnameList[0]) ##레이블을 만들고 레이블명은 label1 그리고 text 초깃값은 사진초깃값과 동일한 인덱션으로한다.
btnPrev.place(x=250,y=10)
label1.place(x=325,y=10) ##이전 버튼고 다음버튼의 중간으로 설정해놓았다.
btnNext.place(x=400,y=10)
pLabel.place(x=300,y=200)
window.mainloop()