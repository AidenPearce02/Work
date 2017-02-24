import turtle
from cmd import Cmd
import random

class Figure(object):
   def __init__(self):
       self.a = 0.0
       self.b = 0.0
       self.x = 0.0
       self.y = 0.0

   def draw(self):
       pass

   def drawf(self):
       pass

   def input_date(self):
       pass


class Square(Figure):
    def __init__(self):
        super(Square, self).__init__()

    def draw(self):
        self.x=turtle.xcor()
        self.y=turtle.ycor()
        for i in range(4):
            turtle.forward(self.a)
            turtle.left(90)

    def drawf(self):
        turtle.penup()
        turtle.setposition(self.x,self.y)
        turtle.pendown()
        for i in range(4):
            turtle.forward(self.a)
            turtle.left(90)

    def input_date(self):
        self.a = float(input("Input a: "))


class Rectangle(Figure):
    def __init__(self):
        super(Rectangle, self).__init__()

    def draw(self):
        self.x=turtle.xcor()
        self.y=turtle.ycor()
        for i in range(2):
            turtle.forward(self.a)
            turtle.left(90)
            turtle.forward(self.b)
            turtle.left(90)

    def drawf(self):
        turtle.setx(self.x)
        turtle.sety(self.y)
        for i in range(2):
            turtle.forward(self.a)
            turtle.left(90)
            turtle.forward(self.b)
            turtle.left(90)

    def input_date(self):
        self.a = float(input("Input a: "))
        self.b = float(input("Input b: "))


class Circle(Figure):
    def __init__(self):
        super(Circle, self).__init__()

    def draw(self):
        self.x=turtle.xcor()
        self.y=turtle.ycor()
        turtle.circle(self.a)

    def drawf(self):
        turtle.setx(self.x)
        turtle.sety(self.y)
        turtle.circle(self.a)

    def input_date(self):
        self.a = float(input("Input a: "))


class TriangleE(Figure):
    def __init__(self):
        super(TriangleE, self).__init__()

    def draw(self):
        self.x=turtle.xcor()
        self.y=turtle.ycor()
        for i in range(3):
            turtle.forward(self.a)
            turtle.left(120)

    def drawf(self):
        turtle.setx(self.x)
        turtle.sety(self.y)
        for i in range(3):
            turtle.forward(self.a)
            turtle.left(120)

    def input_date(self):
        self.a = float(input("Input a: "))


class Storage(object):
    def __init__(self):
        self.storage={}

    def addff(self,ids,figure):
        self.storage[ids]=figure
        if "Circle" in str(figure):
            figuref = Circle()
            f = figure.split(',')
            figuref.a = float(f[1])
            figuref.x = float(f[3])
            figuref.y = float(f[4])
            figuref.drawf()

        elif "Square" in str(figure):
            figuref = Square()
            f = figure.split(',')
            figuref.a = float(f[1])
            figuref.x = float(f[3])
            figuref.y = float(f[4])
            print(str(figuref.a)+" "+str(figuref.x)+" "+str(figuref.y ))
            figuref.drawf()

        elif "Rectangle" in str(figure):
            figuref = Rectangle()
            f = figure.split(',')
            figuref.a = float(f[1])
            figuref.b = float(f[2])
            figuref.x = float(f[3])
            figuref.y = float(f[4])
            figuref.drawf()

        elif "TriangleE" in str(figure):
            figuref = TriangleE()
            f = figure.split(',')
            figuref.a = float(f[1])
            figuref.x = float(f[3])
            figuref.y = float(f[4])
            figuref.drawf()

    def addf(self, ids, figure):
        if "Circle" in str(figure):
            self.storage[ids] = "Circle," + str(figure.a)+","+str(figure.b) + ","+str(figure.x)+","+str(figure.y)
        if "Rectangle" in str(figure):
            self.storage[ids] = "Rectangle," + str(figure.a)+"," +str(figure.b) + ","+str(figure.x)+","+str(figure.y)
        if "TriangleE" in str(figure):
            self.storage[ids] = "TriangleE," + str(figure.a)+","+str(figure.b) + ","+str(figure.x)+","+str(figure.y)
        if "Square" in str(figure):
            self.storage[ids] = "Square," + str(figure.a)+","+str(figure.b) + ","+str(figure.x)+","+str(figure.y)

    def ls(self):
        for i in sorted(self.storage.keys()):
            print ("(%s -> %s)" % (i,self.storage[i]))

storage=Storage()
name=""
class MyCmd(Cmd):

    def do_ls(*args, **kwargs):
        storage.ls()

    def do_coordinate(*args,**kwargs):
        turtle.penup()
        x=float(input("Insert x: "))
        y=float(input("Insert y: "))
        turtle.setx(x)
        turtle.sety(y)
        turtle.pendown()

    def do_draw(*args, **kwargs):

        print("Menu to select figures")
        print("Press 1 to draw square")
        print("Press 2 to draw rectangle")
        print("Press 3 to draw circle")
        print("Press 4 to draw eTriangle")
        print("Press 0 to exit to main menu")
        chosenF = int(input("Your choice: "))
        if chosenF == 1:
            figure = Square()
            figure.input_date()
            figure.draw()
            storage.addf(random.randint(10, 99), figure)
        elif chosenF == 2:
            figure = Rectangle()
            figure.input_date()
            figure.draw()
            storage.addf(random.randint(10, 99), figure)
        elif chosenF == 3:
            figure = Circle()
            figure.input_date()
            figure.draw()
            storage.addf(random.randint(10, 99), figure)
        elif chosenF == 4:
            figure = TriangleE()
            figure.input_date()
            figure.draw()
            storage.addf(random.randint(10, 99), figure)
        elif chosenF == 0:
            pass

    def do_save(*args,**kwargs):
        name = input("File name: ")
        f = open(name, 'w')
        for index in storage.storage:
            f.write(str(index)+" "+storage.storage[index]+'\n')
        turtle.bye()
        f.close()

    def do_open(*args,**kwargs):
        name = input("File name: ")
        f = open(name)
        for line in f:
            if line!='\n':
                text=line[3:]
                storage.addff(int(line[0])*10+int(line[1]),text)
        turtle.Screen()
        f.close()

    def do_create(*args,**kwargs):
        name=input("File name: ")
        f=open(name,'w')
        storage=Storage()
        turtle.Screen()
        f.close()

    def do_exit(*args, **kwargs):
        turtle.bye()
        exit()


c1 = MyCmd()
c1.cmdloop()

