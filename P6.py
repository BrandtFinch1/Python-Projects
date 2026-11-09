
#This isn't going to be the greatest program  
#and there might be a few lines of code that
#aren't needed but I have been working on this
#for the past 3 hours so it should be good

from graphics import *

def main():
  
    win = GraphWin("Python", 800, 800)
    line= Line(Point(100,100), Point(100,500))
    
    #line2= Line(Point(200,500), Point(0,500))
    circle= Circle(Point (100,400), 100)
    rectangle= Rectangle(Point(25,50), Point(0,500))



    rectangle2= Rectangle(Point(375,54), Point(400,475))
    r4= Rectangle(Point(250,495), Point(400,450))

    r5= Rectangle(Point(475,500), Point(500,55))
    r6= Rectangle(Point(500, 250), Point (600, 300))
    r7= Rectangle(Point(500, 75), Point (650, 175))

    r4.setFill("red")

    r6.setFill("red")

    r4.setFill("red")

    r5.setFill("red")

    r7.setFill("red")


    rectangle2.setFill("red")



    
    
    
    line.setOutline("red")

    r6.draw(win)
    r7.draw(win)

    

    
    circle.setFill("red")

    circle.draw(win)
    rectangle.draw(win)
    rectangle.setFill("red")

    rectangle2.draw(win)
    r4.draw(win)
    r5.draw(win)



   
    win.setBackground("white")
    win.getMouse()
   



    

main()