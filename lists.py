
#list comprehension
mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist]
print(mylist)
print(b)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)

words = ['apple', 'banana', 'cherry']
first_letters = [word[0] for word in words]
print(first_letters)

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
fruits = ['apple' , 'cherry', 'orange']
people = [(names, ages, fruits) for names, ages, fruits in zip(names, ages, fruits)]
print(people)

string = 'Hello, There'
characters = [char for char in string]
print(characters)

for i in fruits:
    print(i)

if 'rice' in fruits:
    print('yes')
else:
    print('no')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)
list_org = ["banana", "cherry", "apple"]

list_cpy = list_org[:]

list_cpy.append("lemon")

print(list_cpy)
print(list_org)
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1::]
print(a)

#iterating through a list by creating a for loop
for i in mylist:
  print(i)

#if statement in a list
if "banana" in mylist:
    print("yes")
else:
    print("no")

#checking for the number of element in your list
print(len(mylist))

#using append that enables you to add non-exitent variable
mylist.append("rice")
print(mylist)

#adding an item with it index
mylist.insert(3, "rosemary")
print(mylist)

#clearing a list
item = mylist.clear()
print(mylist)

#using the sort method
item = mylist.sort()
print(mylist)

#Reversing a list
item = mylist.reverse()
print(mylist)

#Removing an item
item = mylist.remove("apple")
print(mylist)
print(item)
print(mylist)
item = mylist[2]
print(item)
mylist2 = list()
mylist2 = [5, True, "apple", "apple"]
print(mylist2)
