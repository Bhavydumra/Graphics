import graphics as gr
import numpy as np
def line(x1, y1, x2,y2):
    l = gr.Line(gr.Point(x1, y1), gr.Point(x2, y2))
    l.draw(win)
win = gr.GraphWin("window", 780, 680)
line(100, 200)
win.getMouse()
win.close()