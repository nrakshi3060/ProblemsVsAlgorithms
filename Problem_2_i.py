def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1

    You are given a sorted array which is rotated at some random pivot point.

    Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

    """

    start_index = 0
    end_index = len(input_list) - 1

    if start_index > end_index:
        return -1

    pivot = find_pivot(input_list)

    if pivot == -1:
        return binary_search(input_list, start_index, end_index, number)

    if input_list[pivot] == number:
        return pivot
    elif input_list[0] <= number:
        return binary_search(input_list, start_index, pivot - 1, number)
    else:
        return binary_search(input_list, pivot + 1, end_index, number)
pass


def binary_search(arr, start_index, end_index, target):
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if arr[mid_index] == target:
            return mid_index
        elif target < arr[mid_index]:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

    return -1


def find_pivot(input_list):
    start_index = 0
    end_index = len(input_list) - 1

    while start_index < end_index:
        mid_index = (start_index + end_index) // 2

        if input_list[mid_index] > input_list[mid_index + 1]:
            return mid_index
        elif input_list[mid_index - 1] > input_list[mid_index]:
            return mid_index - 1
        elif input_list[start_index] >= input_list[mid_index]:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    r = rotated_array_search(input_list, number)
    l = linear_search(input_list, number)
    if l == r:
        print("Pass")
    else:
        print("Fail")


print("-------------Test Case 1---------------")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
print("-------------Test Case 2---------------")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
print("-------------Test Case 3---------------")
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
print("-------------Test Case 4---------------")
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
print("-------------Test Case 5---------------")
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
print("-------------Test Case 6---------------")
test_function([[1, 2, 3, 4, 6, 7, 8, 10], 10])
print("-------------Test Case 7---------------")
test_function([[], 10])

