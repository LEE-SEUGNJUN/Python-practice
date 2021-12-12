from tkinter import *
import math
import random
##버튼으로 도형그리기 (마우스 클릭 이벤트)
## 클래스 선언 부분##
class Shape:   ## 슈퍼클래스 ##
    color, width = '', 0
    shX1, shY1, shX2, shY2 = [0] * 4 ##도형을 포함하는 두점##
    def drawShape(self):             ##추상 메서드##
        raise NotImplementedError()

class Rectangle(Shape): ## 서브클래스 ##
    objects = None  ##사각형 선분 리스트##
    def __init__(self, x1, y1, x2, y2, c, w):
        self.shX1 = x1
        self.shY1 = y1
        self.shX2 = x2
        self.shY2 = y2
        self.color = c
        self.width = w
        self.drawShape()
       
    def __del__(self) : ##사각형의 선분 4개를 삭제##
        for obj  in self.objects :
            canvas.delete(obj)
               
    def drawShape(self) : ## 사각형 그리기로 오버라이딩##
        sx1 = self.shX1; sy1 = self.shY1; sx2 = self.shX2; sy2 =self.shY2
        squreList = []        
        squreList.append(canvas.create_line(sx1, sy1, sx1, sy2, fill = self.color, width = self.width))
        squreList.append(canvas.create_line(sx1, sy2, sx2, sy2, fill = self.color, width = self.width))
        squreList.append(canvas.create_line(sx2, sy2, sx2, sy1, fill = self.color, width = self.width))
        squreList.append(canvas.create_line(sx2, sy1, sx1, sy1, fill = self.color, width = self.width))
        self.objects=squreList ## 선분 리스트(사각형)를 objects에 넣음
       
class Circle(Shape) : ## 서브클래스 ##
    objects = None
    def __init__(self,  x1, y1, x2, y2, c, w):
        self.shX1 = x1
        self.shY1 = y1
        self.shX2 = x2
        self.shY2 = y2
        self.color = c
        self.width = w
        self.drawShape()

    def __del__(self) : ##원은 객체 1개만 삭제
        canvas.delete(self.objects)
 
    def drawShape(self) :       ##원형 그리기로 오버라이딩
        sx1= self.shX1;   sy1= self.shY1;  sx2 = self.shX2;   sy2 = self.shY2
        self.objects = canvas.create_oval(sx1, sy1, sx2, sy2,
                                          outline = self.color,
                                          width = self.width)

def  getColor() : ##임의의 색상 선택 ##
    r = random.randrange(16, 256)
    g = random.randrange(16, 256)
    b = random.randrange(16, 256)
    return "#" + hex(r)[2:] + hex(g)[2:] + hex(b)[2:]

def getWidth() : ##임의의 펜 두께 선택##
    return random.randrange(1, 9) 

##이벤트 함수 선언 부분##
def  startDrawRect(event):
    global x1, y1, x2, y2, rectshape,cirshape
    x1 = event.x
    y1 = event.y

def endDrawRect(event):
    global x1, y1, x2, y2, rectshape,cirshape
    x2 = event.x
    y2 = event.y
    rect = Rectangle(x1, y1, x2, y2, getColor(), getWidth()) ## 사각형 생성
    rectshape.append(rect) ##전체 도형 리스트에 추가 ##

def  startDrawCircle(event):
    global x1, y1, x2, y2, rectshape,cirshape
    x1=event.x
    y1=event.y

def endDrawCircle(event):
    global x1, y1, x2, y2, rectshape,cirshape
    x2=event.x ## x2엔 event시점의 (우클릭을 놓았을때)x 과표를 구함
    y2=event.y ## y2엔 event시점의 y 좌표를 구함
    cir = Circle(x1, y1, x2, y2, getColor(), getWidth()) ##원 생성
    cirshape.append(cir) ## 전체도형 리스트에 추가 ##

def deleteRectShape(event): ##마지막에 그린 사각형 제거 ##
    global rectshape
    if len(rectshape) != 0 : ## 화면에 사각형이 있으면 마지막 사각형 제거
        rectshape2 = rectshape.pop() 
        del(rectshape2)

def deleteCirShape(event): ##마지막에 그린 원 제거 ##
    global cirshape
    if len(cirshape) != 0 :
        cirshape2 = cirshape.pop() ## 마지막 원 제거
        del(cirshape2)

## 전역변수 선언 부분 ##
rectshape,cirshape = [],[] ##사각형 리스트, 원 리스트 
window = None
canvas = None
x1, y1, x2, y2 = None, None, None, None
## 메인 코드 부분 ##
if __name__ == "__main__" :
    window=Tk()
    window.title("객체지향 그림판")
    canvas = Canvas(window, height = 300, width = 300) ## geometry를 정하지않았기 때문에 캔버스 크기대로 윈도창이 나올것임
    ##bind메서드를 이용하여 이벤트가 일어날시 실행할 함수를 구현.
    canvas.bind("<Button-1>", startDrawRect)  ##왼클릭시 startDrawRect함수 시작
    canvas.bind("<ButtonRelease-1>", endDrawRect) ## 왼클릭을 땔씨 endDrawRect함수 시작
    canvas.bind("<Button-3>", startDrawCircle) ##우클릭 startDrawCircle함수 시작
    canvas.bind("<ButtonRelease-3>", endDrawCircle) ##우클릭 땔시 endDrawCircle함수 시작
    canvas.bind("<Double-Button-1>",deleteCirShape) ##왼클릭 더블클릭시 deleteCirShape함수 시작 
    canvas.bind("<Double-Button-3>",deleteRectShape) ## 스크록 더블클릭시 deleteRectShape함수 시작

    canvas.pack() ##캔버스를 pack하여 위치를 잡는다
    window.mainloop()