import queue
from drawer import draw
import cv2

class Rectangle:
    def __init__(self, l, t, width, height):
        self.left = l
        self.top = t
        self.width = width
        self.height = height

class Node:
    def __init__(self, rect):
        self.LT = None
        self.RT = None
        self.LB = None
        self.RB = None
        self.rect = Rectangle(rect.left, rect.top, rect.width, rect.height)

class Tree:
    def __init__(self):
        self.root = None

    def add(self, root, toadd):
        if self.root is None:
            self.root = toadd
        else:
            if toadd.rect.left == root.rect.left and toadd.rect.top == root.rect.top:
                if root.LT is None:
                    root.LT = toadd
                else:
                    self.add(root.LT, toadd)
            elif toadd.rect.left != root.rect.left and toadd.rect.top == root.rect.top:
                if root.RT is None:
                    root.RT = toadd
                else:
                    self.add(root.RT, toadd)
            elif toadd.rect.left == root.rect.left and toadd.rect.top != root.rect.top:
                if root.LB is None:
                    root.LB = toadd
                else:
                    self.add(root.LB, toadd)
            elif toadd.rect.left != root.rect.left and toadd.rect.top != root.rect.top:
                if root.RB is None:
                    root.RB = toadd
                else:
                    self.add(root.RB, toadd)

    def BFS(self):
        image2 = cv2.imread('singleSlice.png')
        que = queue.Queue()
        que.put(self.root)
        while que.qsize() != 0:
            v = que.get()
            draw(v.rect, image2)
            if v.LT is not None:
                que.put(v.LT)
            if v.RT is not None:
                que.put(v.RT)
            if v.LB is not None:
                que.put(v.LB)
            if v.RB is not None:
                que.put(v.RB)
        cv2.imshow('image2', image2)
        cv2.waitKey(0)