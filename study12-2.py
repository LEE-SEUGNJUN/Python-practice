##code 12-7에 Sonata 클래스를 추가해 보자. 
##단, Sonata 클래스는 Car -> Sedan -> Sonata 순서로 상속을 받도록 하자. Sonata 클래스에는 특별히 추가하는 필드나 메서드가 없다

##클래스 선언 부분##

class Car : ## 슈퍼클래스 (최상위 클래스 생성)
    speed=0
    def upSpeed(self , value):
        self.speed += value
        
        print("현재 속도(슈퍼클래스) : %d " % self.speed)

class Sedan(Car) : ##Car클래스를 상속 받아서 클래스 생성
    def upSpeed(self, value):
        self.speed +=value
        if self.speed > 150 :
            self.speed=150
        print("현재 속도(서브클래스) : %d " % self.speed)
class Truck(Car): ##Car 클래스를 상속받아서 클래스 생성
    pass

class Sonata(Sedan) : ##Car클래스를 상속받은 Sedan클래스를 상속받음.
                      ##Car클래스의 필드,메서드를 다 사용가능하지만 Sedan에서 변경이 있을시엔 바로위의 부모클래스인 Sedan의 메서드,필드를 따른다.
    pass
##변수 선언 부분##
sedan1,truck1=None,None 

##메인 코드 부분##
truck1=Truck()
sedan1=Sedan()
sonata1=Sonata()

print("트럭 --> ",end="")
truck1.upSpeed(200)

print("승용자 --> ",end="")
sedan1.upSpeed(200)

print("소나타 --> ",end="")
sonata1.upSpeed(200)
