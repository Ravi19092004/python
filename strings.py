names = "ravi,nikhil"
print(names[0:4])
print(names[:4])
print(names[:])
print(names[5:11])
print(names[0:2:5])
print(len(names))
name="vivek"
friend ="rohan"
anotherfriend='lavish'
akshay='he said, I want to eat apple'
              #or
#akshay="he said \* I want to eat apple"
print(akshay)
print("hello"+ name)
ravi='''
hi
ravi
how are you
'he said, I want to eat apple'''
print(ravi)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print("lets use a for loop")
for character in akshay:
    print(character)
fruit = "!!! mango!!!!! !!!!!! mango !!!! mango"
mangolen = len(fruit)
print(mangolen)
print(fruit[0:4])
#including o but not 4
print(fruit[1:4])
print(fruit[:4])
print(fruit[0:4])
print(fruit[0:-4])
print(fruit[-1:4])
print(fruit[-1:-4])
print(fruit.upper())
print(fruit.lower())
print(fruit.rstrip("!"))
print(fruit.replace("mango","apple"))
print(fruit.split("!"))
print(fruit.split(" "))
#blogheading="introduction to python"
blogheading="introDuction tO pyThon"
print(blogheading.capitalize())
str1= "welcome to python world"
print(len(str1))
print(len(str1.center(50)))
print(str1.center(50))
print(fruit.count("mango"))
print(str1.endswith("to",4,10))
print(str1.endswith("!!!"))
str= "he's name is dan. he is a honest man"
print(str.find("is"))
#if is not found then it will give -1 value.
#print(str.index("is"))
#if is not found then it will give error.
str2="Welcome To The Console"
print(str2.isalnum()) #in this it can be (A-Z),(a-z),(1-10) then true.
print(str2.isalpha()) #in this it can be (A-Z),(a-z) then true.
print(str2.islower())#in this it can be (a-z) then true.
print(str2.isprintable())
str3="                      "
print(str2.isspace()) #if the space is given then it will give true.
print(str3.isspace())
print(str2.istitle()) #if the title is given in capital letters then it will give true.
print(str2.swapcase()) #it will swap the uppercase into lowercase or lowercase into uppercase.
print(str2.startswith("Welcome")) #if the sentence starts with welcome then it will print true or it wil give false.
print(str.title()) #it will capitalize the starting letters of everyword.