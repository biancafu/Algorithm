
def minWindow(s, t):
    """
    on the right track but only used 1 dict
    instead of that, use 2 so we have a reference to check with
    using match to count the number of matching characters we need
    only increment the count when we have the right amount of characters 
    *made the mistake of incrementing when we have >= than amount of characters, but we can only increment when we have exactly the same
    since even when its more than the amout of characters we need, we already incrmenet the matching character previously
    we will decrease the match number after in the while loop where we keep incrementing left counter until match > count
    this gaurantees us to keep shortening the length until we cannot (when we don't have enough matching characters)
    """
#create 2 dictionary: 1 that counts the ongoing characters in s, 1 that counts characters in t
#create 2 counters, match: how many to match to update our shortest string, count: how many matches we currently have
#when checklist[char] == seen[char]: we update count (+= 1)
#when match == count: we update shortest length (min) then we do a while loop to increment left counter until count < match where we find a char in t

#we will create 2 dict: 1 is the one that stores the number of characters we have from t, the other is to keep track of the current characters from s
#we will have 2 numbers: 1 is the number of matches we need to satisfy the substring, 2 is the counter for how many number of matches we currently have
#when an amount of character the window has from s is matching the ones required by t, we will increase the count number
#when match == count, this means we have all characters to form a substring
    checklist, seen = {}, {}
    
    for char in t:
        if char not in checklist:
            checklist[char] = 1
        else:
            checklist[char] += 1
    
    match = len(checklist)
    l, count = 0, 0
    minlength = float("inf")
    index = []

    for r, char in enumerate(s):
        if char in checklist:
            seen[char] = seen.get(char, 0) + 1

            if seen[char] == checklist[char]:
                count += 1
        
        while match == count:
            if r - l + 1 < minlength:
                index = [l, r]
                minlength = r - l + 1
            if s[l] in checklist:
                seen[s[l]] -= 1
                if checklist[s[l]] > seen[s[l]]:
                    count -= 1
            l += 1
    
    return "" if minlength == float("inf") else s[index[0] : index[1] + 1]

            
a = minWindow("ADOBECODEBANC", "ABC")
print(a)


        
            

