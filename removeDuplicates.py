def removeDuplicates(nums) -> int:
    index = 1
    k = 0
    while index < len(nums):
        if nums[index] == nums[index - 1]:
            nums.pop(index)
            nums.append("_")
        elif nums[index] == "_":
            break
        else:
            k = k + 1
            index = index + 1
    return k + 1


nums = [1, 1, 2]
ans = removeDuplicates(nums)

print(ans)
print(nums)


# def removeDuplicates(nums) -> int:
#     k = 0
#     for index in range(1, len(nums)):
#         if nums[index] == nums[index - 1]:
#             nums[index] =
#         else:
#             k = k + 1
#     nums.sort()
#     return k


# nums = [1, 1, 2]
# ans = removeDuplicates(nums)

# print("ans")
# print(nums)
