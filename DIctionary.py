mydict = {"name": "Max", "age": 28, "city": "Ho" }
print(mydict)

mydict2 = dict(name="Mary", age=27, town="Hohoe")
print(mydict2)
#adding an item that was previously not there
mydict2["school"] = {}
mydict2["school"]["email"] = "ST Joseph's School Complex", "saint.com"
print(mydict2)
value = mydict['age']
print(value)
value = mydict2.get('name')
value = mydict2['name']
print(value)

#using pop in dictionary
# mydict2.pop("town")
# print(mydict2)

mydict2.popitem()
print(mydict2)

#if statements
if "name" in mydict:
    print(mydict["name"])

if "town" in mydict2:
    print(mydict2["town"])
#using try except statement
try:
    print(mydict2["lastname"])
except:
    print("Error")

#using for loop
for key in mydict2:
    print(key)

for value in mydict2.values():
    print(value)

for key, value in mydict2.items():
    print(key, value)

#using copy
mydict2_cpy = mydict2
mydict2_cpy = mydict2.copy()
mydict2_cpy["email"] = "saint.com"
# print(mydict2)
# print(mydict2_cpy)

mydict.update(mydict2)
print(mydict)

