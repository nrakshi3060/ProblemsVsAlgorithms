import random


def get_min_max_func(arr, start_index, end_index):
    if start_index == end_index:
        return arr[end_index], arr[start_index]

    if start_index == end_index - 1:
        if arr[start_index] > arr[end_index]:
            return arr[end_index], arr[start_index]
        else:
            return arr[start_index], arr[end_index]

    mid_index = (start_index + end_index) // 2
    min, max = get_min_max_func(arr, start_index, mid_index - 1)
    min_right, max_right  = get_min_max_func(arr, mid_index, end_index)

    if max < max_right:
        max = max_right

    if min_right < min:
        min = min_right

    return min, max


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    return get_min_max_func(ints, 0, len(ints) - 1)


pass

## Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print(l)
print(get_min_max(l))
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
