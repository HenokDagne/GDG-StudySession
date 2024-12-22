def sum_number(number):
    sum = 0
    for i in range(len(number)):
        sum += number[i]
    return sum

num = [1, 2, 3, 4, 5, 6]
print("sum:", sum_number(num))