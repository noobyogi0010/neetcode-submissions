"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        what information i need to be able to assign rooms for meetings
        without any conflicts
        we can sort the meetings by their start time
        use a min heap to keep track of meetings that will end earliest
        whenever a new meeting arrives, i'll try to remove all the meetings
        from the min heap which have ended
        here's a flaw in your thinking - the meeting rooms are not fixed
        its upto me however rooms i wanna add in
        aah but i can use min heap as the count of my meetings, so when a 
        new meeting comes remove all the meetings which have occured already
        and add the new meeting - finally the length of heap will give me
        the min no of rooms
        """
        start = sorted(interval.start for interval in intervals)
        end = sorted(interval.end for interval in intervals)
        s, e = 0, 0
        count = 0
        res = 0

        while s < len(start) and e < len(end):
            # this tells how many meetings have started
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                # this reduces the count when a meeting ends!
                e += 1
                count -= 1

            res = max(res, count)

        return res

        