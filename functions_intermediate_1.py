# x = [ [5,2,3], [10,8,9] ]
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

#1.1 Change value 10 in x to 15

# x[1][0] = 15
# print(x)

#1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'

# students[0]['last_name'] = 'Bryant'
# print(students)

#1.3 In the sports_directory, change 'Messi' to 'Andres'

# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

#1.4 Change the value 20 in z to 30

# z[0]['y'] = 30
# print(z)

# 2 Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:


# iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#Emile help

# def iterate_dictionary(list):
#     for i in range(0, len(list)):
#         output = ""
#         for key,val in list[i].items():
#             output += f" {key} - {val},"
#         print(output)

# iterate_dictionary(students)

#other way to do it

# def iterateDictionary(data):
#     for dict in data:
#         for key,value in dict.items():
#             print(f'{key} - {value},')

#Santana Help
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}]

# def iterateDictionary(studentArray):
#     for i in studentArray:
#         print(i)

# iterateDictionary(students)

# Problem 3 - NEEDS WORK

# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}]




# def iterateDictionary2(key_name, some_list):
#     for i in some_list:
#         print([i],'key_name')

# def iterateDictionary2(key_name, some_list):
#     for i in some_list.key_name():
#         print([i])

# relevant example from learn platform

# my_dict = { "name": "Noelle", "language": "Python" }
# for k in my_dict:
#     print(my_dict[k])
# output: Noelle, Python



# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

# Problem 4 -

# Relevant example from learn platform:

# capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#      print(key)
# # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# #to iterate through the values
# for val in capitals.values():
#      print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# #to iterate through both keys and values
# for key, val in capitals.items():
#      print(key, " = ", val)
# # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# my_list = ["abc", 123, "xyz"]
# for i in range(0, len(my_list)):
#     print(i, my_list[i])
# # output: 0 abc, 1 123, 2 xyz
# # OR
# for v in my_list:
#     print(v)
# # output: abc, 123, xyz



# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(dict):
#     something with len('locations')
#     print(locations.value)

# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon



