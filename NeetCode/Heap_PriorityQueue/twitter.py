#my solution, 27 min #70% speed 79% memory (ranges big for speed goes to 93%)
#neetcode's solution, 90% speed 99% memory (ranges big for speed as well can go down to 30 something %)
#neetcode solution very good (range from 93-70% speed 78% memory)
class Twitter(object):

    def __init__(self):
        #we are using a map for tweets instead of just a big list with every tweet
        #we will then heapify the tweets from the ppl we follow and find the 10 most recent ones
        #this can be more efficient depending on the case because we only have to go through the list of tweets from certain followers, however, if we have a lot of followers to go through, it can take more time
        self.tweets = collections.defaultdict(list) 
        self.followers = collections.defaultdict(set) #followers[followerID] = [list of followee]
        #use heap to track tweets
        self.num = 0

    def postTweet(self, userId, tweetId):
        #compose a new tweet with tweetID (unique)
        #max heap (bigger number, more recent)
        self.tweets[userId].append([-self.num, tweetId])
        self.num += 1
        

    def getNewsFeed(self, userId):
        #10 most recent tweetID's from ppl who the user follows or by the user themselves
        #order: new -> old
        output = []
        heap = [ ]
        self.followers[userId].add(userId) #add itself to get their own tweets
        
        #get tweets from the user's following
        for follower in self.followers[userId]:
            if self.tweets[follower]:  #if there are tweets for this person
                index = len(self.tweets[follower]) - 1
                count, tweetId = self.tweets[follower][index]
                heap.append([count, tweetId, follower, index - 1]) #pass in the next tweet index 
        heapq.heapify(heap)
        while heap and len(output) < 10:
            count, tweetId, follower, index = heapq.heappop(heap)
            output.append(tweetId)
            if index >= 0: 
                count, tweetId = self.tweets[follower][index]
                heapq.heappush(heap, [count, tweetId, follower, index - 1])
                #it is confusing here, we are adding the current tweet with NEXT index, so we need include index == 0 since we are pushing to the heap with info of the tweet that occured at index == 0 but we are passing in index - 1 for next, so when we append at top, it is tweet at index == 0, and after we will see next index < 0 so we don't push it in heap again
                
        return output

        



    def follow(self, followerId, followeeId):
        #user with followerId follows the followeeID user
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class Twitter(object):
    #neetcode: same for followers, for tweets, use a hashmap: userId -> list of [-count(same as my num), tweetId]
    #when finding newsfeed, have all the tweet lists from the followees, and use max heap to find most recent

    #time complexity of using a heap vs not using a heap 
    def __init__(self):
        self.tweets = []
        self.followers = collections.defaultdict(list) #followers[followerID] = [list of followeeId]
        #this means that when we add O(1) but when we unfollow it would be O(n), how do we improve this? use a set (O(1) removal)
        #better approach: followerId -> hashset(followeeIds)
        #use heap to track tweets
        self.num = 0

    def postTweet(self, userId, tweetId):
        #compose a new tweet with tweetID (unique)
        #max heap (bigger number, more recent)
        heapq.heappush(self.tweets, [-self.num, [userId, tweetId]])
        self.num += 1
        

    def getNewsFeed(self, userId):
        #10 most recent tweetID's from ppl who the user follows or by the user themselves
        #order: new -> old
        output = []
        copy = self.tweets[:]
        while copy and len(output) < 10:
            tweet = heapq.heappop(copy)
            if tweet[1][0] in self.followers[userId] or tweet[1][0] == userId:
                output.append(tweet[1][1])
        
        return output
                
        

    def follow(self, followerId, followeeId):
        #user with followerId follows the followeeID user
        self.followers[followerId].append(followeeId)
        

    def unfollow(self, followerId, followeeId):
        #we can use `discard` to remove elements even if it is not in the set without throwing error
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        

#me understnading from neetcode's solution: 63-17% speed 78% memory
#however, neetcode didn't just heapify all the tweets, he did something else to make it more effificent
#he only adds last tweets from all followees at first to the heap
#he push followeeId AND index in heap as well, using those info, he then adds the next new tweet to the heap
class Twitter(object):

    def __init__(self):
        #we are using a map for tweets instead of just a big list with every tweet
        #we will then heapify the tweets from the ppl we follow and find the 10 most recent ones
        #this can be more efficient depending on the case because we only have to go through the list of tweets from certain followers, however, if we have a lot of followers to go through, it can take more time
        self.tweets = collections.defaultdict(list) 
        self.followers = collections.defaultdict(set) #followers[followerID] = [list of followee]
        #use heap to track tweets
        self.num = 0

    def postTweet(self, userId, tweetId):
        #compose a new tweet with tweetID (unique)
        #max heap (bigger number, more recent)
        self.tweets[userId].append([-self.num, tweetId])
        self.num += 1
        

    def getNewsFeed(self, userId):
        #10 most recent tweetID's from ppl who the user follows or by the user themselves
        #order: new -> old
        output = []
        #get the tweets by the user itself
        tweets = self.tweets[userId][:] #mistake!! this is modifying the list saved, we need to make a copy of it
       
        print(self.tweets[userId])
        #get tweets from the user's following
        for follower in self.followers[userId]:
            if self.tweets[follower]:  
                tweets.extend(self.tweets[follower])
        
        heapq.heapify(tweets)

        while tweets and len(output) < 10:
            output.append(heapq.heappop(tweets)[1])
        
        return output

        



    def follow(self, followerId, followeeId):
        #user with followerId follows the followeeID user
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)