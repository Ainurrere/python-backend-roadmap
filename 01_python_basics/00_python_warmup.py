def get_number_status(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

numbers = [12, -4, 7, 0, 25, -8, 13, 6]
sum_positive = 0
total_sum = 0
negative_count = 0
max_number = numbers[0]

for number in numbers:
    total_sum += number
    if number > 0:
        sum_positive += number
    if number < 0:
        negative_count += 1
    if number > max_number:
        max_number = number

average = total_sum / len(numbers)

print("Сумма положительных чисел:", sum_positive)
print("Количество отрицательных чисел:", negative_count)
print("Максимальное число:", max_number)
print("Среднее арифметическое всех чисел:", average)

for number in numbers:
    print(number, "-", get_number_status(number))