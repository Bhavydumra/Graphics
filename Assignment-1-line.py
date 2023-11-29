########################################################################
# Assignment 1: Scan Converting Line
# Roll number: 22071211
# Name: Bhavya
# Date: 31-08-2023
########################################################################
import graphics as gr;
import time

def lineUsingDirect(x1,y1,x2,y2,p_color,win):
    dx=x2-x1
    dy=y2-y1
    adx=abs(dx)
    ady=abs(dy)
    if(dx==0 and dy==0):
        p=gr.Point(x1,y1)
        p.setFill(p_color)
        p.draw(win)
        return
    if(adx==0):
        x_inc=0
    else:
        x_inc=dx/adx
    if(ady==0):
        y_inc=0
    else:
        y_inc=dy/ady
    x=x1
    y=y1
    l=gr.Line(gr.Point(x1,y1),gr.Point(x2,y2))
    l.setFill("white")
    l.draw(myWin)
    p=gr.Point(x,y)
    p.setFill(p_color)
    p.draw(win)
    if(adx>=ady):
        x=x+x_inc
        m=dy/dx
        b=y1-m*x1
        while(x!=x2):
            x=x+x_inc
            y=m*x+b
            time.sleep(0.01)
            p=gr.Point(x,y)
            p.setFill(p_color)
            p.draw(win)
    else:
        if(dx==0):
            while(y!=y2):
                y=y+y_inc
                # x=m_inv*(y-b) 
                time.sleep(0.01)  
                p=gr.Point(x,y)
                p.setFill(p_color)
                p.draw(win)
            return
        y=y+y_inc
        m=dy/dx
        m_inv=1/m
        b=y1-m*x1
        while(y!=y2):
            y=y+y_inc
            x=m_inv*(y-b)   
            time.sleep(0.01)
            p=gr.Point(x,y)
            p.setFill(p_color)
            p.draw(win)

def lineUsingDDA(x1,y1,x2,y2,p_color,win):
    dx=x2-x1
    dy=y2-y1
    adx=abs(dx)
    ady=abs(dy)
    steps=max(adx,ady)
    if(steps==0):
        x_inc=0
        y_inc=0
    else:
        x_inc = dx/steps
        y_inc = dy/steps
    l=gr.Line(gr.Point(x1,y1),gr.Point(x2,y2))
    l.setFill("white")
    l.draw(win)
    x,y=x1,y1
    p=gr.Point(x,y)
    p.setFill(p_color)
    p.draw(win)
    time.sleep(0.01)
    for i in range(1,steps):
        x+=x_inc
        y+=y_inc
        p=gr.Point(x,y)
        p.setFill(p_color)
        p.draw(win)
        time.sleep(0.01)

def lineUsingParametric(x1,y1,x2,y2,p_color,win):
    dx=x2-x1
    dy=y2-y1
    adx=abs(dx)
    ady=abs(dy)
    l=gr.Line(gr.Point(x1,y1),gr.Point(x2,y2))
    l.setFill("white")
    l.draw(win)
    if(adx==0 and ady==0):
        u_inc=1
    elif(adx>ady):
        u_inc=1/adx
    else:
        u_inc=1/ady
    u=0
    x,y=x1,y1
    p=gr.Point(x,y)
    p.setFill(p_color)
    p.draw(win)
    time.sleep(0.01)

    while(u<=1):
        u+=u_inc
        x=x1+u*dx
        y=y1+u*dy
        p=gr.Point(x,y)
        p.setFill(p_color)
        p.draw(win)
        time.sleep(0.01)

def lineUsingBresenham(x1,y1,x2,y2,p_color,win):
    l1 = gr.Line(gr.Point(x1, y1), gr.Point(x2, y2))
    l1.setFill("white")
    l1.draw(win)

    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    adx = abs(dx)
    ady = abs(dy)

    pt = gr.Point(x, y)
    pt.setFill(p_color)
    pt.draw(win)

    if dx == 0:
        xinc = 0
    else:
        xinc = dx / adx

    if dy == 0:
        yinc = 0
    else:
        yinc = dy / ady

    if adx > ady:
        p = 2 * ady - adx
        while x != x2:
            if p < 0:
                p = p + 2 * ady
            else:
                p = p + 2 * ady - 2 * adx
                y = y + yinc
            x = x + xinc
            pt = gr.Point(x, y)
            pt.setFill(p_color)
            pt.draw(win)
            time.sleep(0.01)
    else:
        p = 2 * adx - ady
        while y != y2:
            if p < 0:
                p = p + 2 * adx
            else:
                p = p + 2 * adx - 2 * ady
                x = x + xinc
            y = y + yinc
            pt = gr.Point(x, y)
            pt.setFill(p_color)
            pt.draw(win)
            time.sleep(0.01)
            
max_x=640;
max_y=480;
myWin = gr.GraphWin("my window", max_x, max_y); #creating window object
myWin.setBackground("black");

values={
    'x1':[100,100,400,400,100,100,200,200,100,400,100,100,100],
    'y1':[100,200,100,200,100,400,100,400,100,100,100,200,100],
    'x2':[400,400,100,100,200,200,100,100,400,100,100,100,100],
    'y2':[200,100,200,100,400,100,400,100,100,100,200,100,100],
    'color':["red","blue","green","skyblue","olive","pink","purple","orange","yellow","lightGreen","brown","teal","magenta"]
}
while(True):
    print("""    1. Direct Approach. 
    2. Parameteric Approach.
    3. Digital Differential Analyzer Approach.
    4. Bresenham Approach.
    5. Exit
        """)
    choice=int(input("Enter your choice:-"))
    if(choice==5):
        break
    match(choice):
            case 1:
                i=0
                while(i<13):
                    lineUsingDirect(values['x1'][i],values['y1'][i],values['x2'][i],values['y2'][i],values['color'][i],myWin)
                    i+=1
                myWin.getMouse();
                myWin.close();
            case 2:
                i=0
                while(i<13):
                    lineUsingParametric(values['x1'][i],values['y1'][i],values['x2'][i],values['y2'][i],values['color'][i],myWin)
                    i+=1
                myWin.getMouse();
                myWin.close();
            case 3:
                i=0
                while(i<13):
                    lineUsingDDA(values['x1'][i],values['y1'][i],values['x2'][i],values['y2'][i],values['color'][i],myWin)
                    i+=1
                myWin.getMouse();
                myWin.close();
            case 4:
                i=0
                while(i<13):
                    lineUsingBresenham(values['x1'][i],values['y1'][i],values['x2'][i],values['y2'][i],values['color'][i],myWin)
                    i+=1
                myWin.getMouse();
                myWin.close();