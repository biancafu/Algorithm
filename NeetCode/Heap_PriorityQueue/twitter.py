#my solution, 27 min #70% speed 79% memory
class Twitter(object):

    def __init__(self):
        self.tweets = []
        self.followers = collections.defaultdict(list) #followers[followerID] = [list of followee]
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
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)