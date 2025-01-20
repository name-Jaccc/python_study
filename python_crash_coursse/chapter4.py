# Access all elements in a list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Create a list of numbers
for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

# Assignments

for value in range(1,21):
    print(value)

numbers = []
for value in range(1,1000001):
    numbers.append(value)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = [num for num in range(1,21,2)]

for number in odd_numbers:
    print(number)

list = [num for num in range(3,31,3)]
for num in list:
    print(num)

list = []
for value in range(1,11):
    list.append(value**3)
print(list)

list = [value**3 for value in range(1,11)]
print(list)

# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
for player in players[0:3]:
    print(player.title())

# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[0:3]:
    print(player.title())
for player in players[1:4]:
    print(player.title())
for player in players[-3:]:
    print(player.title())

# Tuples
food = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')
for item in food:
    print(item)

food = ('pizza', 'falafel', 'carrot cake', 'canddddnoli', 'ice crddddeam')
for item in food:
    print(item)