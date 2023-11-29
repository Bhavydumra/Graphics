########################################################################
# Assignment 6: Clipping
# Roll number: 22071211, 22071218
# Name: Bhavya, Jaspreet Kaur
# Date: 24-10-2023
########################################################################
import graphics as gr
import numpy as np
max_x = 1240
max_y=780
mid_x=max_x/2
mid_y=max_y/2
inside = {'top' : 0, 'bottom' : 0, 'right' : 0, 'left' : 0}
top = {'top' : 1, 'bottom' : 0, 'right' : 0, 'left' : 0}
bottom = {'top' : 0, 'bottom' : 1, 'right' : 0, 'left' : 0}
right = {'top' : 0, 'bottom' : 0, 'right' : 1, 'left' : 0}
left = {'top' : 0, 'bottom' : 0, 'right' : 0, 'left' : 1}

def create_Window(color):  
    win = gr.GraphWin("my window", max_x, max_y) #creating window object
    win.setBackground(color)
    lines(0, mid_y, max_x, mid_y, "white", win) # x-axis
    lines(mid_x, 0, mid_x, max_y, "white", win) # y-axis
    return win

def close_Window(win): #closing window
    win.getMouse()
    win.close()

def lines(x1, y1, x2, y2, color, win): # for drawing lines
    line=gr.Line(gr.Point(x1,y1), gr.Point(x2,y2))
    line.setFill(color)
    line.setArrow("both")
    line.draw(win)

def point(x1, y1, dx, dy, u):
    x = round(x1 + dx * ( u ))
    y = round(y1 + dy * ( u ))
    p = gr.Point(x, y)
    return p

def ClippingLine( x1, y1, x2, y2, color, win):
    line = gr.Line(gr.Point(mid_x + x1, mid_y - y1), gr.Point(mid_x + x2, mid_y - y2))
    line.setFill(color)
    line.draw(win)

def regionCode(x, y, xwmin, ywmin, xwmax, ywmax):
    code = {'top' : 0,'bottom' : 0,'right' : 0,'left' : 0}
    if y > ywmax:
        code['top'] = 1
    elif y < ywmin:
        code['bottom'] = 1
    if x > xwmax:
        code['right'] = 1
    elif x < xwmin:
        code['left'] = 1
    return code

def visible(code1, code2):
    result={}
    for key in code1.keys() & code2.keys():
        result[key] = code1[key] + code2[key]
    if result == inside:
        return True
    return False
def invisible(code1, code2):
    result={}
    for key in code1.keys() & code2.keys():
        result[key] = code1[key] * code2[key]
    if result != inside:
        return True
    return False

def cohenSutherlandDirect(x1, y1, x2, y2, xwmin, ywmin, xwmax, ywmax, win):
    ClippingLine(x1, y1, x2, y2, 'white', win )
    win.getMouse()
    code1 = regionCode(x1, y1, xwmin, ywmin, xwmax, ywmax)
    code2 = regionCode(x2, y2, xwmin, ywmin, xwmax, ywmax)

    while True:
        if(visible(code1, code2)):
            ClippingLine(x1, y1, x2, y2, 'red', win )
            break
        if(invisible(code1, code2)):
            ClippingLine(x1, y1, x2, y2, 'black', win )
            return    
        x, y = 0, 0
        if code1 != inside:
            code = code1
        else:
            code = code2
        if code['top']==1:
            x = x1 + (x2 - x1) * (ywmax - y1) / (y2 - y1)
            y = ywmax
        elif code['bottom']==1:
            x = x1 + (x2 - x1) * (ywmin - y1) / (y2 - y1)
            y = ywmin
        elif code['right']==1:
            y = y1 + (y2 - y1) * (xwmax - x1) / (x2 - x1)
            x = xwmax
        elif code['left']==1:
            y = y1 + (y2 - y1) * (xwmin - x1) / (x2 - x1)
            x = xwmin
        
        if code ==code1:
            x1, y1 = x, y
            code1 = regionCode(x1, y1, xwmin, ywmin, xwmax, ywmax)
        else:
            x2, y2 = x, y
            code2 = regionCode(x1, y1, xwmin, ywmin, xwmax, ywmax)

def cohenSutherlandMidPoint(x1, y1, x2, y2, xwmin, ywmin, xwmax, ywmax, win):
    ClippingLine(x1, y1, x2, y2, 'white', win )
    dx = x2-x1
    dy = y2-y1
    if(dx<=1 and dy<=1):
        return
    code1 = regionCode(x1, y1, xwmin, ywmin, xwmax, ywmax)
    code2 = regionCode(x2, y2, xwmin, ywmin, xwmax, ywmax)
    if(visible(code1, code2)):
        ClippingLine(x1, y1, x2, y2, "red", win)
        return
    if(invisible(code1, code2)):
        ClippingLine(x1, y1, x2, y2, "black", win)
        return    
    x, y = (x1 + x2)/2, (y1 + y2)/2
    cohenSutherlandMidPoint(x1, y1, x, y, xwmin, ywmin, xwmax, ywmax, win)
    cohenSutherlandMidPoint(x, y, x2, y2, xwmin, ywmin, xwmax, ywmax, win)
    return
  
def liangBarsky(x1, y1, x2, y2, xwmin, ywmin, xwmax, ywmax, win):
    ClippingLine(x1, y1, x2, y2, 'white', win )
    win.getMouse()
    dx = x2 - x1
    dy = y2 - y1
    p, q, r = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    p[1], p[2], p[3], p[4] = -dx, dx, -dy, dy
    q[1] = x1 - xwmin
    q[2] = xwmax - x1
    q[3] = y1 - ywmin
    q[4] = ywmax - y1
    u1, u2 = 0, 1
    for i in range(1, 5):
        if p[i]==0:
            if q[i]<0:
                ClippingLine(x1, y1, x2, y2, 'black', win )
                return
            else:
                continue
        r[i] = q[i] / p[i]
    for i in range(1, 5):	
        if p[i] < 0:
            u1 = max( u1, r[i])
        elif p[i] > 0: 
            u2 = min(u2, r[i])
    if u1 > u2:
        ClippingLine(x1, y1, x2, y2, 'black', win )
        return
    p1 = point(x1, y1, dx, dy, u1)
    p2 = point(x1, y1, dx, dy, u2)
    ClippingLine(x1, y1, p2.getX(), p2.getY(), 'black', win )
    ClippingLine(p1.getX(), p1.getY(), p2.getX(), p2.getY(), 'red', win )
    ClippingLine(p2.getX(), p2.getY(), x2, y2, 'black', win )
    
def drawRectangle(xwmin, ywmin, xwmax, ywmax, win):
    rect = gr.Rectangle(gr.Point(mid_x + xwmin, mid_y - ywmin), gr.Point(mid_x + xwmax, mid_y - ywmax))
    rect.setOutline('white')
    rect.draw(win)

def main():
    xwmin, ywmin = 0, 0
    xwmax, ywmax = 200, 100
    lines = [ (-50, -100, 100, 200),  # clip
        (15, 50, 150, 90),  # inside
        (205, 105, 250, 150),  # outside
        (100, -100, 100, 200),  # vertical clip
        (-50, 100, -50, 400),  # vertical left
        (300, 200, 300, 100),  # vertical right
        (-100, 50, 300, 50),  # horizontal clip
        (-100, 150, 300, 150),  # horizontal above
        (-100, -100, 300, -100) ] # horizontal below

    while(True):
        print('''1. Cohen Sutherland using direct approach
2. Cohen Sutherland using mid-point subdivision approach
3. Liang-Barsky parametric approach
4. EXIT''')
        choice = int(input('Enter choice:'))
        if(choice==4):
            break
        match(choice):
            case 1:
                win = create_Window("black")
                drawRectangle(xwmin, ywmin, xwmax, ywmax, win)
                for line in lines:
                    cohenSutherlandDirect(*line,  xwmin, ywmin, xwmax, ywmax, win)
                    win.getMouse()
            case 2:
                win = create_Window("black")
                drawRectangle(xwmin, ywmin, xwmax, ywmax, win)
                for line in lines:
                    cohenSutherlandMidPoint(*line,  xwmin, ywmin, xwmax, ywmax, win)
                    win.getMouse()
            case 3:
                win = create_Window("black")
                drawRectangle(xwmin, ywmin, xwmax, ywmax, win)
                for line in lines:
                    liangBarsky(*line,  xwmin, ywmin, xwmax, ywmax, win)
                    win.getMouse()
            case _:
                print("enter right choice")
                continue
        close_Window(win)
if __name__ == "__main__":
    main()
