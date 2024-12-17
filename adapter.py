
class XXCircle:
    def setLocation(self):
        print("XXCircle: Setting location")

    def getLocation(self):
        print("XXCircle: Getting location")

    def displayIt(self):
        print("XXCircle: Displaying")

    def fillIt(self):
        print("XXCircle: Filling")

    def setItsColor(self):
        print("XXCircle: Setting color")

    def undisplayIt(self):
        print("XXCircle: Undisplaying")



class Shape:
    def setLocation(self):
        pass

    def getLocation(self):
        pass

    def display(self):
        pass

    def fill(self):
        pass

    def setColor(self):
        pass

    def undisplay(self):
        pass



class CircleAdapter(Shape):
    def __init__(self):
        self.adaptee = XXCircle()

    def setLocation(self):
        self.adaptee.setLocation()

    def getLocation(self):
        self.adaptee.getLocation()

    def display(self):
        self.adaptee.displayIt()

    def fill(self):
        self.adaptee.fillIt()

    def setColor(self):
        self.adaptee.setItsColor()

    def undisplay(self):
        self.adaptee.undisplayIt()

class Point(Shape):
    def display(self):
        print("Point: Displaying")

    def fill(self):
        print("Point: Filling")

    def undisplay(self):
        print("Point: Undisplaying")


class Line(Shape):
    def display(self):
        print("Line: Displaying")

    def fill(self):
        print("Line: Filling")

    def undisplay(self):
        print("Line: Undisplaying")


class Rectangle(Shape):
    def display(self):
        print("Rectangle: Displaying")

    def fill(self):
        print("Rectangle: Filling")

    def undisplay(self):
        print("Rectangle: Undisplaying")



if __name__ == "__main__":
    shapes = [
        Point(),
        Line(),
        Rectangle(),
        CircleAdapter()
    ]

    for shape in shapes:
        shape.display()
        shape.fill()
        shape.undisplay()
        print()
