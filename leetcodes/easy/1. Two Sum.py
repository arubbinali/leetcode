#main
class Solution(object):
    def twoSum(self, nums, target):
        numbers = {}
        for index, number in enumerate(nums):
            if (target - number) in numbers: return [index, numbers[(target - number)]]
            numbers[number] = index
        return None

#other
class Solution(object):
    def twoSum(self, nums, target):
        numbers = {}
        for index, number in enumerate(nums):
            dif = target - number
            if dif in numbers: return [index, numbers[dif]]
            numbers[number] = index
        return None

class Solution(object):
    def twoSum(self, nums, target):
        outList = []
        for first in range(len(nums)):
            for second in range(len(nums)):
                if first != second:
                    if nums[first] + nums[second] == target:
                        firstnum, secondnum = first, second
        outList.append(secondnum); outList.append(firstnum)
        return outList