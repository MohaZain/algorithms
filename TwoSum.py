# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Ref: https://leetcode.com/problems/two-sum/
# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
def twoSum(nums, target):
    arr=[]
    for i in range(len(nums)-1):
        for j in range(i,len(nums)):
            if nums[i] + nums[j] == target:
                # print(i,'>>>>>>',j)
                arr.append(i)
                arr.append(j)
    return arr

# ---------------------Test----------------------------
nums = [4,7,11,15,3,6]
target =  9
print('[4,5] >>',twoSum(nums,target))
