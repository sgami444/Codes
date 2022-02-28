def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[]
        for i in range(n):
            dp.append(-1)
        dp[n-1] = 1
        dp[n-2] = 2

        i=n-3
        while i>=0:
            dp[i]=dp[i+1]+dp[i+2]
            i=i-1
        return 1 if (n==1) else dp[0]
