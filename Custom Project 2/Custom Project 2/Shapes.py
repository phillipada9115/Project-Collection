#import time
#import turtle
import random
from Constants import *
from Questions import Q


if Q.shape == "1":
    def S1():
        t.right(180)
        t.circle(size)
        t.right(180)
    def S2():
        for i in range(2):
            t.forward(int(size2)*0.7)
            t.right(60)
            for j in range(20):
                t.forward(int(size2)/20)
                t.right(3)
            t.right(60)
elif Q.shape == "2":
    def S1():
        for i in range(4):
            t.forward(size)
            t.right(90)
    def S2():
        for i in range(2):
            t.forward(int(size2)/2)
            t.right(90)
            t.forward(int(size2)*1.5)
            t.right(90)
elif Q.shape == "3":
    def S1():
        for j in range(3):
            t.forward(size)
            t.right(120)
    def S2(): 
        t.forward(int(size2)*0.7)
        t.right(75)
        t.forward(int(size2)*0.6)
        t.right(45)
        t.forward(int(size2)*1.2)
        t.right(120)
        t.forward(int(size2)*1.2)
        t.right(45)
        t.forward(int(size2)*0.6)
        t.right(75)