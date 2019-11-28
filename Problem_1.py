def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    start = 0
    end = number
    count = 0
    ans = 0
    while start <= end:
        count += 1
        mid = (start + end) // 2

        if (mid * mid) == number:
            return mid
        if (mid * mid) < number:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans


print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(3)) else "Fail")
print("Pass" if (2 == sqrt(8)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (6 == sqrt(37)) else "Fail")
