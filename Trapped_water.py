def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # Find maxLeftHeight and maxRightHeight for all the elements in the array and store their values in another array
    # waterTrapped += min(maxLeft, maxRight) - height[i]    
    leftMax=[]
    leftMax.append(0) # leftMax height of 1st element is zero
    result = 0
    # print("Height: " + str(height))

    for i in range(1, len(height)):
        leftMax.append(height[i-1] if height[i-1]>leftMax[i-1] else leftMax[i-1])
    # print("leftMax: " + str(leftMax))

    rightMax=[0]*len(height)
    for i in range(len(height)-2, -1, -1):
        rightMax[i] = height[i+1] if height[i+1]>rightMax[i+1] else rightMax[i+1]
    # rightMax.append(0)
    # print("rightMax: " + str(rightMax))
    

    for i in range(len(height)):
        result += min(leftMax[i], rightMax[i]) - height[i] if (min(leftMax[i], rightMax[i]) - height[i])>0 else 0
    return result


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))