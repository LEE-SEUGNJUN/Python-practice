##code 10-22를 수정하여 이미지가 회색으로 보이도록하자
from os import path
from tkinter import *
from tkinter.filedialog import *
##함수 선언 부분##
def func_open():
    filename=askopenfilename(parent=window, filetypes=(("GIF파일","*.gif"),("모든 파일","*.*")))
    photo=PhotoImage(file=filename)
    for y in range(0,photo.height()): ## y좌표를 0부터 사진의 높이 크기만큼
        for x in range(0,photo.width()): ##x좌표도 0부터 사진의 넓이크기만큼
            r,g,b = photo.get(x,y) ##픽셀 하나하나마다 사진의 색깔을 받음 get()의 반환값은 사진의 red,green,blue의 튜플형식이기때문에 3개의 변수를 준비
            v=r+g+b//3 ## 받은 값을 3으로 나누어 v에 초기화 -> 회색을 만드는 코드
            photo.put("#%02x%02x%02x" % (v,v,v),(x,y)) ##각각의 픽셀 마다 v,v,v회색값을 대입해준다
    pLabel.configure(image=photo)
    pLabel.image=photo

def func_exit():
    window.quit()
    window.destroy()
##메인코드 부분##
window=Tk()
window.geometry("400x400")
window.title="명화 감상하기"
photo=PhotoImage()
pLabel=Label(window,image=photo)
pLabel.pack(expand=1,anchor=CENTER)

mainMenu=Menu(window)
window.config(menu=mainMenu)
filemenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일",menu=filemenu)
filemenu.add_command(label="파일 열기",command=func_open)
filemenu.add_separator()
filemenu.add_command(label="프로그램 종료",command=func_exit)
window.mainloop()