########################################################################
# Assignment 0: Introduction to Graphics, Drawing 2D coordinate system
# Roll number: 22071211
# Name: Bhavya
# Date: 14-08-2023
########################################################################
import graphics as gr;
def lines(x1,y1,x2,y2):
    line=gr.Line(gr.Point(x1,y1), gr.Point(x2,y2));
    line.setArrow("both");
    line.draw(myWin);
def text(x,y,msg,window):
    txt=gr.Text(gr.Point(x,y),msg);
    txt.draw(window);

max_x=640;
max_y=480;
mid_x=max_x/2;
mid_y=max_y/2;

myWin = gr.GraphWin("my window", max_x, max_y); #creating window object
myWin.setBackground("lightGrey");

lines(50,mid_y,max_x-50,mid_y); #y-axis line
lines(mid_x,15,mid_x,max_y-15); #x-axis line
text(mid_x-10,mid_y+10,"0",myWin); #intersection point 0

cir=gr.Circle(gr.Point(mid_x+150,mid_y-150),70); #top right circle
cir.setFill("pink");
cir.draw(myWin);
#lines within circle
lines(mid_x+100,mid_y-100,mid_x+200,mid_y-200);#left-bottom to right-top
lines(mid_x+100,mid_y-200,mid_x+200,mid_y-100);#left-top to right-bottom
lines(mid_x+80,mid_y-150,mid_x+220,mid_y-150);#left to right
lines(mid_x+150,mid_y-220,mid_x+150,mid_y-80);#top to bottomm
text(mid_x+160,mid_y-40,"My first design",myWin)

#defining x-axis and y-axis
text(mid_x,8,"y axis",myWin);
text(mid_x,max_y-8,"-y axis",myWin);
text(25,mid_y,"-x axis",myWin);
text(max_x-25,mid_y,"x axis",myWin);

cir=gr.Circle(gr.Point(mid_x-130,mid_y+130),50); #bottom left circle
cir.setFill("skyblue");
cir.draw(myWin);

myWin.getMouse();
myWin.close();
