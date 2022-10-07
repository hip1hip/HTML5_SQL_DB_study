

##
##  Coding by 홍인표 
##

#from turtle import *

import turtle as t

##forward (100)
##fd(10)
##right (90)
##fd(110)
##rt(90)
##fd(110)
##rt(90)
##fd(110)

##backward (100)
##up ()
##backward (100)
##down ()
##backward (100)

"""
forward (100)
right (90)
fd(100)
lt(90)
up()
fd(100)
down()
lt(90)
fd(100)
rt(90)
fd(100)
lt(90)
up()
fd(100)
down()
lt(90)
fd(100)
rt(90)
fd(100)
lt(90)
up()
fd(100)
down()
lt(90)
fd(100)
rt(90)
fd(100)
"""


"""
a = 0
b = 0
for a in range(3):
    for b in range(3):
        circle(25)
        up()
        fd (50)
        down()
        
    up()
    backward(150)
    down()
    rt(120)
"""

"""
def coolUp():

    write ("시원한 하늘")

    color ("red")

coolUp()


color ("purple")

write ("Coding by 홍인표")


a=0 
for a in range(4):
    fd(20)
    rt(90)


coolUp()
"""

def spiral ( spLength ):

    if spLength <= 5:
        return
    t.rt(90)

    t.fd(spLength)
    
    spiral(spLength-10)
    
    

# 함수 정의 종료


t.color ("red")
t.speed(0)
spiral(350)
#t.hideturtle()
t.write ("Coding by 홍인표")
t.done()

















