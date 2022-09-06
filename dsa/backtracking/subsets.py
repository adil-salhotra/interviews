"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
def subsets(nums):
    ans = list()
    subset = list()

    def dfs(index):
        if index == len(nums):
            ans.append(subset.copy())
            return

        subset.append(nums[index])
        dfs(index+1)

        subset.pop()
        dfs(index+1)
    
    dfs(0)
    return ans