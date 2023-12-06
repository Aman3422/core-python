class Calc:
    def sum(self,a,b):
        c=a+b
        print(c)

    def substraction(self,a,b):
        c=a-b
        print(c)
    def mult(self,a,b):
        c=a*b
        print(c)
    def divide(self,a,b):
        c=a/b
        print(c)

object=Calc()
object.sum(10,20)
object.substraction(20,10)
object.mult(10,1)
object.divide(100,10)