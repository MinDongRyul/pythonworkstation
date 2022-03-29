import pygame
from pygame.constants import KEYDOWN

######################################
# 기본 초기화 ()
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로
screen_height = 480 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang game") #게임 이름

# FPS 설정
clock = pygame.time.Clock()

###################################### 

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 불러오기
background = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/pang_background.jpg")

# 스테이지 불러오기
stage = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/pang_stage.jpg")
stage_size = stage.get_rect().size # 이미지의 크기 불러오기
stage_width = stage_size[0] # 가로
stage_height = stage_size[1] # 세로
stage_x_pos = 0
stage_y_pos = screen_height - stage_height

# 캐릭터 불러오기  
character = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/pang_character.png")
character_size = character.get_rect().size # 이미지의 크기 불러오기
character_width = character_size[0] # 가로
character_height = character_size[1] # 세로
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - stage_height - character_height

character_1 = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/pang_character.png")
character_1_size = character_1.get_rect().size # 이미지의 크기 불러오기
character_1_width = character_1_size[0] # 가로
character_1_height = character_1_size[1] # 세로

# 좌
character_left = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/pang_character_left.png")
character_left_size = character_left.get_rect().size # 이미지의 크기 불러오기
character_left_width = character_left_size[0] # 가로
character_left_height = character_left_size[1] # 세로

# 우
character_right = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/pang_character_right.png")
character_right_size = character_right.get_rect().size # 이미지의 크기 불러오기
character_right_width = character_right_size[0] # 가로
character_right_height = character_right_size[1] # 세로


ballon1 = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/pang_ballon1.jpg")
ballon1_size = ballon1.get_rect().size #사이즈 불러오기
ballon1_width = ballon1_size[0]
ballon1_height = ballon1_size[1]
ballon1_x_pos = (screen_width / 2) - (ballon1_width / 2) # 중앙 시작
ballon1_y_pos = 0  # 시작과 동시에 움직임
ballon1_speed = 10 

# 풍선 2~4 (분해 되는공)
ballon2 = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/pang_ballon2.jpg")
ballon2_size = ballon2.get_rect().size
ballon2_width = ballon2_size[0]
ballon2_height = ballon2_size[1]
ballon2_x_pos = ballon1_x_pos
ballon2_y_pos = ballon1_y_pos

ballon3 = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/pang_ballon3.jpg")
ballon3_size = ballon3.get_rect().size
ballon3_width = ballon3_size[0]
ballon3_height = ballon3_size[1]
ballon3_x_pos = ballon2_x_pos
ballon3_y_pos = ballon2_y_pos

ballon4 = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/pang_ballon4.jpg")
ballon4_size = ballon4.get_rect().size
ballon4_width = ballon4_size[0]
ballon4_height = ballon4_size[1]
ballon4_x_pos = ballon3_x_pos
ballon4_y_pos = ballon3_y_pos

# 무기 정보 
weapon = pygame.image.load("C:/Users/82102/Desktop/pythonworkstation/pygame_basic/pang_weapon.jpg")
weapon_size = weapon.get_rect().size #사이즈 불러오기
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_x_pos = (screen_width / 2) - (character_width / 2)
weapon_y_pos = screen_height - stage_height - character_height

game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

total_time = 99
start_ticks = pygame.time.get_ticks() # 현재 tick 를 받아옴

weapon_attack = 100  # 무기가 위로 올라감
weapon_x = 0
to_x = 0 # 캐릭터의 움직일 정도
character_speed = 1.3

# 이벤트 루프
running = True
while running:
    dt = clock.tick(30) # 보통 30 혹은 60
    # 2. 이벤트 처리 (키보드, 마우스등)
    for event in pygame.event.get():
        dt = clock.tick(30)
        if event.type == pygame.QUIT:
            running = False  

        if event.type == pygame.KEYDOWN: # 방향키를 누르면 움직임 (좌 우)
            if event.key == pygame.K_LEFT:
                character = character_left
                to_x -= character_speed
                weapon_x -= character_speed 

            elif event.key == pygame.K_RIGHT:
                character = character_right
                to_x += character_speed
                weapon_x += character_speed

            elif event.key == pygame.K_SPACE:
                character = character_1
                weapon_y_pos -= weapon_attack
                if weapon_y_pos < 0:
                    weapon_y_pos = screen_height - stage_height - character_height


        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0  
                weapon_x = 0   
    
    # 공을 좌우로 움직이게끔 해주는 작엄
    if 0 <= ballon1_y_pos <= 640:
        ballon1_y_pos += 0.5
        ballon1_x_pos -= 0.5
        #if ballon1_y_pos == (screen_height - stage_height):
        #    ballon1_y_pos -= 5 
        #    ballon1_x_pos += 5 
        #elif ballon1_x_pos == 0:
        #    ballon1_y_pos -= 5 
        #    ballon1_x_pos += 5 
        

    # 3. 게임 캐릭터 위치 정의 (경계 값 처리)        
    character_x_pos += to_x * dt
    weapon_x_pos += weapon_x * dt    
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if weapon_x_pos < 0:
       weapon_x_pos = 0
    elif weapon_x_pos > screen_width - weapon_width:
        weapon_x_pos = screen_width - weapon_width
    

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ballon1_rect = ballon1.get_rect()
    ballon1_rect.left = ballon1_x_pos
    ballon1_rect.top = ballon1_y_pos

    ballon2_rect = ballon2.get_rect()
    ballon2_rect.left = ballon1_x_pos 
    ballon2_rect.top = ballon1_y_pos 

    ballon3_rect = ballon3.get_rect()
    ballon3_rect.left = ballon2_x_pos 
    ballon3_rect.top = ballon2_y_pos 

    ballon4_rect = ballon4.get_rect()
    ballon4_rect.left = ballon3_x_pos 
    ballon4_rect.top = ballon3_y_pos 

    weapon_rect = weapon.get_rect()
    weapon_rect.left = weapon_x_pos
    weapon_rect.top = weapon_y_pos

    
    # 충돌 체크 
    # 공이 무기랑 충돌하면 2개로 나눠짐
    if character_rect.colliderect(ballon1_rect): # 충돌 했는지
        print("풍선과 충돌 했어요")
        running = False

    if weapon_rect.colliderect(ballon1_rect): 
        ballon1 = ballon2 
        weapon_y_pos = screen_height - stage_height - character_height

    if weapon_rect.colliderect(ballon2_rect):
        ballon2 = ballon3 
        weapon_y_pos = screen_height - stage_height - character_height

    if weapon_rect.colliderect(ballon3_rect):
        ballon3 = ballon4
        weapon_y_pos = screen_height - stage_height - character_height

    if weapon_rect.colliderect(ballon4_rect):
        print("풍선 파괴 스테이지 클리어")
        running = False 
        
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, stage_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    # ballon1 ~ ballon4 까지의 공 작업
    screen.blit(ballon1, (ballon1_x_pos, ballon1_y_pos))
  
    pygame.display.update()  # 화면 업데이트(필수) 

# pygame 종료
pygame.quit()