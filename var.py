#Unpacking: Collection of values in list can be extract the value in variable
cars = ["BMW", "Audi", "Mercedes"]
x, y, z = cars
print(x)
print(y)
print(z)

#Global Variables: Created outside the function & use anywhere
a = "World"

def function():
  print("Hello " + a)

function()

#If you use the global keyword, the variable belongs to the global scope
def func():
  global x
  x = "BSCS"

func()

print("Its "  + x)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#List : Used to store multiple items in single variable 
list = ["Apple", "Banana", "Cherry", "kiwi", "melon", "mango"]

list[1] = "blackcurrant"      #Change the second item
list.insert(2, "watermelon")

print(list)
print(len(list))        #To check length of list  
print(type(list))       #To check the type of data store in list

print(list[-1])         #To check the item by -ve index
print(list[2:5])        #To check item between range

#Dictionary 
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
