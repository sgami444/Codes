class Solution(object):
    def maxScore(self, cardPoints, k):
        
        # Sliding window 
        
        result = sum(cardPoints[:k])
        if len(cardPoints)<2:
            return result
        temp = result
        for i in range(1, k+1):
            temp = temp - cardPoints[k-i] + cardPoints[-i]
            result = temp if temp>result else result
        return result
