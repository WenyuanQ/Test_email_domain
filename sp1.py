
class Solution:
    def sift(self, nums, low, high):
        i, j = low, 2 * low
        tmp = nums[i]
        while j <= high:
            if j < high and nums[j] < nums[j + 1]:
                j += 1
            if tmp < nums[j]:
                nums[i] = nums[j]
                i = j
                j = 2 * i
            else: break
        nums[i] = tmp
 
    def findKthLargest(self, nums, k):
        n = len(nums)
        for i in range(n//2, -1, -1):
            self.sift(nums, i, n-1)
        for i in range(n-1, n-1-k, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.sift(nums, 0, i - 1)
        return nums[i]
 
 
if __name__ == '__main__':
    nums, k = [1,3,5,9,100,28,12], 3
    # nums, k = [100, 21, 88, 55, 21, 9, 3], 6
    solu = Solution()
    print(solu.findKthLargest(nums, k))
