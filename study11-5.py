##Code11-12를 다음과 같이 수정해보자.
##프로그램을 실행하면 파일 선택 대화상자가 나와서 모든 파일이 선택 가능하도록 한다.
##예외 처리를 활용한다. 예로 GIF등을 선택해서 처리에 실패할 경우, 정상적인 RAW를 선택해서 성공할경우, 종료시에 다음과 같이 메시지가 나오도록하자.
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
##예외처리로 RAW말고 다른 파일이 실행됐을때 메시지박스를 띄우기위함, 파일을열수있게 탐색기역할을 해주는 filedialog임포트

## 함수 선언 부분##
def func_open():
    global filename
    
    filename=askopenfilename(parent=window, filetypes=(("RAW파일","*.raw"),("모든 파일","*.*")))

    return filename

def loadImage(fname) :
    
    global inImage, XSIZE, YSIZE
    fp=open(fname,'rb')
    
    for i in range(0,XSIZE) :
        tmpList=[]
        for k in range(0,YSIZE) :
            data=int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)
    fp.close()

def displayImage(image):
    global XSIZE,YSIZE
    rgbString=""
    for i in range(0,XSIZE):
        tmpString=""
        for k in range(0,YSIZE):
            data=image[i][k]
            tmpString += "#%02x%02x%02x " % (data,data,data)
        rgbString += "{" + tmpString + "} "
    paper.put(rgbString)
## 전역변수 선언 부분 ##
window=None
canvas=None
XSIZE,YSIZE=256,256
inImage=[]

##메인 코드 부분 ##
window=Tk()
window.title("흑백 사진 보기")
canvas=Canvas(window,height=XSIZE,width=YSIZE)
paper=PhotoImage(width=XSIZE,height=YSIZE)
canvas.create_image((XSIZE/2,YSIZE/2), image=paper , state="normal")

#파일 --> 메모리
func_open()
try :
    loadImage(filename)

except TypeError: 
    messagebox.showinfo("오류",filename+" 처리에 실패하였습니다.")
    photo=PhotoImage(file=filename)
    pLabel=Label(window,image=photo)
    pLabel.image=photo
    pLabel.pack(expand=1)
    window.mainloop()
finally : 
    messagebox.showinfo("종료","수고하셨습니다.")
#메모리 --> 화면
displayImage(inImage)

canvas.pack()

window.mainloop()