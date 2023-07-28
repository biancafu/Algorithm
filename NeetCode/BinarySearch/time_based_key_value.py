from collections import defaultdict
"""
~45 min?
was unable to solve with correct leetcode solution 
BUT it seemed like there was some issue with leetcode compiler since it worked on vscode (the wrong case showed on leetcode)
overall, I understood the question properly and executed it in the right direction
it is not a hard question to solve, I should be able to finish it sooner without difficulty
"""
class TimeMap(object):

    def __init__(self):
        self.mapping = defaultdict(dict)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.mapping[key][timestamp] = value

        
        
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
       """
        if not self.mapping[key]:
            return ""
        keys = list(self.mapping[key].keys())

        low = 0
        high = len(keys) - 1
        res = ""
        while low <= high:
            mid = (low + (high)) // 2
            if keys[mid] <= timestamp:
                res = self.mapping[key][keys[mid]]
                low = mid + 1
            else:
                high = mid - 1
            # if timestamp <= keys[mid]:
            #     return self.mapping[key][keys[mid]]
            # elif keys[mid] > timestamp:
            #     high = mid - 1
            # else:
            #     res = self.mapping[key][keys[mid]]
            #     low = mid + 1

        return res

class TimeMap_NeetCode(object):
#Neetcode uses a list instead of dict inside of the mapping
    def __init__(self):
        self.mapping = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.mapping[key].append([value, timestamp])

        
        
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
       """
        if not self.mapping[key]:
            return ""

        timestamps = self.mapping[key]
        low = 0
        high = len(timestamps) - 1
        res=""
        while low <= high:
            mid = (low + (high)) // 2
            if timestamps[mid][1] <= timestamp:
                res = timestamps[low][0]
                low = mid + 1
            else:
                high = mid - 1
        return res

        #this reduces the memory used, since we are returning when the time == timestamps and not continuing the search
        # while low <= high:
        #     mid = (low + (high)) // 2
        #     if timestamps[mid][1] == timestamp:
        #         return timestamps[low][0]
        #     elif timestamps[mid][1] < timestamp:
        #         res = timestamps[low][0]
        #         low = mid + 1
        #     else:
        #         high = mid - 1

        # return res
"""
Timemap = {
    key: {time: value}
}
"""

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
instruction = ["TimeMap","set","set","get","set","get","set","set","get","set","get","set","get","set","get","set","get","get","get","get","get","get","set","set","set","get","get","set","set","get","set"]
input = [[],["rtzoj","kuexwze",1],["xcywxndnz","herqmazp",2],["xcywxndnz",3],["rtzoj","dgpguflin",4],["xcywxndnz",5],["dgpguflin","lvrexco",6],["xcywxndnz","dgpguflin",7],["xcywxndnz",8],["rtzoj","wxqixmxs",9],["xcywxndnz",10],["kuexwze","lvrexco",11],["dgpguflin",12],["lvrexco","wxqixmxs",13],["xcywxndnz",14],["herqmazp","vjfhio",15],["dgpguflin",16],["herqmazp",17],["herqmazp",18],["rtzoj",19],["herqmazp",20],["herqmazp",21],["kuexwze","vjfhio",22],["dgpguflin","qrkihrb",23],["kuexwze","dgpguflin",24],["rtzoj",25],["dgpguflin",26],["herqmazp","rtzoj",27],["lvrexco","iztpo",28],["lvrexco",29],["kuexwze","lvrexco",30]]
result = []
for i in range(len(input)):
    if instruction[i] == "TimeMap":
        result.append(None)
    elif instruction[i] == "set":
        obj.set(input[i][0],input[i][1],input[i][2])
        result.append(None)
    else:
        param_2 = obj.get(input[i][0],input[i][1])
        result.append(param_2)

print(result)