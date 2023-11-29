# QUESTION - WRITE A PROGRAM TO CHECK WHETHER THE GIVEN NUMBER IS EVEN OR ODD?
# a=eval(input("enter any number"))
# if a%2==0:
#     print("this is even:")
# else:
#     print("this is odd:")
# num=int(input("enter any number"))


#""GIVEN NUMBER IS ONE,TWO,THREE DIGIT?
# n=str(num)
# if len(n) == 1:
#     print("one digit number")
# elif len(n) == 2:
#     print("two digit number")
# elif len(n) == 3:
#     print("three digit number")
# else:
#     print("more than three digit")


# QUESTION - WRITE A PROGRAM TO CHECK WHETHER THE GIVEN NUMBER IS IN BETWEEN 1 AND 100?
# a=eval(input("enter any number"))
# if a>1 and a<100:
#     print("this number",a,"is in between 1 to 100")
# else:
#     print("this number",a,"is not in between 1 to 100")


# #QUESTION - WRITE A PROGRAM TO PRINT HELLO WORLD 10 TIMES.
# s="Hello world"
# index = 1
# while index < len(s):
#     if index % 2==1:
#       print(s[index])
#     index += 1
#
# QUESTION - WRITE A PROGRAM TO CRATE LIST WITH 0 TO 100.


#""SELF"(FOR LOOP)
# a="hello world"
# count=0
# for x in a:
#     count+=1
#     print(x)
# print("the number of character:",count)

#""SELF"" TO PRINT CHARACTERS PRESENT IN STRING INDEX WISE
# a="hello world"
# i=0
# for x in a:
#     print("the character present at",i,"index is:",x)
#     i+=1

#""SELF"" TO PRINT SUM OF NUMBERS PRSEENT IN LIST
# list=eval(input("enter any list"))
# sum=0
# for x in list:
#     sum=sum+x
# print("the sum=",sum)

#QUESTION - COUNT THE ALPHABET PRESENT IN THE STRING
# s="jalaj420@gmail.com"
# index = 0
# alp = 0
# while index<len(s):
#     char=s[index]
#     if 'a'<= char <='z':
#      print(char)
#      alp=alp+1
#     index+=1
# print("the total alphabet presebnt in string:",alp,)

# "+++++++++++++++++++++++++++++++++++++++++PRINT THE PRESENT SPECIAL CHARACTERS..
# s="jalaj420@gmail.com"
# index = 0
# alp = 0
# while index<len(s):
#     char=s[index]
#     if 'a'<= char<='z' or '0'<=char <= '9':
#      alp=alp+1
#     index+=1
# n=len(s)-alp
# print('the special character=',n)

#PRINT THE EKEMENTS OF A LIST IN HORIZONTAL FORM
# list=[10,20,30,40,50]
# for x in list:
#     print(x)

#PRINT THE ELEMENTS OF A LIST IN HORIZONTAL FORM USING WHILE LOOP.
# list=[10,20,30,40]
# sum=0
# index=0
# while index < len(list):
#     n=list[0]+list[1]+list[2]+list[3]
#     print(list[index])
#     index+=1
# print(n)


#WRITE A PROGRAM TO EXTRACT ALL THE VOWELS FOR FROM THE ABOVE STRING AND ADD IT TO A LIST.
# a="aman vishwakarma"
# l=[]
# for char in a:
#     if char in "aeiou" or char in "AEIOU":
#        l.append(char)
# print(l)

# for x in range(65,91):
#    print(chr(x),"assigned for acii value",x)


#QUESTION--->CREATE THE DICTIONARY WITH LOWERCASE ALPHABETS AS KEYS AND THERE ASCII VALUES AS VALUES.
# d={}
# for asci in range(ord('a'),ord('z')+1):
#     char=chr(asci)
#     d[char]=asci
# print(d)

##QUESTION----> [PRINT ALL THE VOWEL WITH THE VALUE FROM THE DICTIONARY]..

# d={'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
# for key in d:
#     var=d[key]
#     if key in 'AEIOUaeiou':
#         print(key,var)

##QUESTION----> [PRINT ALL THE VOWEL WITH THE VALUE FROM THE DICTIONARY]..
# d={}
# for ascii in range(ord('A'),ord('z')+1):
#     char=chr(ascii)
#     d[char]=ascii
# for x in d:
#     var = d[x]
#     if x in "AEIOUaeiou":
#         print(x,var)

##---> PRINT ALL THE KEY WHICH HAVE VALUES ENDING WITH 1 OR 4:
# d={'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
# for key in d:
#     var = str(d[key])
#     if var[-1] == '1' or var[-1] == '4':
#      print(key,var)

# d={'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
# for key in d:
#     var = str(d[key])
#     if var[-1]== '2'or var[-1]=='4':
#          print(key,var)

#QUESTION----->>>>>PRINT CALCULATOR

# a=int(input("enter any number:"))
# b=int(input("enter any number:"))
# operator=input("enter any operator(+,-,/,*)")
# if operator =='+':
#     print("addition",a+b)
# elif operator == '-':
#     print("substraction",a-b)
# elif operator == '/':
#     print("division",a/b)
# elif operator == '*':
#     print("multiplication",a*b)
# else:
#     print("invalid")







