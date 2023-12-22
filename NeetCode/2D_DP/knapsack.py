def main(profits, weights, capacity):
    profits.insert(0,0)
    weights.insert(0,0)
    table = [[0 for j in range(capacity+1)] for i in range(len(profits)+1)]

    for i in range(len(table)):
        for w in range(len(table[0])):
            if i==0 or j==0:
                continue

            elif weights[i] <= w:
                table[i][w] = max(table[i-1][w], table[i-1][w-weights[i]]+profits[i])
            else:
                table[i][w] = table[i-1][w]

    
    i, w = len(profits)-1, capacity
    res = [0] * len(profits) - 1

    while i>0 and w>0:
        if table[i][w] != table[i-1][w]:
            res[i] = 1 #take this object
            w -= w[i] #remaining weights
            i -= 1
        else:
            i -= 1 #dont want this object
    

    return res