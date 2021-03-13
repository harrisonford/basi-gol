def factorial(n):
    # return base case
    if n == 1:
        return 1

    return n * factorial(n - 1)


def steps(n):
    # step 0
    if n == 0:
        return [[0]]
    # step 1
    if n == 1:
        return [[0, 1]]

    n_1 = [a_list + [n] for a_list in steps(n-1)]
    n_2 = [a_list + [n] for a_list in steps(n-2)]

    return n_1 + n_2


# my_max([5, 2, 3, 8, 1, 6]) = 6
def my_bad_max(my_list):

    temp_max = 0
    counter = 0
    for index, value in enumerate(my_list):
        sublist = my_list[0:index]
        for second_value in sublist:
            counter = counter + 1
            if value - second_value > temp_max:
                temp_max = value - second_value

    print(f'I did {counter} iterations...')
    return temp_max


# my_max([5, 2, 3, 8, 1, 6]) = 6
def my_max(a_list):

    temp_max = 0
    temp_number = 0
    counter = 0
    for value in reversed(a_list):
        counter = counter + 1
        if value > temp_number:
            temp_number = value

        if temp_number - value > temp_max:
            temp_max = temp_number - value

    print(f'I did {counter} iterations...')
    return temp_max


if __name__ == '__main__':

    arr = [5, 2, 3, 8, 1, 6]
    print(my_max(arr))
