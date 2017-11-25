# coding:utf8


def maximum_subarray(nums):
    """动态规划的想法"""
    maxsum = 0
    res = 0
    if max(nums) < 0:
        return max(nums)
    else:
        for i in xrange(len(nums)):
            res += nums[i]
            if res > maxsum:
                maxsum = res
            elif res < 0:
                res = 0
        return maxsum

l = [1,2,-3,4,-5,2,3]
print maximum_subarray(l)