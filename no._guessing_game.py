import random
random_num=random.randint(1,100)
attempts=5
score=0
for attempt in range(1,attempts+1):
    guess=int(input("enter guessing number : "))

    if guess==random_num:
        print("Your number is correct")
        score=(attempts-attempt+1)*100
        break
        
    elif guess > random_num:
        print("OOps ! number is high")

    else:
        print("OOps ! number is low")
        
        
    print("Attempts left:", attempts - attempt)
    
if guess != random_num:
    print("\nGame over!")
    print("The correct number was:", random_num)

print("Your score:", score)
