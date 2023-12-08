''' Given an array of integers a, your task is to count the number of pairs i and j (where 0 ≤ i < j < a.length), such that a[i] and a[j] are digit anagrams.

Two integers are considered to be digit anagrams if they contain the same digits. In other words, one can be obtained from the other by rearranging the digits (or trivially, if the numbers are equal). For example, 54275 and 45572 are digit anagrams, but 321 and 782 are not (since they don't contain the same digits). 220 and 22 are also not considered as digit anagrams, since they don't even have the same number of digits.

Example

For a = [25, 35, 872, 228, 53, 278, 872], the output should be solution(a) = 4.

There are 4 pairs of digit anagrams:

a[1] = 35 and a[4] = 53 (i = 1 and j = 4),
a[2] = 872 and a[5] = 278 (i = 2 and j = 5),
a[2] = 872 and a[6] = 872 (i = 2 and j = 6),
a[5] = 278 and a[6] = 872 (i = 5 and j = 6).
Input/Output

[execution time limit] 6 seconds (py)

[memory limit] 1 GB

[input] array.integer a

An array of non-negative integers.

Guaranteed constraints:
1 ≤ a.length ≤ 105,
0 ≤ a[i] ≤ 109.

[output] integer64

The number of pairs i and j, such that a[i] and a[j] are digit anagrams.
'''
#https://leetcode.com/discuss/interview-question/798439/robinhood-coding-question-1

#solution is correct, math equation is wrong
#combination of if n items with r items a group: C(n,r) = n!/(r! * (n-r)! )
# can use python math.factorial

from collections import defaultdict
import math

def solution(a):
    dict = defaultdict(int)
    
    

    for num in a:
        num = int(''.join(sorted(str(num))))
        dict[num] += 1
    res = 0
    print(dict)
    for k in dict:
        n = dict[k]
        if n >= 2:
            res += math.factorial(n)//(2*(math.factorial(n-2)))
    
    return res
    
    
        

