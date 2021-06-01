import sys
import heapq
import time

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