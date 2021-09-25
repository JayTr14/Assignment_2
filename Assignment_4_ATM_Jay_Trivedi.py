""" ATM machine """
pin = 1234
attempts = 3
while True:
    try:
        ans = int(input('Please enter a pin: '))
        if ans != pin:
            print('Invalid pin please try again: ')
            attempts -= 1
        if attempts == 0:
            print('Account locked the police is on its way')
            break
        if ans == pin:
            print('You have no money in your account')
            break
    except ValueError:
        print('Invalid pin please try again')
        break
