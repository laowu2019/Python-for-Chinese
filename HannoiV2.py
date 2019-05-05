#HannoiV2.py
import turtle, time

pie = []
Apos, Bpos, Cpos = [], [], []
Acnt, Bcnt, Ccnt = 0, 0, 0
Atop = [-180, 125]
Btop = [0, 125]
Ctop= [180, 125]
A = [Atop, Apos, Acnt]
B = [Btop, Bpos, Bcnt]
C = [Ctop, Cpos, Ccnt]
m = 0

def MakePies(n):
    global pie, Apos, Bpos, Cpos
    turtle.tracer(False)
    for i in range(n):
        pie.append("")
        pie[i] = turtle.Turtle('square')
        pie[i].shapesize(1,8-i)
        pie[i].penup()
        #time.sleep(1)
        pie[i].goto(-180,-95+20*i)
        #time.sleep(1)
        Apos.append("")
        Bpos.append("")
        Cpos.append("")
        Apos[i] = [pie[i].xcor(), pie[i].ycor()]
        Bpos[i] = [pie[i].xcor()+180, pie[i].ycor()]
        Cpos[i] = [pie[i].xcor()+360, pie[i].ycor()]
        #time.sleep(1)
    turtle.tracer(True)
    #pie[n-1].goto(Cpos[0])

def HannoiSetup(n):
    turtle.tracer(False)
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(-270,-105)
    turtle.pendown()
    for l in range(3):
        turtle.fd(90)
        turtle.left(90)
        turtle.fd(210)
        turtle.bk(210)
        turtle.right(90)
        turtle.fd(90)
    turtle.penup()
    turtle.bk(450)
    turtle.right(90)
    turtle.fd(30)
    turtle.left(90)
    turtle.write('A', font=('Arial',16,'bold'))
    turtle.fd(180)
    turtle.write('B', font=('Arial',16,'bold'))
    turtle.fd(180)
    turtle.write('C', font=('Arial',16,'bold'))
    turtle.hideturtle()
    turtle.tracer(True)
    MakePies(n)

def HannoiMoves(n, src = A, mid = B, dst = C):
    #global pie
    #global Apos, Bpos, Cpos
    #global Acnt, Bcnt, Ccnt
    #global Atop, Btop, Ctop
    #global m
    if n == 1:
        pie[m-n].speed(1)
        pie[m-n].goto(src[0])
        #pie[m-n].goto(mid[0])
        pie[m-n].goto(dst[0])
        pie[m-n].goto(dst[1][dst[2]])
        src[2] -= 1
        dst[2] += 1
    else:
        HannoiMoves(n-1, src, dst, mid)
        #move(n, src, mid, dst)
        pie[m-n].speed(1)
        pie[m-n].goto(src[0])
        #pie[m-n].goto(mid[0])
        pie[m-n].goto(dst[0])
        pie[m-n].goto(dst[1][dst[2]])
        src[2] -= 1
        dst[2] += 1
        HannoiMoves(n-1, mid, src, dst)
    
def main():
    n = eval(input("Levels(<= 7): "))
    turtle.setup()
    #turtle.speed(1)
    HannoiSetup(n)
    Acnt = n
    m = n
    time.sleep(3)
    HannoiMoves(n)
    time.sleep(1)
    turtle.goto(-40, 150)
    turtle.write("Done",font=("Arial", 30))
    turtle.done()

main()