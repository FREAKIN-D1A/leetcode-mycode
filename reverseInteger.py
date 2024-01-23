def reverse(self, x):
    if x < 0:
        res = -1 * int(str(-x)[::-1])
    else:
        res = int(str(x)[::-1])
    if res > 2**31 or res < -(2**31):
        return 0
    return res


# Example usage:
print(reverse(123))  # Output: 321
print(reverse(-123))  # Output: -321
print(reverse(120))  # Output: 21

"""

def reverse(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    # Handle the sign of the integer
    sign = 1 if x >= 0 else -1
    x = abs(x)

    # Reverse the digits
    reversed_x = 0
    while x != 0:
        digit = x % 10
        x //= 10

        # Check for integer overflow
        if reversed_x > (INT_MAX - digit) // 10:
            return 0

        reversed_x = reversed_x * 10 + digit

    return sign * reversed_x

"""
