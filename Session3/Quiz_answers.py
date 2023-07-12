#Question no. 1
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    if num == 3:
        break
    total += num
print(total)

#Ans: 3

#Question no. 2
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num, end = ' ')
print('\n', end = '')

#Ans: 1 3 5

#Question no. 3
i = 0
while i < 5:
    if i == 3:
        break
    i += 1
print(i)

#Ans: 3

#Question no.4
x = 10
y = 5
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")

#Ans: x is greater than y

#Question no. 5
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')
print('\n', end = '')

#Ans: 1 2 4 5

#Question no. 6
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    if num % 2 != 0:
        total += num
print(total)

#Ans: 9

#Question no. 7
x = 5
y = 3
if x > y:
    if x % y == 0:
        print("x is divisible by y")
    else:
        print("x is not divisible by y")
else:
    print("Invalid comparison")

#Ans: x is not divisible by y

#Question no.8
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        break
    print(num)
else:
    print("All numbers are even")

#Ans: 1

#Question no. 9
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')
else:
    if i == 5:
        print("Loop completed successfully", end=' ')
print('\n', end = '')

#Ans: 1 2 4 5 Loop completed successfully

#Question no. 10
x = 100
while x > 0:
    print(x, end=' ')
    x = x // 2

#Ans: 100 50 25 12 6 3 1

