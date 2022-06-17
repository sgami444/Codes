#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        #Making a dictionary that stores integers and their frequency, where key is integer and value is their frequency in array
        for i in range(len(nums)):
            d[nums[i]] = (d[nums[i]]+1) if (nums[i] in d) else 1
        
        #Subtracting each value of array from the target and checking if the result exists in the array
        #if the result exists in the array, return their index, to not get confused between two indixes, make one of the index Null
        for i in d:
            check = target - i
            d[i] -= 1
            if check in d and d[check]>0:
                index1 = nums.index(check)
                nums[nums.index(check)]=None
                return [index1, nums.index(i)]
            d[i]+=1

obj = Solution()
arr = [1,2,3,6,3]
target = 3
print(obj.twoSum(arr, target))