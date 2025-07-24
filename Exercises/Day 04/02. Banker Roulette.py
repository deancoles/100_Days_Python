# Pick a random name from the list of friends
import random

# Method 1
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print (random.choice(friends))

# Method 2
random_index = random.randint(0, 4)
print(friends[random_index])