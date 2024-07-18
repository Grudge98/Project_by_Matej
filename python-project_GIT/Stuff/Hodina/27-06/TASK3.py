import math
from functools import reduce

class MathOperations:

    @staticmethod
    def find_largest(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def find_smallest(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def calculate_average(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Not defined for negative number")
        return math.factorial(n)


a, b, c, d = 10, 20, 4, 3

print("Largest:", MathOperations.find_largest(a, b, c, d))
print("Smallest:", MathOperations.find_smallest(a, b, c, d))
print("Average:", MathOperations.calculate_average(a, b, c, d))
print("Factorial of 8:", MathOperations.factorial(8))