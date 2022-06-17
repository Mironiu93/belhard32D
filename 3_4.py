first_digit = int(input('Enter the first digit: '))
second_digit = int(input('Enter the second digit: '))
third_digit = int(input('Enter the third digit: '))
true_first_digit = (first_digit > 0)
true_second_digit = (second_digit > 0)
true_third_digit = (third_digit > 0)
count_positive = true_first_digit + true_second_digit + true_third_digit
count_negative = 3 - count_positive
print('Positive numbers amount: ', count_positive)
print('Negative numbers amount: ',  count_negative)