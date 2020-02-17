# store end time in heap,
# time O(n*log(n)), space O(n)
import heapq
class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        if not events:
            return 0
        events.sort()
        heap = []
        time = events[0][0]
        cnt = 0
        i = 0
        while i < len(events):
            if not heap:
                time = events[i][0]
            start, end = events[i]
            while i < len(events) and events[i][0] == start:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and (i >= len(events) or (time < events[i][0])):
                end = heapq.heappop(heap)
                if end >= time:
                    cnt += 1
                    time += 1
        return cnt
    


"""
Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.

 

Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
Example 3:

Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4
Example 4:

Input: events = [[1,100000]]
Output: 1
Example 5:

Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7
 

Constraints:

1 <= events.length <= 10^5
events[i].length == 2
1 <= events[i][0] <= events[i][1] <= 10^5
"""
