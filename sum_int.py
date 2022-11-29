'''
Sum of Integers Up To n (integersums.py)

Write a function, add_it_up(), 
that takes a single integer as input
and returns the sum of the integers from zero to the input parameter. 
'''
def add_it_up(x):
    sum = 0
    if type(x) is int:
        for i in range(x+1):
            sum = sum + i 
            # print(i)
        return sum
    else:
        return 0
def first(n):
    num = 1
    sum = 0
    while num < n + 1:
        sum = sum + num
        num = num + 1
    return sum       
# print(type(33 ))
print(add_it_up(9))
print(first(9))

