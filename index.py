marks = [3,4,5,6,"ravi", True ]
print(marks)
print(type(marks))
#positive index
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
#negative index
print(marks[0])
print(marks[-1])
print(marks[-2])
print(marks[-3])
print(marks[-4])
print(marks[len(marks)-3])
#check whether an item is present in list or not
if "ravi" in marks: 
  print("yes")
else:
  print ("no")
if "ra" in "ravi":
  print("yes")
else:
  print("no")
#same thing applies in string as well.
print(marks[:])
print(marks[-4:5:1])
