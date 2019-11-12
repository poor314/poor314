class Solution(object):
    def merge_sort(self,nums):

        #若A數列的長度小於等於1，則直接回傳A
        if len(nums)<=1:
            return nums

        #若A數列長度大於1，則開始進行切割(再細分成左數列跟右數列)
        if len(nums) > 1:
            center = len(nums)//2
            L = nums[:center]
            R = nums[center:]

            #重複呼叫左右數列
            self.merge_sort(L)
            self.merge_sort(R)

            #設定三個變數，分別為左數列、右數列、最後數列
            i=0
            j=0
            m=0

            #若左右數列的長度大於i、j，則將i、j兩數比較
            #i小於j的話，i放入m中，i跳到下一個繼續跟j做比較
            #j小於i的話，j放入m中，i跳到下一個繼續跟i做比較
            #i、j比較完之後，m都要跳到下一個，才能放置下一個值
            while len(L) > i and len(R) > j:
                if L[i] < R[j]:
                    nums[m] = L[i]
                    i=i+1
                else:
                    nums[m] = R[j]
                    j=j+1
                m=m+1

            #左數列剩下的值加到m、右數列剩下的值加到m
            while i < len(L):
                nums[m] = L[i]
                i=i+1
                m=m+1

            while j < len(R):
                nums[m] = R[j]
                j=j+1
                m=m+1

nums = [15,8,11,32,6,71,2,4,89]
Solution().merge_sort(nums)
print(nums)
