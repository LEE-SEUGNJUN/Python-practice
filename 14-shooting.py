from os import strerror
from typing import AsyncContextManager, AsyncIterable
import pygame
import random
import sys
import time

## 함수 선언 부분 ##
# @ 기능 2-5 : 매개변수로 받은 객체를 화면에 그리는 함수를 선언
def paintEntity(entity , x, y):
    monitor.blit(entity, (int(x), int(y) ))

# @ 기능 5-4 : 점수를 화면에 쓰는 함수를 선언
def writeScore(score):
    myfont = pygame.font.Font('shipFile/NanumGothic.ttf', 20) #한글 폰트
    txt = myfont.render("파괴한 우주괴물 수 : " +str(score),True,(255-r,255-g,255-b))
    monitor.blit(txt,(10,sheight-40))
    
def writeBoomMessage(str1): ##우주선이 우주괴물에 닿으면 메시지를 띄우고 게임 종료하는 함수
    global monitor,ship,monster,missile,fireCount,shipimage
    myfont = pygame.font.Font('shipFile/NanumGothic.ttf', 30) #한글 폰트
    txt = myfont.render(str1,True,(255-r,255-g,255-b))
    monitor.blit(txt,(swidth*0.2, sheight/2-10))
    
def boom() : ## 게임을 멈추고 종료시키는 함수
    time.sleep(5)
    pygame.quit()
    sys.exit()
    
    
    

def playGame() :  # 게임을 작동하는 본체함수
    global monitor,ship,monster,missile,fireCount,shipimage
    r=random.randrange(0,256) # 무작위로 색상 선택
    g=random.randrange(0,256)
    b=random.randrange(0,256)
    
    # @ 기능 2-2- : 우주선의 초기 위치 키보드를 눌렀을때 이동량을 저장할 변수 선언
    shipX=swidth/2
    shipY=sheight * 0.8
    dx,dy= 0,0 ## 키보드를 눌렀을때 우주선의 이동량 변수선언
    # @ 기능 3-2 : 우주괴물을 무작위로 추출하고 크기와 위치 설정
    monster = pygame.image.load(random.choice(monsterimage))
    monsterSize = monster.get_rect().size # monsterSize[0]=x값 ,[1]은 y값
    monsterX = random.randrange(0,int(swidth)) ## 위에(y=0) 에서 어디서 나올껀지 x폭 랜덤값 초기화
    monsterY = 0 ## 몬스터가 위에서 부터 올거기때문에 0으로 초기화
    monsterSpeed=random.randrange(5,9) ##  난이도 UP 
    # @ 기능 4-2 : 미사일 좌표를 초기화한다.
    missileX,missileY=None,None ## None은 미사일을 쏘지 않았다는 의미이다

    # @ 기능 5-1 : 맞힌 우주괴물 숫자를 저장할 변수 선언

    # 무한 반복 #

    while True : # 무한 반복 / 나중에 우주선 움직임과 미사일 발사되는 듯한 효과 볼수 있음
        (pygame.time.Clock()).tick(50) # 게임 진행을 늦춰줌 (10~ 100정도가 적당)
        monitor.fill((r,g,b))  ## 화면 배경을 칠함 
        
        # 키보드나 마우스가 이벤트가 들어오는지 확인한다.
        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
            
            # @ 기능 2-3 : 방향키에 따라 우주선이 움직이게 한다.
            
            if e.type in [pygame.KEYDOWN] :
                if e.key == pygame.K_LEFT : dx = -5
                elif e.key == pygame.K_RIGHT : dx = +5
                elif e.key == pygame.K_UP : dy = -5
                elif e.key == pygame.K_DOWN : dy = +5
                # @ 기능 4-3 : 스페이스바를 누르면 미사일을 발사한다.
                elif e.key == pygame.K_SPACE : 
                    if missileX==None : # 미사일을 쏜적이 없다면 , 즉 if missileX에 값이 있다면,현재 미사일이 날아가고 있는 상태이므로 무시함.
                        missileX=shipX + (shipSize[0]/2)
                        missileY=shipY
            
            # 방향키를 때면 우주선이 멈춘다.
            if e.type in [pygame.KEYUP] :
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT \
                    or e.key ==pygame.K_UP or e.key == pygame.K_DOWN : dx,dy = 0,0
                    

        # @ 기능 2-4 : 우주선이 화면 안에서만 움직이게 한다.
        if (0<shipX + dx and shipX +dx <=swidth-shipSize[0])\
            and (sheight/2 < shipY +dy and shipY +dy <= sheight-shipSize[1]) : # 화면의 중앙까지만
            shipX += dx
            shipY += dy
        paintEntity(ship , shipX, shipY) # 우주선을 화면에 표시 <== 함수 호출

        # @ 기능 3-3 : 우주괴물이 자동으로 나타나 왼쪽에서 오른쪽으로 움직인다.
        monsterY += monsterSpeed # X값 고정 Y값만 증가
        monsterX += random.randrange(-monsterSpeed,+monsterSpeed) ##몬스터가 좌우로 움직이면서 내려옴
        if monsterX <= 0 :  ##만약 몬스터의 X좌표가(왼쪽면) 화면 스크린을 넘어가거나 같게되면
            monsterX += monsterSpeed + 2  ## 오른쪽으로 가게끔함 (왼쪽벽을 못넘어가게끔함)
        if monsterX + monsterSize[0] > swidth : ## 몬스터의 오른쪽면(왼쪽면 좌표 + 몬스터의 가로폭 크기)이 오른벽(sheight)을 넘어가면
            monsterX -= monsterSpeed - 2 ## 왼쪽으로 가게끔함 (오른쪽 벽 못넘어가게끔함)
        if monsterY > sheight : ##Y값이 화면 세로폭보다 크면, 화면 밖으로 이동된 것이므로 다시 초기화하여 우주괴물 생성
            fireCount -=1 ## 미사일이 빗나가는것 뿐만 아니라 몬스터를 못맞추고 밑으로 쭉 내려가게 냅두면 점수 -1
            monsterY = 0
            monsterX = random.randrange(0,int(swidth))
        #우주괴물 이미지를 랜덤하게 선택한다.
            monster = pygame.image.load(random.choice(monsterimage))
            monsterSize=monster.get_rect().size
            monsterSpeed=random.randrange(5,9)
        paintEntity(monster,monsterX,monsterY)

        ##우주괴물과 미사일이 닿으면 메시지를 띄우는 함수를 호출한다.
        if  (monsterY + monsterSize[1]> shipY and monsterY < shipY+shipSize[1] ) and \
            (monsterX + monsterSize[0] > shipX and monsterX < shipX + shipSize[0]):
            str1="우주선 폭파"
            writeBoomMessage(str1)
        ##우주괴물이 미사일과 아주 조금 더 마주쳤을때 노래를 틀고 ,게임을 멈추고 종료하는 함수를 호출한다.
        if  (monsterY + monsterSize[1] -10> shipY and monsterY < shipY+shipSize[1]-10 ) and \
            (monsterX + monsterSize[0] -10> shipX and monsterX < shipX + shipSize[0]-10):
            pygame.mixer.music.load('shipFile/gameover.wav')
            pygame.mixer.music.play(-1) ## -1 은 무한반복을 뜻한다.
            boom()
            
            
            
            
        # @ 기능 4-4 : 미사일을 화면에 표시한다
        if missileX != None : # 미사일을 쐇다면
            missileY -= 10 # 반복문 돌때마다 미사일의 y좌표를 -10씩 이동 (위로 발사 되는것처럼보이게)
            if missileY < 0 : ## 만약 미사일이 맨위에 도착하면
                fireCount -= 1
                missileX,missileY=None,None ##미사일 없어짐
            
        if missileX != None :
            paintEntity(missile,missileX,missileY) ## 화면에 미사일을 띄어줌
            # @ 기능 5-2 : 우주괴물이 미사일에 맞았는지 체크한다.
            if (monsterX < missileX and missileX < monsterX + monsterSize[0]) and \
                (monsterY < missileY and missileY < monsterY + monsterSize[1]) :
                pygame.mixer.music.load('shipFile/hit.wav')
                pygame.mixer.music.play()
                
                fireCount += 1
                #우주 괴물을 초기화 (무작위 이미지로 다시준비)
                monster = pygame.image.load(random.choice(monsterimage))
                monsterSize=monster.get_rect().size
                monsterX=random.randrange(0,swidth)
                monsterY=0
                monsterSpeed=random.randrange(5,9)
                #미사일 초기화
                missileX,missileY=None,None #총알 사라진다
                #우주선 초기화
                newshipX=shipX; newshipY=shipY
                num=random.randrange(0,3)
                ship = pygame.image.load(random.choice(shipimage))
                shipX=newshipX; shipY=shipY
                

                
        
        # @ 기능 5-3 : 점수를 화면에 쓰는 함수를 호출한다
        writeScore(fireCount)
        # 화면을 업데이트한다
        pygame.display.update()
        print("~",end="")

        


##전역변수 선언 부분##
r,g,b=0,0,0 ## 화면 색깔 
swidth,sheight=500,700 ## 화면크기
monitor=None ## 게임화면
ship ,shipSize=None,0 #우주선의 객체와 크기 변수 선언 <== 우주선 객체 준비
fireCount=0 # 점수


# @ 기능 3-1 : 무작위로 사용할 우주괴물의 이미지 10개를 준비한다.
monsterimage=['shipFile/monster01.png','shipFile/monster02.png','shipFile/monster03.png','shipFile/monster04.png',\
            'shipFile/monster05.png','shipFile/monster06.png','shipFile/monster07.png','shipFile/monster08.png',\
            'shipFile/monster09.png','shipFile/monster10.png']
shipimage=['shipFile/ship01.png','shipFile/ship02.png','shipFile/ship03.png','shipFile/ship04.png']
monster=None

missile = None
##메인 코드 부분##
pygame.mixer.init() ##pygame.mixer를 사용하겠단 의미
pygame.init() ##pygame 초기화하고 앞으로 사용하겠다는 의미 / 처음에 실행 되어야함
monitor=pygame.display.set_mode((swidth,sheight)) ##화면 크기 지정해서 monitor에 대입
pygame.display.set_caption("우주괴물 무찌르기") ## 화면 캡션을 적음

##  @기능 2-1 : 우주선 이미지를 준비하고 크기를 구한다.
ship=pygame.image.load('shipFile/ship01.png')
shipSize=ship.get_rect().size
## @ 기능 4-1 : 미사일 이미지를 추가한다.
missile=pygame.image.load("shipFile/missile.png")

playGame() # 게임 무한 반복