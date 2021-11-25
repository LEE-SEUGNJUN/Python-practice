## code 12-2의 upSpeed() 함수를 수정해서 속도가 최대 150이 되도록 조절해 보자. 예를들어 upSpeed(200)을 사용해도 출력은 150km가 되어야한다. 
## 힌트 : if 문을 사용한다

##클래스 선언부분##

class Car :
    color = ""
    speed =0
    """
    def __init__(self,color,speed) :
        self.color=color
        self.speed=speed
        이렇게 작성하여 인스턴스 생성할때 myCar=Car("빨강",200) 이런식으로 할 수도 있다
    """
    def upSpeed(self,value) : ##인스턴스.함수() 로 호출할때엔 self 매개변수가 있어야 오류가안난다.
        self.speed += value
        if self.speed >= 150:
            self.speed = 150
        
## 메인 코드 부분##
myCar1 = Car()
myCar1.color = "빨강" ##Car 클래스에 있는 변수를 . (접근연산자)를통하여 변수를 사용한다. (이하 마찬가지)
myCar1.speed = 0 

myCar2 = Car()
myCar2.color= "파랑"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(30)
print("자동차1의 색상은 %s 이며 현재 속도는 %dkm 입니다." % (myCar1.color,myCar1.speed))

myCar2.upSpeed(1600) ## 매서드에서 if문으로 150이상되면 150으로 속도를 고정 시키게 돼있기때문에 1600을 스피드업해도 150이 출력된다.
print("자동차2의 색상은 %s 이며 현재 속도는 %dkm 입니다." % (myCar2.color,myCar2.speed))

myCar3.upSpeed(0)
print("자동차3의 색상은 %s 이며 현재 속도는 %dkm 입니다." % (myCar3.color,myCar3.speed))
