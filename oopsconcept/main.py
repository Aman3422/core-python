# # #******EXCEPTION HANDLING
#
# a=5
# b=0
# try:
#     c=5/0
#     print(c)
# except:
#     print("plz enter a right digit")
# #
# #
# try:
#     age=int(input("enter any number:"))
#     print(age)
# except:
#     print("enter a numeric value")
#
# a=5
# b==0
# try:
#     c=a/b
#     print(c)
# except Exception as e:
#     print("please enter right number",e)
#
# a=4
# b=0
# try:
#     c=a/b
#     print('c:',c)
# except ZeroDivisionError:
#     print("check your division is zero")
# else:
#     print("your division is grater than zero")

####TRY-FINALLY

# a=10
# b=5
# try:
#     c=a/b
#     print('c:',c)
# except ZeroDivisionError as e:
#     print("check your division is zero")
# finally:
#     print("finally executed")

###RAISE EXEPTION

# try:
#     num1=int(input("enter a numerator:"))
#     num2=int(input("enter a denominator:"))
#
#     result=num1/num2
# ##THIS WILL RAISE AN EXCEPTION IF THE RESULT IS A DECIMAL
#     if result %1 !=0:
#         raise ValueError("result is not an integer")
#
# ##THIS WILL RAISE AN EXCEPTION IF THE RESULT IS NEGATIVE
#
#     if result <0:
#         raise ValueError("result is negative",result)
#
#     print(f"the result of the division is: {result}")
#
# except ValueError as ve:
#     print(f"Error:{ve}")
#
# except ZeroDivisionError:
#     print("Error:cannot divide by zero")
#
# except Exception as e:
#     print(e)
#

