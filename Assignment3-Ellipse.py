########################################################################
# Assignment 3. Scan Conversion of Ellipse
# Roll number: 22071211
# Name: Bhavya
# Date: 14-09-2023
########################################################################

import graphics as gr
import math
import time
def create_Window(max_x, max_y, color):  
    win = gr.GraphWin("my window", max_x, max_y) #creating window object
    win.setBackground(color)
    lines(0, max_y/2, max_x, max_y/2, "white", win) # x-axis
    lines(max_x/2, 0, max_x/2, max_y, "white", win) # y-axis
    return win

def close_Window(win): #closing window
    win.getMouse()
    win.close()

def lines(x1, y1, x2, y2, color, win): # for drawing lines
    line=gr.Line(gr.Point(x1,y1), gr.Point(x2,y2))
    line.setFill(color)
    line.setArrow("both")
    line.draw(win)

def plot_Pixel(x, y, color, win):
    pt=gr.Point(x, y)
    pt.setFill(color)
    pt.draw(win)

def defaultEllipse(h,k,a,b,win): # white colored ellipse
    e1=gr.Oval(gr.Point(h-a,k-b),gr.Point(h+a,k+b))
    e1.setOutline("white")
    e1.draw(win)

def plotEllipsePixel( h, k, x, y, win):
    col=["red","blue","pink","purple"]
    plot_Pixel(h+x, k+y, col[0], win)
    plot_Pixel(h-x, k+y, col[1], win)
    plot_Pixel(h-x, k-y, col[2], win)
    plot_Pixel(h+x, k-y, col[3], win)

def ellipse_Direct(h, k, a, b, win): # Direct method 
    defaultEllipse(h, k, a, b, win)
    x=0
    y=b
    plotEllipsePixel(h, k, x, y, win)
    a_sq = a*a
    b_sq = b*b
    while(b_sq*x) <= (a_sq*y):
        x += 1
        y = b*math.sqrt(1-(x * x)/(a_sq))
        plotEllipsePixel(h,k,x,round(y),win) # round bcoz y is calculated from eqn
        time.sleep(0.02)
    y=round(y)
    while(y>0):
        y -= 1
        x = a * math.sqrt(1 - (y * y) / (b_sq))
        plotEllipsePixel(h,k,round(x),y,win) # round bcoz y is calculated from eqn
        time.sleep(0.02)

def ellipse_Polar(h, k, a, b, win): # Polar Domain
    defaultEllipse(h, k, a, b, win)
    if a>b:
        d_theta = 1/a
    else:
        d_theta = 1/b
    theta, x, y = 0, a, 0
    plotEllipsePixel(h, k, x, y, win)
    time.sleep(0.02)
    pi_by_2 = math.pi/2
    while theta <= pi_by_2:
        theta = theta + d_theta
        x = a * math.cos(theta)
        y = b * math.sin(theta)
        plotEllipsePixel(h, k, round(x), round(y), win) # round bcoz x and y is calculated from eqn
        time.sleep(0.02)

def ellipse_IncPolar(h, k, a, b, win): # incremental polar domain
    defaultEllipse(h, k, a, b, win)
    d_theta = 1/max(a,b)
    c = math.cos(d_theta)
    sab = (a / b) * math.sin(d_theta)
    sba = (b / a) * math.sin(d_theta)
    x, y= a, 0
    plotEllipsePixel(h, k, x, y, win)
    time.sleep(0.02)
    while x >= 0:
        x_temp=x
        x = x * c - sab * y
        y = x_temp * sba + y * c
        plotEllipsePixel(h, k, round(x), round(y), win) # round bcoz x and y is calculated from eqn
        time.sleep(0.02)
        
def ellipse_MidPoint(h, k, a, b, win): # Mid point approach
    defaultEllipse(h, k, a, b, win)
    x, y= 0, b
    a_sq = a*a
    b_sq = b*b
    p = (b_sq) - (a_sq * b) + (a_sq / 4)
    p = round(p)
    plotEllipsePixel(h, k, x, y, win)
    time.sleep(0.02)
    while(b_sq * x) <= (a_sq * y):
        if p < 0:
            p += b_sq * (2 * x + 3)
        else:
            p += b_sq * (2 * x + 3) + a_sq *(-2 * y + 2)
            y -= 1
        x += 1
        plotEllipsePixel(h, k, round(x), round(y), win) # round bcoz x and y is calculated from eqn
        time.sleep(0.02)
    p = b_sq * (x + 0.5) * (x + 0.5) + (a_sq) * (y - 1) * (y - 1) - a_sq * b_sq
    p=round(p)
    while y > 0:
        if p < 0:
            p += b_sq * (2 * x + 2) + a_sq * (-2 * y + 3)
            x += 1
        else:
            p += a_sq *(-2 * y + 3)
        y -= 1
        plotEllipsePixel(h, k, round(x), round(y), win) # round bcoz x and y is calculated from eqn
        time.sleep(0.02)

max_x=640
max_y=480
mid_x=max_x/2
mid_y=max_y/2

h=int(input("Enter the value of h:-")) 
k=int(input("Enter the value of k:-"))
a=int(input("Enter the value of a:-"))
b=int(input("Enter the value of b:-"))
h = mid_x + h
k = mid_y - k
while(True):
    print("""    1. Direct Approach. 
    2. Polar Domain Approach.
    3. Incremental Polar Domain Approach.
    4. Mid Point Approach.
    5. Exit
        """)
    choice=int(input("Enter your choice:-"))
    if(choice==5):
        break
    win=create_Window(max_x,max_y,"black")
    match(choice):
            case 1:
                ellipse_Direct(h, k, a, b, win)
                close_Window(win)
            case 2:
                ellipse_Polar(h, k, a, b, win)
                close_Window(win)
            case 3:
                ellipse_IncPolar(h, k, a, b, win)
                close_Window(win)
            case 4:
                ellipse_MidPoint(h, k, a, b, win)
                close_Window(win)
            case _:
                print("Enter a correct number")
