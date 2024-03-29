def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    start_index = 0
    nex_pos_0  = 0
    nex_pos_2 = len(input_list) - 1
    count_iterations = 0

    while start_index <= nex_pos_2:
        if input_list[start_index] == 0:
            input_list[start_index] = input_list[nex_pos_0]
            input_list[nex_pos_0] = 0
            nex_pos_0 += 1
            start_index += 1
        elif input_list[start_index] == 2:
            input_list[start_index] = input_list[nex_pos_2]
            input_list[nex_pos_2] = 2
            nex_pos_2 -= 1
        else:
            start_index += 1

        count_iterations += 1
    print("Iterations count ==> {} Length of Array {}".format(count_iterations, len(input_list)))
    return input_list
    pass


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
