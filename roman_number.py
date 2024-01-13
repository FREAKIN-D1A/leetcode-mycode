table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romanToInt(s: str) -> int:
    newS = list(s)
    sum = 0
    i = 0
    while i < len(newS) - 1:
        # print(newS[i])
        if table[newS[i]] < table[newS[i + 1]]:
            sum -= table[newS[i]]
        else:
            sum += table[newS[i]]
        i += 1
        # print(sum)
        pass
    sum += table[newS[-1]]
    # print(sum)
    return sum


romanToInt("XIV")
