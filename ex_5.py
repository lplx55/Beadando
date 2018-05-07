import random

signs=['+','-','']              #can put them between the numbers in 3^8 ways
numbers=[i for i in range(1,10)]    #might be sets
#i=random.choice(signs)
for k in range(-1,9):
    for i in random.choice(signs):
        print(numbers[k],i,numbers[k+1])