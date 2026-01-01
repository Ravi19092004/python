#def average(a,b):
#    print("the average is ", (a+b)/2)
#average(4,6)
def average(a=2,b=3):
    print("the average is ", (a+b)/2)
#average()
#average(1,6)
#average(5)
average(b=5)
#1)default argument
def name(fname,mname,lname):
    print("hello,",fname,mname,lname)
name("ravishankar","gharabidi","pitambar")
#2)keyword argument
'''in this we can change the place of the value '''
average(b=5,a=6)
#3)required arguments
'''in this if we use 3 values a b c so we should give the value of atleast 2 values and 3rd one can be have the default value'''
def average(a,b,c=5):
    print("The average is ", (a+b+c)/3)
average(8,9)
def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
        print("average is:",sum /len(numbers))
average(5,6)
#keyword arbitrary argument
def name(**name):
    print("hello,",name["fname"],name["mname"],name["lname"])
name(lname="pitambar",fname="ravishankar",mname="gharabidi")

#return statement is used to return the value of the expression back to the calling function.
def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
        return sum /len(numbers)
c = average(5,6,7,8)
print(c)
