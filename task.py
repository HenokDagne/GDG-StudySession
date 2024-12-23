def sum_number(number):
    sum = 0
    for i in range(len(number)):
        sum += number[i]
    return sum
def even_number():
    for i in range(0,20, 2):
        if i != 0:
            print(i, end=' ')

num = [1, 2, 3, 4, 5, 6]
print("sum:", sum_number(num))
even_number()
