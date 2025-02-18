def sum_number(number):
    sum = 0
    for i in range(len(number)):
        sum += number[i]
    return sum
def largest_number(number):
    max = number[0]
    for i in range(len(number)):
        if number[i] > max:
            max = number[i]
    return max        
def even_number():
    for i in range(0,20, 2):
        if i != 0:
            print(i, end=' ')

def frequency_word(sentence):
    frequency = {}
    words = sentence.split(' ')
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

num = [1, 2, 3, 4, 5, 6]
print("sum:", sum_number(num))
even_number()
print("\nLargest number:", largest_numb8er(num))
sentence = "I love python programming"
print(frequency_word(sentence))
