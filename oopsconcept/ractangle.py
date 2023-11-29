from shape import Shape

class Ractangle(Shape):
    def __init__(self,color,bw,length,width):
        super().__init__(color,bw)
        self.__length = length
        self.__width= width

    def setLength(self,length):
        self.__length=length

    def getLength(self):
        return self.__length

    def setWidth(self,w):
        self.__width=w

    def getwidth(self):
        return self.__width

    def area(self):
        return self.getwidth() * self.getLength()