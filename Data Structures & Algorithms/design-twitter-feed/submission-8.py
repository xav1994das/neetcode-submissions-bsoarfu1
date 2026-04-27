import collections
import heapq
import time

class Twitter:
    def __init__(self):
        self.tweetlist = collections.defaultdict(list)
        self.following = collections.defaultdict(set)
        # Use a simple counter to guarantee order
        self.count = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        # Because of defaultdict, you don't need the 'if userId not in' check
        self.tweetlist[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> list:
        heap = []
        # Create a set of users to pull tweets from
        # Using a set here ensures the user is included without duplicates
        userlist = self.following[userId] | {userId}

        for user in userlist:
            # Safely get tweets (if any exist)
            for tweet in self.tweetlist.get(user, []):
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)

        arr = []
        while heap:
            arr.append(heapq.heappop(heap)[1])
        return arr[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        # A user shouldn't follow themselves in most test cases
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # .discard() handles the case where the followeeId isn't in the set
        if followerId in self.following:
            self.following[followerId].discard(followeeId)