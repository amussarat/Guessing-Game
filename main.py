from random import randint

x, y = input(f'Hey, Choose your lucky number range: ').split()

start = int(x)
end = int(y)

while True:
    try:
        guess = int(input(f'Guess your lucky number of the day from {x} to {y}:  '))
        if  int(x) <= guess <= int(y):
            answer = randint(start,end)
            if guess == answer:
                print('You are a genius!You won the game! ')
                break
        else:
            print(f'Hey silly, I said from {x} to {y}')
        
    except ValueError:
        print('Please enter a number and try again')
    continue