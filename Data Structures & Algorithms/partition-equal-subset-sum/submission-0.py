class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        dp=[False]*(target+1) #使用前面已经处理过的数字，是否可以凑出和 j
        nextDp=[False] *(target+1) #加入当前 nums[i] 后，是否可以凑出 j。

        dp[0]=True
        for i in range(len(nums)):
            for j in range(1,target+1):
                if j>=nums[i]:
                    nextDp[j]=dp[j] or dp[j-nums[i]]
                else:
                    nextDp[j]=dp[j]
            dp,nextDp=nextDp,dp #新旧状态交换，节约资源
        return dp[target]