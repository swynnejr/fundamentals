num1 = 42 #variable declaration: int
num2 = 2.3 #variable declaration: float
boolean = True #data type: boolean
string = 'Hello World' #data type: string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration: array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration: object
fruit = ('blueberry', 'strawberry', 'banana') #error: shouldnt this have [] 
print(type(fruit)) #log statment: function
print(pizza_toppings[1]) #log statement: string array (topping is sausage from array above)
pizza_toppings.append('Mushrooms') # I think this is adding a mushrooms to the pizza topping array, like .push in js
print(person['name']) #log statment: this is trying to pull the name John from the object established above
person['name'] = 'George' #I think this is adding the name George to a persons array of data
person['eye_color'] = 'blue' #same as above, but rather creating a category not previously established and adding the data to it
print(fruit[2]) #log statment: trying to print 'banana' from the fruit array above (no brackets)

if num1 > 45: #conditional - else if
    print("It's greater") #log statement
else: #conditional - else
    print("It's lower") #log statement

if len(string) < 5: #condtional if
    print("It's a short word!") #log statment
elif len(string) > 15: #conditional else if
    print("It's a long word!") #log statment
else: #conditional else
    print("Just right!") #log statment

for x in range(5):
    print(x) #log statement
for x in range(2,5):
    print(x) #log statement
for x in range(2,10,3):
    print(x) #log statement
x = 0 #variable declaration
while(x < 5): #while loop: start
    print(x) #log statement
    x += 1 #while loop: incriment

pizza_toppings.pop() #removes the last item from array 'pizza toppings'
pizza_toppings.pop(1) #removes index one? or maybe it just pop()

print(person) #log statment for an object established above
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)