#11.Write a program to create function which shall accept any number of arguments and display total of all the numbers given as argument.

def sum_all(*args):
    result = 0
    for num in args:
        result += num
    return result
print(sum_all(1,2,3,4,5))
        

