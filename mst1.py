########################################################################
# MST-I: draw rectangle using DDA and then rotate it by 45
# Roll number: 22071211
# Name: Bhavya
# Date: 31-10-2023
########################################################################

import graphics as gr
import numpy as np
max_x = 1240
max_y = 780
mid_x = max_x / 2
mid_y = max_y / 2
def create_window():
    win = gr.GraphWin("mst", max_x, max_y)
    l1 = gr.Line(gr.Point(mid_x, 0), gr.Point(mid_x, max_y))
    l1.draw(win)
    l1 = gr.Line(gr.Point(0, mid_y), gr.Point(max_x, mid_y))
    l1.draw(win)
    return win
def closeWin(win):
    win.getMouse()
    win.close()
def DDA(x1, y1, x2, y2, win):
    dx=x2-x1
    dy=y2-y1
    adx = abs(dx)
    ady = abs(dy)
    steps=adx if adx>=ady else ady
    steps = int(steps)
    if steps==0:
        xinc = 0
        yinc = 0
        win.plotPixel(x1, y1, "black")
        return
    if(adx == 0):
        xinc=0
    else:
        xinc = dx/steps
    if(ady == 0):
        yinc=0
    else:
        yinc = dy/steps
    x, y = x1, y1
    win.plotPixel(x, y, "black") 
    for i in range(steps):
        x+=xinc
        y+=yinc
        win.plotPixel(round(x), round(y), "black") 

def rotation(theta):
    theta = np.radians(theta)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                [np.sin(theta), np.cos(theta), 0],
                                [0, 0, 1]])
    return rotation_matrix
def matrixToVertices(matrix):
    vertices = []
    for i in range(2):
        vertices.append(round(matrix[0][i]))
        vertices.append(round(matrix[1][i]))
    return vertices

def drawRect(x1, y1, x2, y2, win):
    DDA(mid_x + x1, mid_y - y1, mid_x + x1, mid_y - y2, win)
    DDA(mid_x + x1, mid_y - y2, mid_x + x2, mid_y - y2, win)
    DDA(mid_x + x2, mid_y - y2, mid_x + x2, mid_y - y1, win)
    DDA(mid_x + x2, mid_y - y1, mid_x + x1, mid_y - y1, win)
        
def main():
    win = create_window()
    x1, y1 = 50, 50
    x2, y2 = -50, -50
    drawRect(x1, y1, x2, y2, win)
    homo_marix = np.array([[x1, x2],
                           [y1, y2],
                           [1, 1]])
    rotation_matrix = rotation(45)
    result = np.dot(rotation_matrix, homo_marix)
    vertices = matrixToVertices(result)
    drawRect(*vertices, win)
    closeWin(win)
if __name__ == "__main__":
    main()