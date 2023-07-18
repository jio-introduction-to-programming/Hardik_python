#Q1 : Write a function which takes a list as input and return its sum

import statistics


def sum_num(nums):
    return sum(nums)

number = [1,2,3,4,5,6]
result1 = sum_num(number)
print('sum of the numbers:  ', result1)



#Q2 : Write a function which takes a list as an input and return the max element in the list

def max_num(number):
    return max(number)

number = [3,4,55,6,7,888]
result2 = max(number)
print('MAx number:  ', result2)




#Q3 : Write a function which takes a list as input and returns the reverse of the list in the output

def reverse_lst(lst):
    n_lst = lst[::-1]
    return n_lst

lst1 = [1,2,3,4,5,6,7,8]
result3 = reverse_lst(lst1)
print('reverse_list: ', result3)


#Q4 : Write a function which takes a list as input and returns the list in sorted format.

def sort_lst(lst4):
    lst4.sort()
    return lst4

list_4 = [32,5,65,21,10,10]
result4 = sort_lst(list_4)
print('Sorted list will be: ', result4)



#Q5 : Write a function which takes a list as an input and returns the following statistics: 1.Mean/avg 2. Mode

def stats(lst5):
    total = sum(lst5)
    mean1 = total / len(lst5)
    n_lst5 = statistics.mode(lst5)
    return   "mode: {} and mean: {}".format(n_lst5, mean1)  


lst_5 = [22,33,44,55,66,77,33,22,22]
result5 = stats(lst_5)
print(result5)


#trial code

def math(a,b):
    return a + b, a*b

x = 5
y =6
result = math(x,y)
print(result)



