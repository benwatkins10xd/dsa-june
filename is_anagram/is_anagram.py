# Naive solution 

def naive_is_anagram(s: str, t: str) -> bool:    
    # Check if lengths of the strings are different
    if len(s) != len(t):
        return False
    
    # Convert strings to lists
    str1_list = list(s)
    str2_list = list(t)
    
    # Sort the lists
    str1_list.sort()
    str2_list.sort()
    
    # Compare the sorted lists
    for i in range(len(str1_list)):
        if str1_list[i] != str2_list[i]:
            return False
    
    return True

# Hashmapped solution

def faster_is_anagram(s: str, t: str) -> bool:
    # use two hashmaps for each string
    # char : int
    sMap = {}
    tMap = {}

    # go through each string and see how many times
    # each character occurs
    for i in s:
        sMap[i] = sMap.get(i, 0) + 1
    
    for i in t:
        tMap[i] = tMap.get(i, 0) + 1

    # compare the maps
    if sMap == tMap:
        return True
    else:
        return False
