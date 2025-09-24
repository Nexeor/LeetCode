class TimeMap:

    def __init__(self):
        self.timeset = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        timeline = self.timeset.get(key, [])
        timeline.append((value, timestamp))
        self.timeset[key] = timeline

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeset:
            return ""

        timeline = self.timeset[key]
        l, r = 0, len(timeline) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            value, prev_timestamp = timeline[m]

            # Need closest prev_timestamp <= timestamp
            if prev_timestamp > timestamp:
                r = m - 1
            # If current time is greater, record and move to the right to test look for a closer timestamp
            else:
                res = value
                l = m + 1
        return res
