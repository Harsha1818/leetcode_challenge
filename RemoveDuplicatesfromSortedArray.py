class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        final = List[int]
        count=1

        for i in range (1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[count] = nums[i]
                count=count+1


        return count
    




        