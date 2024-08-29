"""
class Solution(object):
    def twoSum(self, nums, target):
        numbers = {}
        for index, number in enumerate(nums):
            dif = target - number
            if dif in numbers:
                return sorted([index, numbers[dif]])
            numbers[dif] = index
        return None
    """

def twoSum(nums, target):
        # Create a dictionary to store numbers and their corresponding indices
        number_map = {}

        # Loop through the array
        for i, num in enumerate(nums):
            # Calculate the difference between the target and the current number
            diff = target - num

            # Check if the difference already exists in the dictionary
            if diff in number_map:
                # If it exists, return the indices of the current number and the number that adds up to the target
                return [i, number_map[diff]]

            # If it doesn't exist, add the current number and its index to the dictionary
            number_map[num] = i
        
        # If no two numbers add up to the target, return None
        return None


print(twoSum([3, 2, 3], 6))

















































"""
class Solution(object):
    def twoSum(self, nums, target):
        outList = []
        for number in range(len(nums)-1):
            if nums[number] + nums[number + 1] == target:
                first = number; second = number + 1
        outList.append(second); outList.append(first)
        return outList

nums = [2,7,11,15]
target = 9



class Solution(object):
    def twoSum(self, nums, target):
        
        outList = []
        
        for first in range(len(nums)):
            for second in range(len(nums)):
                if first != second:
                    if nums[first] + nums[second] == target:
                        firstnum, secondnum = first, second
        
        outList.append(secondnum); outList.append(firstnum)
        return outList"""