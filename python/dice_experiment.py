import random
number=random.randint(1,12)
print(number)
if(number%6==0):
    print("your turn is over")
else:
    print("try again")