#TO PRINT NUMBERS FROM 1 TO 10 BY USING WHILE LOOP
# x=1
# while x<=10:
#     print(x)
#     x+=1
import random

#TO DISPLAY THE SUM OF FIRST 'N' NUMBERS

# n=int(input("enter any number:"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("the sum of first",n,"numbers is",sum)

#WRITE A PROGRAM TO PROMPT USER TO ENTER SOME NAME UNTILL ENTERING DURGA

# name=""
# while name!='durga':
#     name=input("enter name")
# print("thanx for confirmation")

#"""USER NAME & PASSWORD"""
# name=""
# password=""
# while name!='aman' or password!='bhaiya':
#     name=input("enter name:")
#     password=input("enter password")
# print("login successful")

###################TRANSFER STATEMENT#################
#1----->>>> BREAK
#eg.
# for i in range(10):
#     if i==7:
#        print("processing is enough..plz break:")
#        break
#     print((i))

#eg2
# cart=[10,20,30,400,700,40,50]
# for item in cart:
#     if item>500:
#         print("this item must needed insurence:")
#         break
#     print(item)
#2----->>>>>>>>>"""continue
# cart=[10,20,30,400,700,40,50]
# for item in cart:
#     if item>500:
#         print("this item must needed insurence:")
#         continue
#     print(item)
#3---->break loop with else-> if break is not executed then else execute

# cart=[10,20,30,40]
# for item in cart:
#     if item>=500:
#         print("this order is not processed:")
#         break
#     print(item)
# else:
#     print("all orders is processed")

# cart=[10,20,500,30,40]
# for item in cart:
#     if item>=500:
#         print("this order is not processed:")
#         continue
#     print(item)
# else:
#     print("all orders is processed")

#---->>>>string operator
# s=input("enter any string")
# i=0
# for x in s:
#     print("the character present at positive index {} and at negative index {} is {}".format(i,i-len(s),x))
#     i+=1

##--->WRITE A PROGRAM TO ACCESS EEACH CHARACTER OF STRING IN FORWARD AND BACKWARD DIRECTION BY USIN WHILE LOOP?
#
# s="python is very easy"
# n=len(s)
# i=0
# print("foward direction")
# while i<n:
#     print(s[i],end='')
#     i+=1
# print()
# print("backward direction")
# i=-1
# while i>=-n:
#     print(s[i],end='')
#     i=i-1

#ALTERNATIVE WAY USING FOR LOOP--->>>>>>>>

# s="python is very easy language"
# n=len(s)
# print("forward direction")
# for i in s:
#     print(i,end='')
# print()
# print("backward direction")
# for i in s[::-1]:
#     print(i,end='')

# WRITE A PROGRAM TO READ MAIN AND SUB STRING FROM KEY BOARD CHECK SUB STRING AVALABLE IN MAIN STRING OR NOT
# s=input("enter main string:")
# subs=input("enter sub string")
# if subs in s:
#     print(subs,"is found in main string")
# else:
#     print(subs,"is not found in main string")

# a=int(input("enter any number b/w 1 to 9:"))
# b= random.randrange(1,9)
# for i in range(b):
#     print("the number is matched:")
# else:
#     print("the number is not matched:")
#     option= ("do you want to any other number:[yes|no]")
#     if option == "no":
#     break
# print("thanx")