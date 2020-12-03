# 1
def your_function(*args, **kwargs):
    sum = 0
    for number in args:
        if type(number) is int:
            sum += number
    return sum


print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))  # 3
print(your_function())  # 0
print(your_function(2, 4, 'abc', param_1=2))  # 6


# 2
def recursive_function_1(number):
    if number == 0:
        return 0
    return recursive_function_1(number - 1) + number


print(recursive_function_1(7))


def recursive_function_2(number):
    if number == 0:
        return 0
    if number % 2 == 0:
        return recursive_function_2(number - 1) + number
    else:
        return recursive_function_2(number - 1)


print(recursive_function_2(7))


def recursive_function_3(number):
    if number == 0:
        return 0
    if number % 2 == 1:
        return recursive_function_3(number - 1) + number
    else:
        return recursive_function_3(number - 1)


print(recursive_function_3(7))

# one function :

def sums(number):
    if number == 0:
        return 0, 0, 0
    totalSum, even_sum, odd_sum = sums(number - 1)
    totalSum += number
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
    return totalSum, even_sum, odd_sum

total_sum, even_sum, odd_sum = sums(7)
print(total_sum, even_sum, odd_sum)

# 3
def val_intreg():
    write = input("Write your 'number': ")
    try:
        write = int(write)
        return write
    except ValueError as e:
        #print(e)
        return 0


print(val_intreg())
