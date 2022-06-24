def merge(intervals):
    if len(intervals)<2:
        return intervals
    i = 0
    while True:
        j = 0
        print("Before EVERYthing \ti: "+str(i)+"\tj: "+str(j)+"\tintervals: "+str(intervals))
        if i>=len(intervals):
            return intervals
        while True:
            if j==i:
                j+=1
            print("Before things \ti: "+str(i)+"\tj: "+str(j)+"\tintervals: "+str(intervals))
            if i>= len(intervals):
                return intervals
            if j>=len(intervals):
                i+=1
                print("j>=len(intervals) \ti: "+str(i)+"\tj: "+str(j)+"\tintervals: "+str(intervals))
                break
            print("Overlaping resuls: "+ str(isOverlaping(intervals[i],intervals[j])))
            if isOverlaping(intervals[i], intervals[j]):
                print("Overlapping before \ti: "+str(i)+"\tj: "+str(j)+"\tintervals: "+str(intervals))
                intervals.append(isOverlaping(intervals[i], intervals[j]))
                intervals.pop(j)
                intervals.pop(i)
                i=0
                j=0
                print("Overlapping after \ti: "+str(i)+"\tj: "+str(j)+"\tintervals: "+str(intervals))
            else:
                j+=1



def isOverlaping(interval1, interval2):
    if interval1[0]<=interval2[0] and interval1[1]>=interval2[1]:
        return interval1
    elif interval1[0]>=interval2[0] and interval1[1]<=interval2[1]:
        return interval2
    elif interval1[0]<=interval2[0] and interval1[1]>=interval2[0] and interval1[1]<=interval2[1]:
        return [interval1[0], interval2[1]]
    elif interval2[0]<=interval1[0] and interval2[1]>=interval1[0] and interval2[1]<=interval1[1]:
        return [interval2[0], interval1[1]]
    else:
        return None


# if isOverlaping([0,16],[0,9]):
    # print("Overlapping: " + str(isOverlaping([0,16],[0,9])))


intervals = [[1,3],[0,2],[2,3],[4,6],[4,5],[5,5],[0,2],[3,3]]
print(merge(intervals))