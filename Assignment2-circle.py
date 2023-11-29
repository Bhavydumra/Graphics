########################################################################
# Assignment 2: Scan converting a Circle
# Roll number: 22071211
# Name: Bhavya
# Date: 14-08-2023
########################################################################
import graphics as gr
import math
import time
def create_Window(max_x,max_y,color):  
    win = gr.GraphWin("my window", max_x, max_y) #creating window object
    win.setBackground(color)
    lines(0,max_y/2,max_x,max_y/2,"white",win)
    lines(max_x/2,0,max_x/2,max_y,"white",win)
    return win
def close_Window(win):
    win.getMouse()
    win.close()
def lines(x1,y1,x2,y2,color,win):
    line=gr.Line(gr.Point(x1,y1), gr.Point(x2,y2))
    line.setFill(color)
    line.setArrow("both")
    line.draw(win)
def default_Circle(h,k,r,color,win):
    c1=gr.Circle(gr.Point(h,k),r)
    c1.setOutline(color)
    c1.setWidth(2)
    c1.draw(win)
def put_Circle_Pixel(h,k,x,y,color,win):
    win.plotPixel(h+x,k+y,color[0])
    win.plotPixel(h-x,k+y,color[1])
    win.plotPixel(h+x,k-y,color[2])
    win.plotPixel(h-x,k-y,color[3])
    win.plotPixel(h+y,k+x,color[4])
    win.plotPixel(h-y,k+x,color[5])
    win.plotPixel(h+y,k-x,color[6])
    win.plotPixel(h-y,k-x,color[7])
def cicle_Direct(h,k,r,colors,win):
    x=0
    y=r
    default_Circle(h,k,r,"white",win)
    put_Circle_Pixel(h,k,x,y,colors,win)
    while(x<=y):
        x+=1
        y=math.sqrt(r*r-x*x)
        put_Circle_Pixel(h,k,x,y,colors,win)
        time.sleep(0.03)
def circle_Polar(h,k,r,color,win):
    default_Circle(h,k,r,"white",win)
    theta=0
    theta_inc=1/r
    while theta<=math.pi/4:
        x=r*math.cos(theta)
        y=r* math.sin(theta)
        theta+=theta_inc
        put_Circle_Pixel(h,k,x,y,color,win)
        time.sleep(0.03)
def circle_IncrementPolar(h,k,r,color,win):
    x=0
    y=r
    default_Circle(h,k,r,"white",win)
    dtheta=1/r
    sin=math.sin(dtheta)
    cos=math.cos(dtheta)
    put_Circle_Pixel(h,k,x,y,color,win)
    time.sleep(0.03)
    while(x<=y):
        xtemp=x
        x=x*cos-y*sin
        y=xtemp*sin+y*cos
        put_Circle_Pixel(h,k,round(x),round(y),color,win)
        time.sleep(0.03)
def circle_Bresenham(h,k,r,color,win):
    x=0
    y=r
    default_Circle(h,k,r,"white",win)
    p = 3-2*r
    put_Circle_Pixel(h,k,x,y,color,win)
    time.sleep(0.03)
    while x<=y:
        if p<=0:
            p+=4*x+6
        else:
            p+=4*(x-y)+10
            y-=1
        x+=1
        print("iteration", x, y, p)
        put_Circle_Pixel(h,k,x,y,color,win)
        time.sleep(0.03)
def circle_MidPoint(h,k,r,color,win):
    x=0
    y=r
    p=1-r
    default_Circle(h,k,r,"white",win)
    put_Circle_Pixel(h,k,x,y,color,win)
    time.sleep(0.03)    
    while x<=y:
        if p<0:
            p+=2*x+3
        else:
            p+=2*x-2*y+5
            y-=1
        x+=1
        put_Circle_Pixel(h,k,x,y,color,win)
        time.sleep(0.03)

max_x=640
max_y=480
mid_x=max_x/2
mid_y=max_y/2
h=int(input("enter the value of h:-"))
k=int(input("enter the value of k:-"))
r=int(input("enter the value of radius:-"))
colors=["red", "blue", "green", "skyblue", "pink", "purple", "orange", "yellow"]
while(True):
    print("""    1. Direct Approach. 
    2. Polar Domain Approach.
    3. Incremental Polar Domain Approach.
    4. Bresenham Approach.
    5. Mid Point Approach.
    6. Exit
        """)
    choice=int(input("Enter your choice:-"))
    if(choice==6):
        break
    match(choice):
            case 1:
                myWin=create_Window(max_x,max_y,"black")
                cicle_Direct(mid_x+h,mid_y-k,r,colors,myWin)
                close_Window(myWin)
            case 2:
                myWin=create_Window(max_x,max_y,"black")
                circle_Polar(mid_x+h,mid_y-k,r,colors,myWin)
                close_Window(myWin)
            case 3:
                myWin=create_Window(max_x,max_y,"black")
                circle_IncrementPolar(mid_x+h,mid_y-k,r,colors,myWin)
                close_Window(myWin)
            case 4:
                myWin=create_Window(max_x,max_y,"black")
                circle_Bresenham(mid_x+h,mid_y-k,r,colors,myWin)
                close_Window(myWin)
            case 5:
                myWin=create_Window(max_x,max_y,"black")
                circle_MidPoint(mid_x+h,mid_y-k,r,colors,myWin)
                close_Window(myWin)