'''
Skip to:

Header Navigation
Side Navigation
HackerRank
R
B
Crazy Ledger (Official Template - Test)
Bianca
Rachel Ye
Crazy Ledger (Official Template - Test)
Description
Given a set of transactions between users.
Each transaction denotes the payer-> payee relation. The amount paid is in terms of percentage.

 

A->B 20%

 

This means A paid 20% of whatever he/she had to B.

 

Input:

A has $100

 

List of transactions:

 

A->B 20%

 

A->C 40%

 

B->D 30%

 

C->D 50%

 

C->F 20%

 

B->E 50%

 

D->E 25%

 

F->G 10%

 

E->C 50%

 

Part 1) Print final balances of all users.

 

Expected Output:

 

{'A': 48.0, 'B': 7.0, 'C': 19.05, 'D': 16.5, 'F': 2.88, 'E': 6.25, 'G': 0.32}

Python 2
15161718192021222324252627282930313233141312113435109873637


from collections import defaultdict
class CrazyLedger():
    def __init__ (self, transactions):
        self.transactions = transactions
        self.finishedTransaction = defaultdict(int)
        self.finishedTransaction['A'] = 100
        self.copy = [self.finishedTransaction.copy()]
        
…a.delete(3)
print(a.finishedTransaction)
    
    
# res = main([['A','B', 20], ['A','C',40], ['B','D',30], ['C','D',50], ['C','F',20], ['B','E',50], ['D','E',25], ['F','G',10], ['E','C',50]], 100)

# print(res)
Line: 44 Col: 13

Input / Output

Test Cases

Console
Runtime Error (Compilation Successful).
Input
Enter the raw STDIN input
Error (stderr)
Traceback (most recent call last):
  File "Solution.py", line 36, in <module>
    a.calculate([['A','B', 20], ['A','C',40], ['B','D',30], ['C','D',50], ['C','F',20], ['B','E',50], ['D','E',25], ['F','G',10], ['E','C',50]])
  File "Solution.py", line 15, in calculate
    copy = self.copy.copy()
AttributeError: 'list' object has no attribute 'copy'
Your Output (stdout)
No output to show
n, ``` n ```, , hint
'''

from collections import defaultdict
class CrazyLedger():
    def __init__ (self, transactions):
        self.transactions = transactions
        self.finishedTransaction = defaultdict(int)
        self.finishedTransaction['A'] = 100
        self.copy = [self.finishedTransaction.copy()]
        
    def calculate(self, transactions, start=None):
        if not start:
            start = self.finishedTransaction
        output = start.copy()
        copy = self.copy.copy()
        for transaction in transactions:
            send, to, percentage = transaction
            money = output[send]*(float(percentage)/100)
            print(money)
            output[send] -= money
            output[to] += money
            
            copy.append(output.copy()) 
        
        self.copy = copy
        self.finishedTransaction  = output
        

        
    def delete(self, n):
        prev = self.copy[n-1]
        self.calculate(self.transactions[n+1:], prev)
        
        
a = CrazyLedger([['A','B', 20], ['A','C',40], ['B','D',30], ['C','D',50], ['C','F',20], ['B','E',50], ['D','E',25], ['F','G',10], ['E','C',50]])
a.calculate([['A','B', 20], ['A','C',40], ['B','D',30], ['C','D',50], ['C','F',20], ['B','E',50], ['D','E',25], ['F','G',10], ['E','C',50]])
print(a.finishedTransaction)
a.delete(3)
print(a.finishedTransaction)
    
    
# res = main([['A','B', 20], ['A','C',40], ['B','D',30], ['C','D',50], ['C','F',20], ['B','E',50], ['D','E',25], ['F','G',10], ['E','C',50]], 100)

# print(res)