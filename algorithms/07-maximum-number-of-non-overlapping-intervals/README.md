# Maximum Number of Non-Overlapping Intervals
**Difficulty:** <span style="color:#00B8A3">Easy</span> | [HackerRank](https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/maximum-non-overlapping-intervals/problem?isFullScreen=true)


## 🎯 Challenge
Given an array of intervals where each interval has a start and end time, return the maximum number of non-overlapping intervals.

## ⚠️ Edge Cases
* **Empty List of Meetings:** Handled immediately at the start by returning `None` (or `0` depending on requirements) before attempting to access index 0.
* **Single Meeting:** The `for` loop from index 1 is skipped, and the code safely returns `count = 1`.
* **Adjacent Meetings:** The condition `meetings[x][0] >= last_end` uses the `>=` operator, correctly allowing a new meeting to start at the exact same minute the previous meeting ends.
* **Unsorted Input Intervals:** Addressed by explicitly sorting the input intervals based on their end times (`x[1]`) before selecting meetings.

## 💡 Resolution
The algorithm applies the **Interval Scheduling / Greedy Algorithm** approach:
1. Validate edge cases: return early if the meeting list is empty.
2. Sort all meetings in ascending order based on their end times (`meetings.sort(key=lambda x: x[1])`). Selecting meetings that end earliest leaves the maximum room for remaining meetings.
3. Initialize the schedule by selecting the first meeting: set `count = 1` and store its end time in `last_end = meetings[0][1]`.
4. Iterate through the remaining meetings starting from index 1.
5. For each meeting, check if its start time is greater than or equal to `last_end` (`meetings[x][0] >= last_end`).
6. If non-overlapping, increment `count` by 1 and update `last_end` to the current meeting's end time.
7. Return `count` upon completing the iteration.

## ⚙️ Complexity
**Time Complexity:** $O(N \log N)$

**Space Complexity:** $O(1)$ and $O(N)$