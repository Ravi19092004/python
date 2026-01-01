a=int(input("enter your age: "))
print("your age is:",a)
#conditional statement
# >,<,>=,<=,==,!=
# print(a>=18)
# print(a<=18)
# print(a>18)
# print(a<18)
# print(a==18)
# print(a!=18)
if(a>=18):
    print("you are eligible to vote")
if(a<18):
    print("you are not eligible to vote") 
num=int(input("enter the value of num: "))
if(num<0):
    print("number is negative")
elif(num==0):
     print("number is zero") 
else:
    print("number is positive")
print("*******exit*******")
# nested if statement
a1=int(input("enter the number:"))
if (a1<0):
    print("your number is negative") 
elif(a1>0):
    if(a1<=0):
        print("number is  then greater then 0 or eequal to 0 ")
    elif(a1==0):
        print("number is zero")
    else:
        print("number is smaller then 0 or equal to 0")
else:
    ("print number is zero")
        
              