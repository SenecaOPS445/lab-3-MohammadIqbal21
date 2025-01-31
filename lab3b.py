#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: 105830228

def sum_numbers(number1, number2):
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

def subtract_numbers(number1, number2):
    num1 = 10
    num2 = 5
    num3 = num1 - num2
    return num3

def multiply_numbers(number1, number2):
    num1 = 10
    num2 = 5
    num3 = num1 * num2
    return num3

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))