import datetime

def exercise1():
    name = input('What is your name?: ')
    age = input('What is your age?: ')
    times = input('Pick a random number: ')
    x = datetime.datetime.now()
    current_year = x.year
    years_left = 100 - int(age)
    future_year = current_year + years_left
    y = 1
    while y <= int(times):
        print (name,'you will turn 100 years old in the year',future_year)
        y += 1

exercise1()
