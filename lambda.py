multiply = lambda num : num *2

# print (multiply(9))

#map() filter() reduce( )  recursion()

numbers = [1, 2, 3, 4, 5, 6, 7]


result = map(lambda num : num *6, numbers)
result1 = filter(lambda num : num % 2 ==0, numbers)

print(list(result))
print(list(result1))


#reduce

from functools import reduce

expenses = [
            ('Dinner', 90),
            ('Car repair', 120)

 ]

sum = reduce(lambda a,b : a[1] + b[1], expenses)

print(sum)


#recursion

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n *factorial(n - 1)

print(factorial(5))
