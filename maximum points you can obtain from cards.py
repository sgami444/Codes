class Solution(object):
    def maxScore(self, cardPoints, k):
        
        # O(n^2) sum(n elements) is O(n) too
        
        result = sum(cardPoints[:k])
        if len(cardPoints)<2:
            return result
        for i in range(1, k+1):
            temp = sum(cardPoints[:k-i]) + sum(cardPoints[-i:])
            result = temp if temp>result else result
        return result
