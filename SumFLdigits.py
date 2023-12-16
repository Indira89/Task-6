def sum_of_first_and_last_digit(number):
  
    num_str = str(number)

    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])

    sum_result = first_digit + last_digit

    return sum_result

user_input = int(input("Enter an integer: "))
result = sum_of_first_and_last_digit(user_input)
print(result)