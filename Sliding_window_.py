#Find min no of swaps to bring all elements less than equal to k together

arr = [2, 7, 9, 5, 8, 7, 4]
k = 6

def together(arr, k):
    cnt=0
    for i in arr:
        cnt = cnt + 1 if i <= k else cnt + 0
        # print("i: " + str(i) + "\ncnt: " + str(cnt))
    # print("pointer: " + str(cnt))
    result = 0
    for i in range(0, cnt):
        result = result + 1 if arr[i] > k else result
    # print("i: " + str(i) + "\n")
    temp = result
    while i < len(arr)-1:
        i += 1
        if arr[i] > k:
            temp += 1
        if arr[i-cnt] > k:
            temp -= 1
        result = temp if temp < result else result
    return result

print(together(arr, k))