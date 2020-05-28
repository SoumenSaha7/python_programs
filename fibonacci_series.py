# To print the Fibonacci series
def fib(n):  # defines a function to find the fibonacci no. of given index using recursion
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


terms = int(input("Please, enter the no. of terms of Fibonacci series to show: "))
fib_list = []
i = 0
if terms <= 0:  # in case the no. given as input is -ve or 0
    print("Invalid Input\n")
else:
    while i < terms:
        fib_list.insert(i, fib(i))  # the fibonacci nos. are stored in a list
        i += 1
    print(*fib_list, sep=", ", end="\n\n")  # prints the list elements separated by ", "


"""
OUTPUT:
    # 1
    Please, enter the no. of terms of Fibonacci series to show: 10
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    
    # 2
    Please, enter the no. of terms of Fibonacci series to show: -1
    Invalid Input
"""
