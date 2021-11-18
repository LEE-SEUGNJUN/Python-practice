##code10-16을 수정하여 shift+화살표 키를 누르면 화살표키가 출력되도록 해보자
from tkinter import *
from tkinter import messagebox
##함수 선언 부분##
def keyEvent(event):
    str1="눌린키 : Shift + "
    if event.keycode== 37: ##왼쪽 화살표의 이벤트코드
        messagebox.showinfo("키보드이벤트",str1+"왼쪽 화살표")
    elif event.keycode ==38: ##위쪽 화살표의 이벤트코드
        messagebox.showinfo("키보드이벤트",str1+"위쪽 화살표")
    elif event.keycode ==39: ##오른쪽 화살표의 이벤트코드
        messagebox.showinfo("키보드이벤트",str1+"오른쪽 화살표")
    elif event.keycode ==40: ##아래쪽 화살표의 이벤트코드
        messagebox.showinfo("키보드이벤트",str1+"아래쪽 화살표")
##메인 코드 부분##
window=Tk()
window.bind("<Shift-Up>", keyEvent) ##shift와 위쪽 방향키를 누르면 이벤트 발생, keyEvent 함수 실행,   
window.bind("<Shift-Down>", keyEvent) ##shift와 아래쪽 방향키를 누르면 이벤트 발생, keyEvent 함수 실행,   
window.bind("<Shift-Left>", keyEvent)  ##shift와 왼쪽 방향키를 누르면 이벤트 발생, keyEvent 함수 실행,   
window.bind("<Shift-Right>", keyEvent) ##shift와 오른쪽 방향키를 누르면 이벤트 발생, keyEvent 함수 실행,   
window.mainloop()