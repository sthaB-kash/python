import random
# generate number between 0 to 1
print(random.random())
# generate number between 10 to 20
print(random.randint(10, 20))

# randomly pic an element of the list
names = ['bikash', 'samita', 'shrestha']
leader = random.choice(names)
print(leader)