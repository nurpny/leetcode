class Solution:
    def maxProductNaive(self, nums):
        # O(n^2 time)
        if not nums: return 0
        max_prod = nums[0]
        length = len(nums)
        for i in range(length):
            curr_prod = nums[i]
            max_prod = max(max_prod, curr_prod)
            for j in range(i + 1, length):
                curr_prod *= nums[j]
                max_prod = max(max_prod, curr_prod)
        return max_prod

    def maxProductDynamic(self, nums):
        #O(n) time
        max_pos_prod = 1
        max_neg_prod = 1
        max_prod = float("-inf")
        for num in nums:
            max_prod = max(num, max_prod)
            if (num > 0):
                max_pos_prod *= num
                max_prod = max(max_prod, max_pos_prod)
                if max_neg_prod < 0:
                    max_neg_prod *= num
            elif (num < 0):
                prev_pos, prev_neg = max_pos_prod, max_neg_prod
                if max_neg_prod < 0:
                    max_pos_prod = prev_neg * num
                    max_prod = max(max_prod, max_pos_prod)
                else:
                    max_pos_prod = 1
                max_neg_prod = prev_pos * num
            else:
                max_neg_prod = 1
                max_pos_prod = 1
        return max_prod

    def maxProductDynamic2(self, nums):
        # O(n) time. Same concept as above, cleaner code.
        if not nums: return 0
        acc_max = nums[0]
        acc_min = nums[0]
        max_prod = acc_max
        for i in range (1, len(nums)):
            curr = nums[i]
            if curr == 0:
                acc_min = 0
                acc_max = 0
            else:
                curr_min = curr * acc_min
                curr_max = curr * acc_max
                acc_min = min(curr, curr_min, curr_max)
                acc_max = max(curr, curr_min, curr_max)
            max_prod = max(acc_max, max_prod)
        return max_prod

solution = Solution()
print(solution.maxProductDynamic([2,3,-2,4]))
print(solution.maxProductDynamic2([2,3,-2,4]))
