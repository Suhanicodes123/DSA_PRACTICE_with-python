Problem:Finding factorial
Concept:Recursion


num = int(input("Enter the number:"))

def factorial(n):
    if n == 0 or n ==1:
        return 1

    return n * factorial(n-1)
print("Factorial=", factorial(num))
