##code 10-4를 수정해서 이미지 2개가 나오게끔하기
from tkinter import * ##GUI관련 모듈 제공해주는 윈도 라이브러리

window = Tk() ## 윈도우를 반환하여 window에 저장.(window는 윈도우 창 그자체를 뜻)

photo = PhotoImage(file="gif\dog.gif") ##file옵션의 파일명의 이미지를 photo변수에 담는다
photo2 = PhotoImage(file="gif\cat.gif") ##file옵션의 파일명의 이미지를 photo2변수에 담는다
label1=Label(window,image=photo)  ##레이블을 만들어준다.  window창에 띄울것이며, image옵션에는photo변수에 담긴 이미지를 넣는다
label2=Label(window,image=photo2) ##동일
label1.pack(side=LEFT) ##레이블을 띄운다. 왼쪽에 넣는다.
label2.pack() ##레이블을 띄은다. 이미 하나가 왼쪽에 넣어져있으므로 그냥 pack()해도 오른쪽으로 알아서 가로로 들어간다.
window.mainloop() ##위에 설정값을 적용하고 윈도창에 키보드 누르기 마우스클릭 등 다양한 이벤트가 일어날 때까지 윈도창을 띄어준다.