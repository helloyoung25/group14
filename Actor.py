import pygame  # pygame 라이브러리를 가져와라.
from pygame.locals import *

import random
import math


# =================actor 클래스 정의=============================
class Actor():

    def __init__(self, pygame):  # actor의 멤버함수 객체가 생성될때 변수들을 초기화 하는 역할
        self.x = 0  # 객체의 멤버 변수
        self.y = 0

        self.centerX = 0
        self.centerY = 0

        self.width = 0  # 물체의 크기
        self.height = 0

        self.actor = 0
        self.maxVitality = 0
        self.vitality = 0  # 에너지

        self.pygame = pygame

        self.sound = 0

        self.isDead = False

        self.isAlive = True

    def setSound(self, soundPath):
        self.sound = pygame.mixer.Sound(soundPath)  # 객체에 의존되는 소리

    def soundPlay(self):
        self.sound.play()

    def setPosition(self, x, y):  # 객체의 위치를 x와 y로 업데이트 시킴
        self.x = x
        self.y = y

    def move(self, dx, dy):  # 현재위치에서 이동변화량 만큼만 위치를 변화시킴
        self.x = self.x + dx
        self.y = self.y + dy

    def setImage(self, imgPath):  # image를 읽어서 객체의 모습을 셋팅할 수 있다.
        self.actor = self.pygame.image.load(imgPath)

    def setScale(self, width, height):
        self.width = width
        self.height = height
        self.actor = self.pygame.transform.scale(
            self.actor, (self.width, self.height))  # 객체의 크기 조절

    def setVitality(self, value):
        self.vitality = value
        self.maxVitality = value

    def estimateCenter(self):
        self.centerX = self.x + (self.width/2)
        self.centerY = self.y + (self.height/2)

    def decreaseVitality(self, value):
        self.vitality -= value
        if self.vitality < 0:
            self.vitality = 0
            self.isDead = True

    def increaseVitality(self, value):
        self.vitality += value
        if self.vitality > 100:
            self.vitality = 100
            self.isAlive = True

    def getVitalStatus(self):
        vitalRatio = self.vitality/self.maxVitality
        x = self.x
        y = self.y + self.height + 5
        width = vitalRatio * self.width
        height = 5
        return x, y, width, height

    def moveRandomly(self, nX, nY):

        dX = random.uniform(-5, 5)
        dY = random.uniform(-5, 5)
        newX = self.centerX + dX
        newY = self.centerY + dY

        # if newX < nX*0.1  or newX > nX*0.5 or newY < nY*0.1 or newY > nY*0.5:
        #     pass
        # else:
        self.x = self.x + dX  # random.uniform(-20, 20)
        self.y = self.y + dY  # random.uniform(-20, 20)

    def isCollide(self, otherActor):
        dist = math.sqrt(math.pow(self.centerX - otherActor.centerX,
                         2) + math.pow(self.centerY - otherActor.centerY, 2))
        # print(dist)
        if dist < otherActor.width/2:
            return True
        else:
            return False

    def drawActor(self, screen):
        screen.blit(self.actor, (self.x, self.y))

    def drawEnergyBar(self, screen):
        x, y, width, height = self.getVitalStatus()
        self.pygame.draw.rect(screen, (255, 255, 255),
                              (x, y, self.width, height))
        self.pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))

    def damage(self,value):
        damage = value

class Heal(Actor):
    def __init__(self, pygame):
        super().__init__(pygame)
        self.drop_speed = 10
        self.islive = False
        self.interval = 10

    def reset(self, screen: pygame.Surface):
        self.setPosition(random.randint(0, screen.get_width()), 0)
        self.islive = True

    def drop(self):
        self.y += self.drop_speed

class PowerUp(Actor):
    def __init__(self, pygame):
        super().__init__(pygame)
        self.drop_speed = 10
        self.islive = False
        self.interval = 10

    def reset(self, screen: pygame.Surface):
        self.setPosition(random.randint(0, screen.get_width()), 0)
        self.islive = True

    def drop(self):
        self.y += self.drop_speed
