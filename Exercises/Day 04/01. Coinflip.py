print("This is a coinflip generator")
coin_toss = random.randint(0, 1)
if coin_toss == 0:
    print("Heads")
else:
    print("Tails")