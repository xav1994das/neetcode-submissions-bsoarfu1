import collections
import time
import heapq
class Twitter:

    def __init__(self):
        self.following=collections.defaultdict(set)
        self.tweetlist=collections.defaultdict(list)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        self.tweetlist[userId].append((self.timer,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users=[userId]
        heap=[]
        for u in self.following[userId]:
            users.append(u)
        for u in users:
            for t in self.tweetlist[u]:
                heapq.heappush(heap,t)
                if len(heap)>10:
                    heapq.heappop(heap)
        res=[]
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
