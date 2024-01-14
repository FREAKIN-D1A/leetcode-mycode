# def longestCommonPrefix(strs):
#     result = strs[0]
#     for string in strs:
#         if len(string) < len(result):
#             result = result[: len(string)]
#             # print("the result after trimming is :", result)
#         for index in range(len(result)):
#             if result[index] != string[index]:
#                 # result[index] = ""
#                 # result = result.replace(result[index], "", 1)
#                 result = result[:index]
#                 break

#             # print("the result after  if result[index] != string[index]: is :", result)
#     print(result)
#     return result


def longestCommonPrefix(v) -> str:
    ans = ""
    v = sorted(v)
    first = v[0]
    last = v[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans


ans = longestCommonPrefix(["flower", "flow", "flight"])
print(ans)
