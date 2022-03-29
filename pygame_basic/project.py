import pygame
from typing import ParamSpec
from random import *

# random 초기화

pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz") #게임 이름

# FPS 설정
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/ddong_background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/ddong_character.png")
character_size = character.get_rect().size # 이미지의 크기 불러오기
character_width = character_size[0] # 가로
character_height = character_size[1] # 세로
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0 # 움직일 정도

character_speed = 0.6

# 똥 이미지 불러오기
enemy = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/ddong_enemy.png")
enemy_size = enemy.get_rect().size #사이즈 불러오기
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width - enemy_width) #랜덤으로 위치 정하기
enemy_y_pos = 0 # 계속 마이너스로 끝까지 떨어지기
#enemy_speed = 10 스피드로 정의해줌

# 이벤트 루프
running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # 방향키를 누르면 움직임 (좌 우)
            if event.key == pygame.K_LEFT:

                to_x -= character_speed
            elif  event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt # 위치 정의
  
    # 똥의 위치 정의
    if 0 <= enemy_y_pos <= 640:
        enemy_y_pos += 10
        if enemy_y_pos == 640:
            enemy_y_pos = 0
            enemy_x_pos = randint(0, 410)
    
    #if enemy_y_pos > screen_height:
    #    enemy_y_pos = 0 
    #    enemy_x_pos = random.randint(0, screen_width - enemy_width)
    
    #enemy_y_pos += enemy_speed

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 충돌 처리 정의
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect): # 충돌 했는지
        print("충돌했어요")
        running = False


    #5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 
  
    pygame.display.update()  # 화면 업데이트 

# 잠시 대기
pygame.time.delay(1000)


# pygame 종료
pygame.quit()