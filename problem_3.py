def find_pivot_index(arr, start_index, end_index):
    left_index = start_index
    pivot_index = end_index
    pivot_value = arr[pivot_index]

    while left_index != pivot_index:
        left_value = arr[left_index]
        if arr[left_index] >= arr[pivot_index]:
            left_index += 1
            continue
        arr[left_index] = arr[pivot_index - 1]
        arr[pivot_index - 1] = pivot_value
        arr[pivot_index] = left_value
        pivot_index -= 1
    return pivot_index


def quick_sort_func(arr, start_index, end_index):
    if end_index <= start_index:
        return
    pivot_index = find_pivot_index(arr, start_index, end_index)

    quick_sort_func(arr, start_index, pivot_index - 1)
    quick_sort_func(arr, pivot_index + 1, end_index)


def quick_sort(arr):
    quick_sort_func(arr, 0, len(arr) - 1)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    quick_sort(input_list)
    x = 0
    y = 0
    for i, item in enumerate(input_list):

        if i % 2 == 0:
            x = x * 10 + item
        else:
            y = y * 10 + item
    print("x ==> {} y ==> {}".format(x, y))
    return [x, y]
    pass


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [531, 42]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], [0, 0]])
test_function([[1, 1, 1], [11, 1]])
test_function([[3, 2, 1], [31, 2]])

