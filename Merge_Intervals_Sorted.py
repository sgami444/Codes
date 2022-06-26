def merge(intervals):
    if len(intervals) < 2:
        return intervals
    intervals.sort()
    merged = [intervals[0]]
    # print("sorted: "+str(intervals))
    for i in range(1, len(intervals)):
        # print("Current: " + str(intervals[i])+"\tMerged: "+str(merged))
        # print(intervals[i][0])
        # print(merged[-1][1])
        if intervals[i][1]<=merged[-1][1]:
            # print("Continued")
            continue
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = intervals[i][1]
        else:
            merged.append(intervals[i])
    return merged


intervals = [[1,4],[4,5]]
print(merge(intervals))