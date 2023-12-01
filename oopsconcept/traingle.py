from shape import Shape
class traingle(Shape):
    def __init__(self,height,base):

        self.__height=height
        self.__base=base

    def setheight(self,height):
        self.__height = height

    def getheight(self):
        return self.__height

    def setbase(self,base):
        self.__base=base

    def getbase(self):
        return self.__base

    def area(self):
        return self.__base*self.__height*0.5