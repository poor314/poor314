class Solution(object):
    def heapify(self,nums,size,i):
        l=2*i+1 #左子節點
        r=2*i+2 #右子節點
        largest=i #i=最大

        if l<size and nums[l]>nums[largest]:
            largest=l

        if r<size and nums[r]>nums[largest]:
            largest=r

        if largest!=i:
            nums[i],nums[largest]=nums[largest],nums[i] #交換

            self.heapify(nums,size,largest)
    def heap_sort(self,nums):
        size=len(nums)

        for i in range(size,-1,-1):
            self.heapify(nums,size,i)

        for i in range(size-1,0,-1):
            nums[i],nums[0]=nums[0],nums[i] #交換

            self.heapify(nums,i,0)

nums=[12,1,13,5,26,7,33]
Solution().heap_sort(nums)
print(nums)
