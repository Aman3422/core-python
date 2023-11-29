# from shape import Shape
# s=Shape("green",2)
# s.setColor(input(("enter color")))
# print(s.getColor())
# s.setBorderWidth(3)
#
# print(s.getBorderWidth())
# print(Shape.PI)
# print(s.getPi())

from ractangle import Ractangle
obj=Ractangle("red",12,25,3)
print(obj.getLength())
print(obj.getColor())
print(obj.getBorderWidth())
print(obj.getwidth())
print(obj.area())


from circle import Circle
cir=Circle("red",6)
cir.setRadius(6)
print(cir.getPi())
cir.setColor("RED")
print(cir.getColor())
print(cir.area())


print(cir.area()*obj.area())