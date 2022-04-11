import cv2
import random as rd
import queue
import math
import quadtree
from drawer import draw

def isNeedToDivide(rect):
    white = 0
    black = 0
    for i in range(40):
        x = rd.randint(rect.left, rect.left+rect.width)
        y = rd.randint(rect.top, rect.top+rect.height)
        if image[x][y][0] == 0 and image[x][y][1] == 0 and image[x][y][2] == 0:
            black += 1
        elif image[x][y][0] == 255 and image[x][y][1] == 255 and image[x][y][2] == 255:
            white += 1
    if white == 0 or black == 0:
        r = quadtree.Node(rect)
        tree.add(tree.root, r)
        return False
    else:
        #draw(rect)
        return True

def divide(rect):
    r1 = quadtree.Rectangle(rect.left, rect.top, math.floor(rect.width/2), math.floor(rect.height/2))
    que.put(r1)
    draw(r1, image)
    r2 = quadtree.Rectangle(rect.left+math.floor((rect.width/2)), rect.top, math.floor(rect.width/2), math.floor(rect.height/2))
    que.put(r2)
    draw(r2, image)
    r3 = quadtree.Rectangle(rect.left,  rect.top+math.floor(rect.height/2), math.floor(rect.width/2), math.floor(rect.height/2))
    que.put(r3)
    draw(r3, image)
    r4 = quadtree.Rectangle(rect.left+math.floor((rect.width/2)), rect.top+math.floor(rect.height/2), math.floor(rect.width/2), math.floor(rect.height/2))
    que.put(r4)
    draw(r4, image)

que = queue.Queue()
image = cv2.imread('bg.png')
tree = quadtree.Tree()
base = quadtree.Rectangle(0, 0, 499, 699)
que.put(base)
while que.qsize() != 0:
    rectangle = que.get()
    if rectangle.width >= 1 and rectangle.height >= 1:
        if isNeedToDivide(rectangle):
            divide(rectangle)

cv2.imshow('image', image)

tree.BFS()
cv2.waitKey(0)
#cv2.destroyAllWindows()