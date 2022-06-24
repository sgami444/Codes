def groupAnagrams(strs):
    group = {}
    for i in strs:
        temp_str = "".join(sorted(list(i)))
        if temp_str not in group:
            temp_list = [i]
            group[temp_str] = temp_list
        else:
            temp_list = group[temp_str]
            temp_list.append(i)
            group[temp_str] = temp_list
        # print("Group: " + str(group) + "\ntemp str: " + str(temp_str))

    return group.values()


strs = ["bat","tab","cat","tac","act","car","rat","at","ta","do"]
print(groupAnagrams(strs))