# We can express the elements of a list as a sequence of values separated by commas and enclosed in square brackets.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
print(bicycles[0])

# Index Positions Start at 0, Not 1
print(bicycles[1])
print(bicycles[3])

 # Use the value of a list item
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# Changing, Adding, and Removing Elements
# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to a List
# Appending Elements to the End of a List
motorcycles.append('honda')
print(motorcycles)

# Inserting Elements into a List
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing Elements from a List
# Removing an Item Using the del Statement
del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Popping Items from any Position in a List
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print(motorcycles)

# Removing an Item by Value
motorcycles.remove('yamaha')
print(motorcycles)

# Organizing a List
# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)


# Sorting a List Permanently in Reverse Alphabetical Order
cars.sort(reverse=True)
print(cars)

# Reversing the Order of a List
cars.reverse()
print(cars)

# Finding the Length of a List
print(len(cars))

# Avoiding Index Errors When Working with Lists
# IndexError: list index out of range   print(cars[4])

# Accessing the Last Element in a List
print(cars[-1])
