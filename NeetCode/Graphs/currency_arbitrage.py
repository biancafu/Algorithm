#use Bellman Ford's algorithm: used to find shortest path, but we want max amount so we will -*log(Rate) values

#create a weighted graph using log(rate) as their weight

#check through the currency with graph and if sum(log(rate)) > 0 means there is a arbitrage or < 0 means arbitrage (from other side i think)

#if there is a negative weighted cycle -> bellman ford wont work
