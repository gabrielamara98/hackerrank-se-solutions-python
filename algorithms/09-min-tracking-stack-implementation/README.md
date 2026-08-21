# Min-Tracking Stack Implementation
**Difficulty:** <span style="color:#00B8A3">Easy</span> | [HackerRank](https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/min-tracking-stack/problem?isFullScreen=true)


## 🎯 Challenge
Implement a stack that supports push, pop, top, and getMin operations in O(1) time, where getMin returns the minimum element.

## ⚠️ Edge Cases
* **Duplicate Minimum Values:** Pushing multiple instances of the current minimum value requires adding each to the auxiliary stack using `<=`. Otherwise, popping one instance removes the minimum tracking prematurely for remaining duplicate values.
* **Popping Non-Minimum Elements:** When popping an element that is strictly larger than the current minimum, the auxiliary stack remains untouched while only the main stack pops.
* **Empty Stack Operations:** Operations checking or pushing when `min_number` is empty are safely guarded by `len(min_number) < 1` to initialize the first minimum value.
* **Consecutive Pop and GetMin Calls:** Popping the exact current minimum properly updates the tracking stack so subsequent `getMin` calls instantly reflect the previous minimum.

## 💡 Resolution
The algorithm utilizes two **Stack (LIFO)** data structures—a main stack for storing elements and an auxiliary stack to track historical minimums in $O(1)$ time:
1. Iterate through each string operation `op` in the `operations` list.
2. If `getPush(op, stack)` identifies a push command:
   * Parse the integer and append it to the main `stack`.
   * If `min_number` is empty, append the new element to `min_number`.
   * If `min_number` is not empty and the new element is $\le$ the top of `min_number`, append it to `min_number`.
3. If `getPop(op)` identifies a pop command:
   * Compare the top element of `stack` with the top of `min_number`.
   * If they match, pop the top element from `min_number`.
   * Pop the top element from `stack`.
4. If `getTop(op)` identifies a top command, append `stack[-1]` to the `output` list.
5. If `getMin(op)` identifies a min command, append `min_number[-1]` to the `output` list.
6. Return the `output` list containing all retrieved query results.

## ⚙️ Complexity
**Time Complexity:** $O(1)$ per operation

**Space Complexity:** $O(N)$
