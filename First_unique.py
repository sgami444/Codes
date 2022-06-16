#First unique character in a string

def first_unique(check):
    d = {}
    for i in check:
        if i in d:
            d[i] = 1
        else:
            d[i] = 0
    print(d)
    idx = 0
    for j in check:
        if d[j]==0:
            return idx
        idx += 1
    return -1

#Enter the string here
print(first_unique("susup"))