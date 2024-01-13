def isPalindrome( x: int):
    newX = str(x)
    newX =  list(newX)
    Y =newX[::-1]

    print(newX)
    print( Y)
    return newX == Y

ans = isPalindrome(1241)
print(ans)


"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x

"""