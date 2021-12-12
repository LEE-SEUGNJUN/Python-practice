from os import read
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from typing import OrderedDict
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

## 함수 선언 부분 ##
def displayImage(img,width,height):
    global window,canvas,paper,photo,photo2,oriX,oriY

    window.geometry(str(width)+"x"+str(height))
    if canvas != None :
        canvas.destroy()
    
    canvas = Canvas(window, width=width, height=height)
    paper=PhotoImage(width=width,
    height=height)
    canvas.create_image(width/2,height/2, image=paper, state="normal")
    rgbString=""
    rgbImage=img.convert('RGB') ##img.convert 함수는모든 점에 접근하기 위해 사용 
    for i in range(0,height): # 이미지의 폭과 높이만큼 반복해서 픽셀의 RGB값을 추출하고 rgbstring에 "#RRGGBB" 형식의 문자열로 추가
        tmpString=""          # 반복문을 통해서 rgbString에는 모든 픽셀의 색상값이 "{#RRGGBB #RRGGBB~~..} 대괄호 하나에 height1, width의 픽셀 전부가 들어감"
        for k in range(0,width): 
            r,g,b = rgbImage.getpixel((k,i))
            tmpString += "#%02x%02x%02x " % (r,g,b) # x 뒤 한칸 공백     
        rgbString+="{" + tmpString + "} "           # } 뒤 한칸 공백
    paper.put(rgbString)   ##25~26행 : rgbString의 문자열을 paper에 한꺼번에 대입시킨 후 화면에 출력
    canvas.pack()
    
def func_open():
    global window,canvas,paper,photo,photo2,oriX,oriY
    readFp=askopenfilename(parent=window, filetypes=(("모든 그림 파일","*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),("모든파일","*.*") ))
    
    photo=Image.open(readFp).convert('RGB') ## 32행 : 선택한 파일을 Image.open()으로 열고 convert('RGB')로 일반적인 컬러 형태로 변형한 후, photo에 저장 , 즉 원본 
    oriX=photo.width
    oriY=photo.height
    
    photo2=photo.copy() ##원본이미지 그대로 복사
    newX=photo2.width ##복사한 파일의 x좌표
    newY=photo2.height ##복사한 파일의 y좌표
    displayImage(photo2,newX,newY) ##photo2와 x,y좌표를 디스플레이함수에 호출

def func_save():
    global window,canvas,paper,photo,photo2,oriX,oriY
    if photo2 == None :
        return
    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetypes=(("JPG 파일","*.jpg;*.jpeg"),("모든 파일","*.*"))) # 저장파일 입력
    photo2.save(saveFp.name)

def func_exit():
    exit()

def func_zoomin(): # resize((폭,높이)) 함수 사용
    global window,canvas,paper,photo,photo2,oriX,oriY
    scale=askinteger("확대배수","확대할 배수를 입력하세요", minvalue=2, maxvalue=5)
    photo2 = photo.copy()
    photo2 = photo2.resize( (int(oriX * scale), int(oriY*scale)) ) ##56행 : photo2를 새로운 크기로 변경
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_zoomout(): # resize((폭,높이)) 함수 사용
    global window,canvas,paper,photo,photo2,oriX,oriY
    scale=askinteger("축소", "축소할 배수(2,3,4)를 입력하세요 ", minvalue=2,maxvalue=5)
    photo = photo.copy()
    photo2 = photo2.resize( (int(oriX / scale), int(oriY/scale)) ) ## 축소할 배율
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_mirror1():
    global window,canvas,paper,photo,photo2,oriX,oriY
    photo2=photo.copy()
    photo2=photo.transpose(Image.FLIP_TOP_BOTTOM)
    newX=photo2.width
    newY=photo2.height
    
    displayImage(photo2,newX,newY)

def func_mirror2():
    global window,canvas,paper,photo,photo2,oriX,oriY
    photo2=photo.copy()
    photo2=photo.transpose(Image.FLIP_LEFT_RIGHT)
    newX=photo2.width
    newY=photo2.height
    
    displayImage(photo2,newX,newY)
 
def func_rotate():  ##회전 시키기 위한 함수
    global window,canvas,paper,photo,photo2,oriX,oriY
    dgree=askinteger("회전", "회전할 각도를 입력하세요",minvalue=0,maxvalue=360)
    photo2=photo.copy()
    photo2.rotate(dgree,expand=True)
    newX=photo2.width
    newY=photo2.height

    displayImage(photo2,newX,newY)

def func_bright(): ## imageEnhance.Brightness(이미지).enhance(밝기값) 함수사용 밝기값=1.0이면 원본이미지밝기, 밝기값 >1.0이면 밝게처리
    global window,canvas,paper,photo,photo2,oriX,oriY
    value=askfloat("밝게", "밝게할 값을 입력하세요 (1.0~10.0)",minvalue=1.0,maxvalue=10.0)
    photo2.copy()
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)
    

def func_dark(): ##imageEnhance.Brightness(이미지),enhance(밝기값) 함수사용 밝기값=1.0이면 원본이미지밝기, 밝기값 <1.0이면 어둡게처리
    global window,canvas,paper,photo,photo2,oriX,oriY
    value=askfloat("어둡게", "어둡게할 값을 입력하세요 (0.0~1.0)",minvalue=0.0,maxvalue=1.0)
    photo2.copy()
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_blur():  #filter(ImageFilter.필터) 함수 사용 블러링은 BLUR, 엠보는 EMBOSS 필터사용
    global window,canvas,paper,photo,photo2,oriX,oriY 
    photo2 = photo.copy()
    photo2 = photo2.filter(ImageFilter.BLUR)
    newX = photo2.width
    newY = photo2.height
    
    displayImage(photo2,newX,newY)

def func_embo(): ##엠보 : 윤곽이 보이게끔 해주는 필터 , ##블러 : 흐릿하게 해주는 필터
    global window,canvas,paper,photo,photo2,oriX,oriY
    photo2 = photo.copy()
    photo2 = photo2.filter(ImageFilter.EMBOSS)
    newX=photo2.width
    newY=photo2.height

    displayImage(photo2,newX,newY)

def func_bw(): ## ImageOps.grayscale(이미지) 함수 사용
    global window,canvas,paper,photo,photo2,oriX,oriY
    photo2=photo.copy()
    photo2=ImageOps.grayscale(photo2)
    newX=photo2.width 
    newY=photo2.height

    displayImage(photo2,newX,newY)

## 전역 변수 선언 부분##

window,canvas,paper=None,None,None
photo,photo2=None,None
oriX,oriY=0,0

## 메인 코드 부분 ##
window=Tk()
window.geometry("250x250")
window.title("미니 포토샵")

mainMenu=Menu(window)
window.config(menu=mainMenu)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_command(label="파일 저장", command=func_save)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

image1Menu=Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(1)",menu=image1Menu)
image1Menu.add_command(label="확대", command=func_zoomin)
image1Menu.add_command(label="축소", command=func_zoomout)
image1Menu.add_separator()
image1Menu.add_command(label="상하 반전", command=func_mirror1)
image1Menu.add_command(label="좌우 반전", command=func_mirror2)
image1Menu.add_command(label="회전", command=func_rotate)

image2Menu=Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(2)",menu=image2Menu)
image2Menu.add_command(label="밝게", command=func_bright)
image2Menu.add_command(label="어둡게", command=func_dark)
image2Menu.add_separator()
image2Menu.add_command(label="블러링", command=func_blur)
image2Menu.add_command(label="엠보싱", command=func_embo)
image2Menu.add_separator()
image2Menu.add_command(label="흑백이미지", command=func_bw)
window.mainloop()

