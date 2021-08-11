# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Ref: https://leetcode.com/problems/two-sum/
# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
def twoSum(nums, target):
    dict_num = {}
    arr = []
    for i,num in enumerate(nums):
        if target - num in dict_num:
            arr.append(i)
            arr.append(dict_num[target - num])

        dict_num[num] = i
    return arr

# ---------------------Test----------------------------
nums = [4,7,11,15,3,6]
target =  9
# print('[4,5] >>',twoSum(nums,target))
# -----------------------------------------------------
nums = [3,2,4]
target =  6
print('[2,1] >>',twoSum(nums,target))
