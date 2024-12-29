class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i=0

        while i<len(nums):
            j=0
            i = i+1
            while j<len(nums):

                if j==i:
                    j = j+1
                    pass
                else:
                    value = nums[i] + nums[j]
                    if value==target:
                        required_list= [i,j]
                        return required_list
                    else:
                        j = j+1

         