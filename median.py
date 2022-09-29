"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        
    except ValueError:
        print("Some input could not be converted to a number!")
        
    else:
        break
    
print(numbers)
numbers.sort()

def median():

    if len(numbers) % 2 != 0:
        median = numbers[int(len(numbers) / 2)]
        print(median)
        return median

    else:
        
        length = len(numbers)
        

        a = numbers[int(length / 2)]
        b = numbers[int((length / 2) - 1)]

        median = (a + b) / 2
        print(median)
        return median


median()
