from tkinter import *
## 변수 ##
window = None
canvas = None
XSIZE, YSIZE = 256, 256

#함수 선언 부분#
def loadImage(fname):
    global XSIZE,YSIZE
    #이부분에서 읽어올 파일 경로
    fp=open(fname,"rb")       ## fp? =파일포지션
    
    for i in range(0, XSIZE) :
        for k in range(0,YSIZE)  :
            data = int(ord(fp.read(1)))
            paper.put("#%02x%02x%02x " % (data,data,data) , (k, i))
 
    fp.close()

## 메인코드 ##
filename="C:/SeungjunPython/RAW/tree.raw"
window=Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height=XSIZE, width=YSIZE)
 
paper=PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE/2,YSIZE/2), image=paper,state="normal")
 
loadImage(filename)
canvas.pack()
window.mainloop()