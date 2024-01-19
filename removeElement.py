def removeElement(nums, val) -> int:
    index = 0
    length = 0
    while index < len(nums):
        if nums[index] == val:
            nums.pop(index)
            continue
        index += 1
        length += 1
    return length


nums = [3, 2, 2, 3]
val = 3
ans = removeElement(nums, val)
print(ans, nums)
