#버그: 피사체가 사라졌지만 총알은 계속 맞는 버그
#버그: 피사체가 있는 위치에 총을 쏠 경우 총알의 발사속도가 빨라짐
#버그: 발사체의 y축 위치에 따라서 총알의 발사속도가 달라짐
#버그: 발사체가 화면 밖으로 계속 나갈 수 있음.
import pygame  # pygame 라이브러리를 가져와라.
import pygame as pg #pygame 라이브러리를 pg 라는 이름으로 가져와라.
from pygame.locals import *

import Actor

import random
import math
score=0000000

#컬러 값을 미리 설정한다. 컴퓨터에서 컬러를 표현할때 RGB를 사용한다.
BLACK = (0, 0, 0) #검정

#게임창에 텍스트를 출력하기 위한 함수코드
#printText(출력하고싶은 내용, 컬러, 위치)
def printText(msg, color=(255,255,255), pos=(50,50)):
    font= pygame.font.SysFont("consolas",20)
    textSurface=font.render(msg,True,color)
    screen.blit(textSurface,pos)


#===========================================파이게임 코딩을 시작하는 부분..

pygame.init() # 가장 윗줄에 게임에 대한 값들을 초기화


pygame.mixer.music.load("background.mp3") #배경음악을 셋팅
pygame.mixer.music.play(-1)


background = pygame.image.load("background.png")#배경 맵


nX = 800  #게임 창의 X(가로)의 차원 (길이) 
nY = 600  #게임 창의 Y(세로)의 차원 (길이)

size = [nX, nY] #size라는 list 데이터로 가지고 있음

keyFlag = None

#게임 창의 크기를 셋팅한다.
screen = pygame.display.set_mode(size) #pygame 라이브러리 사용
pygame.display.set_caption("Mario") #pygame 라이브러리 사용하여 게임창의 이름을 붙여준다.

start_ticks=pygame.time.get_ticks() #시간 시작 tick을 받아옴

done = False
clock = pygame.time.Clock()

hero = Actor.Actor(pygame) # Actor클래스를 사용하여 객체(주인공) 하나를 생성
hero.setImage("buzz.png")
hero.setScale(100, 100)
hero.setPosition(nX/2, nY/2 + 100)
hero.setVitality(100)
hero.estimateCenter()


bullet = Actor.Actor(pygame)
bullet.setImage("bullet.png")
bullet.setScale(20, 20)
bullet.setPosition(hero.centerX, hero.centerY)
bullet.setSound("laser.wav")
bullet.estimateCenter()


enermy = Actor.Actor(pygame) #actor클래스를 사용하여 객체(적) 하나를 더 생성
enermy.setImage("bacteria1.png")
enermy.setScale(200, 200)
enermy.setPosition(nX/2, nY/2-200) #-200
enermy.setVitality(500)
enermy.estimateCenter()



bulletFire = False #총알이 날아가고 있는가?
bd = 0 #bullet delta 총알이 날아가는 변화량

dx = 0
dy = 0
ds = 0



#반복자 while문
while not done: #done이 False를 유지하는 동안 계속 실행, not False = Ture
    clock.tick(100) #set on 10 frames per second (FPS)

    #게임을 실행하는 기능들을 실제로 여기에 구현
    
    screen.fill(BLACK) # 스크린의 배경색을 채워넣기
    screen.blit(background, (0, 0))

    elapsed_timer=(pygame.time.get_ticks()-start_ticks)/1000#경과시간(ms)을 1000으로 나누어 초 단위로 표시
    elapsed_timer_hour=int(elapsed_timer/60)#초를 분:초로 나타내기 위함
    elapsed_timer_sec=int(elapsed_timer%60)#초를 분:초로 나타내기 위함     
    printText(str(elapsed_timer_hour)+":"+str(elapsed_timer_sec), color=(255,255,255), pos=(10,10))#텍스트 함수

    printText("score:"+str(score),color=(255,255,255),pos=(10,30))#score 표시함수
    for event in pygame.event.get(): #어떤 이벤트가 들어왔을때 그 이벤트를 가져옴

        if event.type == pygame.QUIT: #그 특정 이벤트가 무엇인지 직접 확인하는 절차
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                print("왼쪽키 누름")
                dx = - 10
            elif event.key == pygame.K_RIGHT:
                print("오른쪽키 누름")
                dx = 10
            elif event.key == pygame.K_DOWN:
                print("아래키 누름")
                dy = 10
            elif event.key == pygame.K_UP:
                print("위로키 누름")
                dy = -10
            elif event.key == pygame.K_a:
                print("버튼a 누름")
                ds = 3
            elif event.key == pygame.K_SPACE:
                print("스페이스 버튼 누름")

                if bulletFire == False:
                    bullet.soundPlay()
                    hero.estimateCenter()
                    bullet.setPosition(hero.centerX, hero.centerY) #총을 쏠때, 총알의 위치를 주인공의 위치로 셋팅
                    bd = -20
                    bulletFire = True

                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: 
                print("왼쪽키 떼짐")
                dx = 0
            elif event.key == pygame.K_RIGHT:
                print("오른쪽키 떼짐")
                dx = 0
            elif event.key == pygame.K_DOWN:
                print("아래키 떼짐")
                dy = 0
            elif event.key == pygame.K_UP:
                print("위로키 떼짐")
                dy = 0
            elif event.key == pygame.K_a:
                print("버튼a 누름")
                ds = 0


    if bullet.y < 0:
        bulletFire = False


    if bulletFire == True: #총을 쏘고 있는가? 이게 참이라면.. 총알을 계속 이동시켜야함
        
        bullet.move(0, bd)
        bullet.estimateCenter()
        enermy.estimateCenter()
        bullet.drawActor(screen)

        collsion = bullet.isCollide(enermy)
        if collsion == True:
            print("부딪힘")
            score=score+50
            enermy.decreaseVitality(50)
            bulletFire = False


    hero.move(dx, dy)
    hero.drawActor(screen)
    hero.drawEnergyBar(screen)


    if enermy.isDead == False:
        enermy.drawActor(screen)
        enermy.drawEnergyBar(screen)
        enermy.moveRandomly(nX, nY)
    


    pygame.display.update()


pygame.quit() #게임을 끝내는 명령어

