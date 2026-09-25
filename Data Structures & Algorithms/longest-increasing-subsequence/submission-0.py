class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        memo=[-1]*n #用来记录从nums[i]开始，最长递增子序列有多长

        def dfs(i): # 以nums[i]作为第一个元素时，最长递增子序列的长度
            if memo[i]!=-1:
                return memo[i]
            LIS=1 #必须选择nums[i]，即使后面没有任何更大的，也可以选自己
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    LIS=max(LIS,1+dfs(j))
            memo[i]=LIS
            return LIS
        return max(dfs(i) for i in range(n))