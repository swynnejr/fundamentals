# #  Problem 3 -  Get key value from list of dictionaries

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# # Define a function thats reuasable for both key values in a list
# def iterateDictionary2(key_name, some_list):
#     # iterate through the dictionaries in my list
#     for i in range(0, len(some_list)):
#         # For KEY VALUE PAIRS in whatever list I pass into this fucniton
#         for key,val in some_list[i].items():
#             if key == key_name:
#                 print(val)

# # iterateDictionary2('first_name', students)

# iterateDictionary2('last_name', students)

# Problem 4

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key,value in some_dict.items():
        print('------')
        print(f'{len(value)}', key)
        print('------')
        for i in range (0,len(value)):
            print(value[i])

printInfo(dojo)

