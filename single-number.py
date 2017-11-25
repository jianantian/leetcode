import datetime


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = nums[0]
    for x in nums[1:]:
        res ^= x
        return res
now = datetime.datetime.now()

# print singleNumber(l)
# print datetime.datetime.now() - now
