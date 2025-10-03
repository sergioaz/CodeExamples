"""
Class to limit rate per user per time
"""
import time
from collections import deque, defaultdict

class RateLimiter ():

    def __init__(self, rateLimit: int, timeWindow: int):
        """
        :param rateLimit: Number requests
        :param timeWindow: time period in secs
        """
        self.userDict = defaultdict(deque)
        self.rateLimit = rateLimit
        self.timeWindow = timeWindow

    def addRequest(self, userName: str) -> bool:
        """
        try to add request to user queue
        :param userName:
        :return: Request allowed or not
        """

        # remove timestamps older than time window
        while self.userDict[userName] and self.userDict[userName][0] < (time.time() - self.timeWindow):
            self.userDict[userName].popleft()

        if len(self.userDict[userName]) < self.rateLimit:
            self.userDict[userName].append(time.time())
            return True
        else:
            return False

rateLimitTest = RateLimiter(3, 5)

for i in range(15):
    res = rateLimitTest.addRequest("user1")
    print (f"{i=}, {res=}, time={time.time()}, len={len(rateLimitTest.userDict['user1'])}")
    time.sleep (1)
