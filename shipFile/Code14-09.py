from tkinter import *    
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image, ImageFilter, ImageEnhance, ImageOps  # PIL은 이미지 처리 기능을 제공하는 Pillow의 Library.

# 함수 정의 부분
def displayImage(img, width, height) :           # 7~26행 : displayImage(이미지, 폭, 높이) 함수는 넘겨받은 이미지를 폭과 높이대로 화면에 출력
    global window,canvas, paper, photo, photo2, oriX, oriY

    window.geometry(str(width)+"x"+str(height))  # 10행 : 윈도창의 크기를 넘겨받은 이미지의 폭, 높이와 동일하게 설정
    if canvas != None :                          # 11~12행 : 기존 캔버스에 출력한 적이 있다면,  캔버스를 깨끗하게 만듦
        canvas.destroy()

    canvas = Canvas(window, width=width, height=height) # 14~16행 : 캔버스 위에 흰 종이(paper)를 붙인 개념
    paper=PhotoImage(width=width, height=height)
    canvas.create_image( (width/2, height/2), image=paper, state="normal")
    rgbString = ""
    rgbImage = img.convert('RGB')  # 18행 : img.convert('RGB')함수는 이미지 파일의 모든 점에 접근하기 위해 사용
    for i in range(0, height) :    # 19~24행 : 이미지의 폭과 높이만큼 반복해서 픽셀의 RGB 값을 추출하고, rgbString에“#RRGGBB”형식의 문자열로 추가.
        tmpString = ""             # 반복문을 통해서 rgbString에는 모든 픽셀의 색상값이“{#RRGGBB #RRGGBB~총 width 256개의 픽셀,이것이 height한 개의 픽셀~}... {#RRGGBB #RRGGBB~총 width 256개의 픽셀,이것이 총 height 256개의 픽셀}”형식의 문자열로 저장된다.
        for k in range(0, width) :
            r,g,b = rgbImage.getpixel((k, i))
            tmpString += "#%02x%02x%02x " % (r, g, b) # x 뒤에 한칸 공백
        rgbString += "{" + tmpString + "} "           # } 뒤에 한칸 공백
    paper.put(rgbString)           # 25~26행 : rgbString의 문자열을 paper에 한꺼번에 대입시킨 후 화면에 출력
    canvas.pack()

def func_open() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    readFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),  ("모든 파일", "*.*") )) # 30행 : askopenfilename( )은 [열기] 대화상자를 나타낸다. 여기서는 모든 종류의 그림 파일을 선택 가능!

    photo = Image.open(readFp).convert('RGB')  # 32행 : 선택한 파일을 Image.open( )으로 열고 convert('RGB')로 일반적인 컬러 형태로 변형한 후, photo에 저장. 즉 선택한 원본 이미지를 photo에 저장.
    oriX = photo.width          # 33~34행 : 원본 이미지의 크기를 oriX, oriY에 저장. 
    oriY = photo.height

    photo2 =  photo.copy()      # 그런데 아직 이미지를 처리하지 않았으므로 원본 이미지를 36행에서 copy( ) 함수를 사용해 결과 이미지인 photo2에 그대로 복사.
    newX = photo2.width         # 37~38행 : 결과 이미지의 크기를 계산한 후 displayImage(이미지, 폭, 높이) 함수를 호출해서 화면에 출력 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_save() :
    global window,canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None :        # 44~45행 : 결과 이미지 photo2가 없다면, 그냥 빠져나감
        return
    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetypes=(("JPG 파일", "*.jpg;*.jpeg"), ("모든 파일", "*.*"))) # 46행 : 저장파일 입력
    photo2.save(saveFp.name)   # 47행 : save()함수로 변환한 jpg 파일 저장
    
def func_exit() :
    exit()

def func_zoomin() :   # resize((폭, 높이)) 함수 사용
    global window,canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("확대배수", "확대할 배수를 입력하세요", minvalue=2, maxvalue=5)  # 54행 : 확대할 배율 입력
    photo2 = photo.copy()      # 55행  : photo를 photo2로 복사
    photo2 = photo2.resize( (int(oriX * scale) , int(oriY * scale)) )  # 56행 : photo2를 새로운 크기로 변경
    newX = photo2.width        # 57~59행 : 결과 이미지 출력
    newY = photo2.height    
    displayImage(photo2, newX, newY)

def func_zoomout() :  # resize((폭, 높이)) 함수 사용
    global window,canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("축소", "축소할 배수(2, 3, 4)를 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.copy()
    photo2 = photo2.resize((int(oriX / scale), int(oriY / scale)))     # 65행 : 축소(배율로 나눔)
    newX = photo2.width 
    newY = photo2.height    
    displayImage(photo2, newX, newY)

def func_mirror1() :  # transpose(Image.FLIP_TOP_BOTTOM) 함수 이용 
    global window,canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.transpose(Image.FLIP_TOP_BOTTOM)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_mirror2() :  # transpose(Image.FLIP_LEFT_RIGHT) 함수 이용 
    global window,canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.transpose(Image.FLIP_LEFT_RIGHT)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_rotate() :  # rotate(degree, expand=True) 함수 사용. 각도는 0 ~ 360도, expand = True이면 회전결과 이미지 확대, False이면, 원본 크기 유지.
    global window,canvas, paper, photo, photo2, oriX, oriY
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)
    photo2 =  photo.copy()
    photo2 =  photo2.rotate(degree, expand=True)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_bright() : # ImageEnhance.Brightness(이미지).enhance(밝기값) 함수 사용, 밝기값 = 1.0이면 원본 이미지 밝기, 밝기값 > 1.0이면 이미지 밝게 처리.
    global window,canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("밝게", "값을 입력하세요(1.0~10.0)", minvalue=1.0, maxvalue=10.0)
    photo2 = photo.copy()
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)    

def func_dark() :  # ImageEnhance.Brightness(이미지).enhance(밝기값) 함수 사용, 밝기값 = 1.0이면 원본 이미지 밝기, 밝기값 < 1.0이면, 이미지 어둡게 처리.
    global window,canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("어둡게", "값을 입력하세요(0.0~1.0)", minvalue=0.0, maxvalue=1.0)
    photo2 = photo.copy()
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_blur(): # filter(ImageFilter.필터) 함수 사용, 블러링은 BLUR 필터 사용. filter(ImageFilter.BLUR)  
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.filter(ImageFilter.BLUR) 
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_embo():  # filter(ImageFilter.필터) 함수 사용, 엠보싱은 EMBOSS 필터 사용. filter(ImageFilter.EMBOSS),
    global window, canvas, paper, photo, photo2, oriX, oriY  # 그 이외의 ImageFilter 모듈에는 CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    photo2 = photo.copy()                                    #  FIND_EDGES, SHARPEN, SMOOTH, SMOOTH_MORE
    photo2 = photo2.filter(ImageFilter.EMBOSS)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_bw():  # ImageOps.grayscale(이미지) 함수 이용
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = ImageOps.grayscale(photo2)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 변수 선언 부분
window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0

# 메인 코드 부분
window = Tk()
window.geometry("250x250")
window.title("미니 포토샵")

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_command(label="파일 저장", command=func_save)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(1)", menu=image1Menu)
image1Menu.add_command(label="확대", command=func_zoomin)
image1Menu.add_command(label="축소", command=func_zoomout)
image1Menu.add_separator()
image1Menu.add_command(label="상하 반전", command=func_mirror1)
image1Menu.add_command(label="좌우 반전", command=func_mirror2)
image1Menu.add_command(label="회전", command=func_rotate)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(2)", menu=image2Menu)
image2Menu.add_command(label="밝게", command=func_bright)
image2Menu.add_command(label="어둡게", command=func_dark)
image2Menu.add_separator()
image2Menu.add_command(label="블러링", command=func_blur)
image2Menu.add_command(label="엠보싱", command=func_embo)
image2Menu.add_separator()
image2Menu.add_command(label="흑백이미지", command=func_bw)
window.mainloop()
