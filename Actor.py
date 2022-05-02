import pygame  # pygame 라이브러리를 가져와라.
import pygame as pg #pygame 라이브러리를 pg 라는 이름으로 가져와라.
from pygame.locals import *
import random
import math
#=================actor 클래스 정의=============================
class Actor():
    def __init__(self, pygame): #actor의 멤버함수 객체가 생성될때 변수들을 초기화 하는 역할
        self.x = 0 #객체의 멤버 변수
        self.y = 0
        self.centerX = 0
        self.centerY = 0
        self.width = 0 #물체의 크기
        self.height = 0
        self.actor = 0
        self.maxVitality = 0
        self.vitality = 0 #에너지
        self.pygame = pygame
        self.sound = 0
        self.isDead = False
    
    def setSound(self, soundPath):
        self.sound = pygame.mixer.Sound(soundPath) #객체에 의존되는 소리
    def soundPlay(self):
        self.sound.play()
    def setPosition(self, x, y): #객체의 위치를 x와 y로 업데이트 시킴
        self.x = x 
        self.y = y
    def move(self, dx, dy): #현재위치에서 이동변화량 만큼만 위치를 변화시킴
        self.x = self.x + dx
        self.y = self.y + dy
        
    def setImage(self, imgPath): #image를 읽어서 객체의 모습을 셋팅할 수 있다.
        self.actor = self.pygame.image.load(imgPath)
    def setScale(self, width, height):
        self.width = width
        self.height = height
        self.actor = self.pygame.transform.scale(self.actor, (self.width, self.height)) #객체의 크기 조절

    def setVitality(self, value):
    def setVitality(self, value):#객체의 생명력 조정및 최대 생명력 설정
        self.vitality = value
        self.maxVitality = value

    def estimateCenter(self):
    def estimateCenter(self):#이부분은 뭔지 잘모르곘음
        self.centerX = self.x + (self.width/2)
        self.centerY = self.y + (self.height/2)

    def decreaseVitality(self, value):
    def decreaseVitality(self, value):#객체의 생명력 감소
        self.vitality -= value
        if self.vitality < 0:
        if self.vitality < 0:#객체의 생명력이 0보다 적은경우 사망관련 부울변수를 True로 바꿈
            self.vitality = 0
            self.isDead = True

    def getVitalStatus(self):
    def getVitalStatus(self):#객체의 생명력비율
        vitalRatio = self.vitality/self.maxVitality
        x = self.x
        y = self.y + self.height + 5
        width = vitalRatio * self.width
        width = vitalRatio * self.width#감소된 생명력 비율만큼 너비 감소
        height = 5
        return x, y, width, height

@@ -88,10 +88,10 @@ def moveRandomly(self, nX, nY):
        self.y = self.y + dY #random.uniform(-20, 20)   


    def isCollide(self, otherActor):
        dist = math.sqrt(math.pow(self.centerX - otherActor.centerX, 2) + math.pow(self.centerY - otherActor.centerY, 2))    
    def isCollide(self, otherActor):#충돌 관련 함수
        dist = math.sqrt(math.pow(self.centerX - otherActor.centerX, 2) + math.pow(self.centerY - otherActor.centerY, 2)) #객체간의 거리를 피타고라스로 보여주는 부분   
        print(dist)
        if dist < otherActor.width/2:
        if dist < otherActor.width/2:#거리가 장애물객체(?)의 너비의 절반, 즉 반경보다 작을경우 충돌했다 판단
            return True
        else:
            return False
