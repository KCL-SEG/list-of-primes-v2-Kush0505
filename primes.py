"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def primes(number_of_primes):
    list = []
    if (number_of_primes <= 0):
        raise ValueError('Only input numbers greater than 0')
    num = 2
    list.append(num)
    while(len(list) < number_of_primes):
        counter = 0
        num+=1
        for i in range(2,int(math.sqrt(num)+1)):
            if(num % i == 0):
                counter+=1
                break
        if(counter == 0):
            list.append(num)
    
    return list


