import pygame
import time
import random
from RoutingAlgo import routing, longRouting

pygame.init()
 
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
 
dis_width = 200
dis_height = 200
 
dis = pygame.display.set_mode((dis_width, dis_height))
mainGraph = pygame.surfarray.pixels_green(dis)

pygame.display.set_caption('Perfect Snake')

clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 50

# def drawStyleRect(surface):
#     pygame.draw.rect(dis, (0,0,255), (x,y,150,150), 0)
#     for i in range(4):
#         pygame.draw.rect(dis, (0,0,0), (x-i,y-i,155,155), 1)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
        pygame.draw.rect(dis, (255,255,255), (x[0]-1,x[1]-1,snake_block,snake_block), 1)

 
def gameLoop():
    Length_of_snake = 1

    direction = 'center'
    game_over = False
    game_close = False
 
    x1 = int(dis_width / 2)
    y1 = int(dis_height / 2)
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
 
    foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
    foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
 
    while not game_over:
 
        while game_close == True:

            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        #print(foodx, foody)
        mainGraph = pygame.surfarray.pixels_green(dis)

        if Length_of_snake < 30:
            path_to_follow = routing((x1,y1), (foodx,foody), mainGraph)

        else: path_to_follow = longRouting((x1,y1), (foodx,foody), mainGraph)

        # print('length', Length_of_snake)
        # for co_ordinates in path_to_follow:
        #     pygame.draw.rect(dis, (255,255,255), [co_ordinates[0], co_ordinates[1], 10, 10])
        #     pygame.display.update()
        
        for co_ordinates in path_to_follow:
        
            if x1 > co_ordinates[0] and direction!='right':
                x1_change = -snake_block
                y1_change = 0
                direction = 'left'

            elif x1 < co_ordinates[0] and direction!='left':
                x1_change = snake_block
                y1_change = 0
                direction = 'right'

            elif y1 > co_ordinates[1] and direction!='down':
                y1_change = -snake_block
                x1_change = 0
                direction = 'up'

            elif y1 < co_ordinates[1] and direction!='up':
                y1_change = snake_block
                x1_change = 0
                direction = 'down'
 
            if x1 > dis_width or x1 < 0 or y1 > dis_height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change

            time.sleep(0.0255)

            dis.fill(black)
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)

            if len(snake_List) > Length_of_snake:
                del snake_List[0]
    
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
    
            our_snake(snake_block, snake_List)

            pygame.display.update()
 
        # print(snake_List)
        flag = True

        if x1 == foodx and y1 == foody:
            while flag:
                foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)

                if [foodx,foody] not in snake_List: flag = False
                
            Length_of_snake += 1

        # print('head=', x1, y1)
        # print('food=', foodx, foody)

        # print('\n\n')
        clock.tick(snake_speed)
 
    
    pygame.quit()
    quit()
 
gameLoop()