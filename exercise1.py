# Exercise: Write a list comprehension which, from a list,
# generates a lowercased version of each string that has
# length greater than five.

fruits = ['apple', 'orange', 'strawberry', 'pineapple']
upperCaseFruit = [x.upper() for x in fruits if len(x)>5 ]
print(upperCaseFruit)
