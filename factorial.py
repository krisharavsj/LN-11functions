def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("factorial(0)",factorial(0))
print("factorial(1)",factorial(1))
print("factorial(2)",factorial(2))
print("factorial(3)",factorial(3))
print("factorial(4)",factorial(4))
print("factorial(5)",factorial(5))