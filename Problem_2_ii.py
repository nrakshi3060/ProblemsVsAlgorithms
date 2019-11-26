def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return rotated_array_search_func(input_list, 0, len(input_list) - 1, number)


def rotated_array_search_func(input_list, start_index, end_index, target):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2

    if input_list[mid_index] == target:
        return mid_index

    if input_list[start_index] <= input_list[mid_index]:

        if input_list[start_index] <= target <= input_list[mid_index]:
            return rotated_array_search_func(input_list, start_index, mid_index - 1, target)

        return rotated_array_search_func(input_list, mid_index + 1, end_index, target)
    else:
        if input_list[mid_index] <= target <= input_list[end_index]:
            return rotated_array_search_func(input_list, mid_index, end_index, target)
        return rotated_array_search_func(input_list, start_index, mid_index - 1, target)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
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
