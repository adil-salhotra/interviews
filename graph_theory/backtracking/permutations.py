"""
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
"""
def permute(nums):
    output = list()

    if len(nums) == 1:
        return nums[:]


    num = nums.pop(0)

    for index in range(len(nums)):
        perms = permute(nums)

        for perm in perms:
            perm.append(num)
    
    output.extend(perm)
    nums.append(num)
    return output