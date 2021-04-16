import sys
import heapq
import time
import pygame
import random

came_from = dict()
count = 30

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def neighbours(a, graph):
    neighbour = []

    if a[0]-10 >= 0 and graph[a[0]-10][a[1]]!=255:
        neighbour.append((a[0]-10, a[1]))

    if a[1]+10 < len(graph[0]) and graph[a[0]][a[1]+10]!=255: 
        neighbour.append((a[0], a[1]+10))

    if a[0]+10 < len(graph) and graph[a[0]+10][a[1]]!=255: 
        neighbour.append((a[0]+10, a[1]))

    if a[1]-10 >= 0 and graph[a[0]][a[1]-10]!=255: 
        neighbour.append((a[0], a[1]-10))

    return neighbour


# def filterPath(a, graph):
#   global came_from, count
#   roi = []
#   visited = dict()
#   c = 0
#   flag = False

#   roi.append(a)
#   visited[a] = True

#   while len(roi)!=0:
#     current = roi.pop(0)
#     c+=1

#     for x in neighbours(current, graph):
#       try:
#         if x in came_from: flag = False
#         print("in try")
#       except:
#         flag = True
#         print("in catch")

#       if not visited.get(x, False) and flag:
#         roi.append(x)
#         visited[x] = True

#   print(c/(400-count))
#   return c/(400-count) > 0.8


def routing(vertex, goal, mainGraph):

    frontier = []

    dist = dict()
    came_from = dict()
    final = []

    dist[vertex] = 0
    came_from[vertex] = None

    heapq.heappush(frontier, (0, vertex))

    while len(frontier)!=0:

        current = heapq.heappop(frontier)[1]

        if current == goal: break

        for pt in neighbours(current, mainGraph):
            new_cost = dist[current] + 1
            old_cost = dist.get(pt, 10000)

            if pt not in dist or new_cost < old_cost:
                dist[pt] = new_cost
                priority = new_cost + heuristic(pt, goal)
                heapq.heappush(frontier, (priority, pt))
                came_from[pt] = current

    temp = goal
    while temp!=vertex:
        #print(temp, end=' ')
        final.append(temp)
        temp = came_from[temp]

    #print(final, '\n\n\n')
    return final[::-1]



def longRouting(vertex, goal, mainGraph):
    # Length_of_snake = globalVariables.getLength()
    global came_from, count

    frontier = []
    # print('count', count)
    dist = dict()
    
    final = []

    dist[vertex] = 0
    came_from[vertex] = None

    heapq.heappush(frontier, (0, vertex))

    while len(frontier)!=0:

        current = heapq.heappop(frontier)[1]

        if current == goal: break

        # isReachable = filterPath(current, mainGraph)
        # print(current, isReachable)

        for pt in neighbours(current, mainGraph):
            new_cost = dist[current] + 1
            old_cost = dist.get(pt, 10000)

        #isReachable = filterPath(pt, mainGraph)
        #print(isReachable)

            if (pt not in dist or new_cost < old_cost):# and isReachable:
                dist[pt] = new_cost
                priority = -(new_cost + heuristic(pt, goal))
                heapq.heappush(frontier, (priority, pt))
                came_from[pt] = current

    temp = goal
    while temp!=vertex:
        #print(temp, end=' ')
        final.append(temp)
        temp = came_from[temp]

    count+=1
    #print(final, '\n\n\n')
    return final[::-1]



pygame.init()
 
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
 
dis_width = 400
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

# def path_short(x1, y1, foodx, foody):
#     global mainGraph, dis_width, snake_block
#     try: 
#         path_to_follow = routing((x1,y1), (foodx,foody), mainGraph)
#         return path_to_follow

#     except:
#         foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
#         foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
#         path_short(x1, y1, foodx, foody)


# def path_long(x1, y1, foodx, foody):
#     global mainGraph, dis_width, snake_block
#     try: 
#         path_to_follow = longRouting((x1,y1), (foodx,foody), mainGraph)
#         return path_to_follow

#     except:
#         foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
#         foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
#         path_long(x1, y1, foodx, foody)


 
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

        # if Length_of_snake < 30:
        #         path_to_follow = path_short(x1, y1, foodx, foody)

        # else: path_to_follow = path_long(x1, y1, foodx, foody)

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

            #time.sleep(0.0255)
            time.sleep(0.01)

            dis.fill(black)
            # pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            pygame.draw.circle(dis, red, (foodx+5, foody+5), 5, 0)

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