from random import randint

x, y = input(f'Hey, Choose your lucky number range: ').split()
#x, y = [int(x) for x in [x, y]]
#x, y = [int(x) for x in input().split()] 
x = int(x)
y = int(y)
answer = randint(x,y)
#print(answer)

while True:
    try:
        guess = int(input(f'Guess your lucky number of the day from {x} to {y}:  '))
        if  x < guess < y:
            if guess == answer:
                print('You are a genius!You won the game! ')
                break
        else:
            print('hey silly, I said {x} to {y}')
    except ValueError:
        print('Please enter a number and try again')
    continue