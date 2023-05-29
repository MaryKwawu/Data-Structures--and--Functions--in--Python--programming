
my_tuples = (1, 2, 3)
print(my_tuples)

person = ('John', 25, 'USA')
print(person[0][3])#this refers to john  thus the index 0 and letter n
print(person[2])

def get_name_age():
    name = 'Alice'
    age = 30
    return name, age

result = get_name_age()
print(result)

fruits = ('Pear', 'Pineapple', 'apple')
# print(len(fruits))
print(fruits.count('Pineapple'))

fruits = list(fruits)
print(fruits)

fruits = tuple(fruits)
print(fruits)

my_tuple = "Richeal", 28, "Boston"
name, age, city = my_tuple
print(name)
print(age)
print(city)
