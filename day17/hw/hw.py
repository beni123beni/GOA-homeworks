#age = 0

#while age < 10:
    #print(age)
    #age = age + 1
#age = 20

#while age > 10:
    #print(age)
    #age = age - 1


secret = 'goa'
user_guess = input('enter secret word:')

while user_guess != secret:
    user_guess = input('enter secret word:')

print('match!')