#https://leetcode.com/discuss/interview-question/933426/oa-uber

'''
You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its values. So you've decided to take matters into your own hands and implement your own hashmap in your new language that has the following operations:

insert x y - insert an object with key x and value y.
get x - return the value of an object with key x.
addToKey x - add x to all keys in map.
addToValue y - add y to all values in map.
To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).

Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.

Example

For queryType = ["insert", "insert", "addToValue", "addToKey", "get"] and query = [[1, 2], [2, 3], [2], [1], [3]], the output should be solution(queryType, query) = 5.

The hashmap looks like this after each query:

1 query: {1: 2}
2 query: {1: 2, 2: 3}
3 query: {1: 4, 2: 5}
4 query: {2: 4, 3: 5}
5 query: answer is 5
The result of the last get query for 3 is 5 in the resulting hashmap.



For queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"] and query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]], the output should be solution(queryType, query) = 6.

The hashmap looks like this after each query:

1 query: {1: 2}
2 query: {1: 4}
3 query: answer is 4
4 query: {1: 4, 2: 3}
5 query: {2: 4, 3: 3}
6 query: {2: 3, 3: 2}
7 query: answer is 2
The sum of the results for all the get queries is equal to 4 + 2 = 6.

Input/Output

[execution time limit] 4 seconds (py)

[memory limit] 1 GB

[input] array.string queryType

Array of query types. It is guaranteed that each queryType[i] is either "addToKey", "addToValue", "get", or "insert".

Guaranteed constraints:
1 ≤ queryType.length ≤ 105.

[input] array.array.integer query

Array of queries, where each query is represented either by two numbers for insert query or by one number for other queries. It is guaranteed that during all queries all keys and values are in the range [-109, 109].

Guaranteed constraints:
query.length = queryType.length,
1 ≤ query[i].length ≤ 2.

[output] integer64

The sum of the results for all get queries.
'''

#time exceeded limit first time
def solution(queryType, query):
    '''
    create ur own hashmap
    return sum of all "get" operations
    map = {
        1+1 = 2:2+2 = 4 => 2:4
        2+1 = 3:3+2 = 5 => 3:5
    }
    
    map = {
        2:3
        3:2
    }
    
    question, can we have get with values not existing in map? (no gaurantee) if can't find what happens?
    '''
    class CustomMap(object):
        def __init__(self):
            self.hashmap = {}
            self.ck = 0 #cumilative key
            self.cv = 0 #cumilative value
            
    
        def insert(self, x, y):
            self.hashmap[x - self.ck] = y - self.cv 
            #im not changing keys, when i adjust keys, i need to find original key value by -self.ck
            #if im inserting a new key when ck is not 0, im using key-ck for get function
            #therefore i need to store this new key as key-ck to get correct value
            
        def get(self, x):
            # return self.hashmap[x]
            return self.hashmap[x - self.ck] + self.cv
        
        def addToKey(self, x): 
            # new = {}
            # for key in self.hashmap:
            #     new[key+x] = self.hashmap[key]
            
            # self.hashmap = new
            if self.hashmap:
                self.ck += x
            
        def addToValue(self, y):
            # for key in self.hashmap:
            #     self.hashmap[key] += y
            if self.hashmap:
                self.cv += y
            
    getsum = 0
    m = CustomMap()
    for i in range(len(queryType)):
        type, input = queryType[i], query[i]
        if type == "insert":
            m.insert(input[0],input[1])
        elif type == "get":
            getsum += m.get(input[0])
        elif type == "addToKey":
            m.addToKey(input[0])
        elif type == "addToValue":
            m.addToValue(input[0])
    
    return getsum
    
    ans = 0
    hmap = {}
    ck = 0
    cv = 0
    for i in range(len(queryType)):
        cmd = queryType[i]
        quer = query[i]
        if cmd == "insert":
            key,val = quer[0],quer[1]
            hmap[key-ck]=val-cv
        elif cmd == "addToValue":
            k = quer[0]
            cv+=k
        elif cmd == "addToKey":
            k = quer[0]
            ck+=k
        else:
            k = quer[0]
            k-=ck
            val = hmap[k] + cv
            ans = ans + val
    return ans

        
        

