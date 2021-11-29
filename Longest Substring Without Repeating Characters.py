def lengthOfLongestSubstring(s) :
    s_set = set()
    l = 0
    re = 0
    for i in range(len(s)): # using two loop
        while s[i] in s_set: #loop until not dulicate element in s[i]
            s_set.remove(s[l]) #remove left variable
            l += 1
            #print(l)
        s_set.add(s[i])
        #print(s_set)
        re = max(re,i-l + 1)
    return re






a1 = "abcabcbb"
# Output: 3
a2 = "bbbbb"
# Output: 1
a3 = "pwwkew"
# Output: 3
a4 = ""
# Output: 0
print(lengthOfLongestSubstring(a1))
#print(lengthOfLongestSubstring(a2))
#print(lengthOfLongestSubstring(a3))
#print(lengthOfLongestSubstring(a4))