#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while True:
        if counter == 0:
            print('Happy New Year!')
            break
        print(counter)
        counter -= 1

def square_integers(int_list):
    return [int * int for int in int_list]

def fizzbuzz():
    for num in range(1, 101):
        if num % 5 == 0 and num % 3 == 0:
            print('FizzBuzz')
        elif num % 5 == 0:
            print('Buzz')
        elif num % 3 == 0:
            print('Fizz')
        else:
            print(num)
