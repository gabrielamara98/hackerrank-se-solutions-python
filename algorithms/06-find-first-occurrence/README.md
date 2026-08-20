# Find First Occurrence
**Difficulty:** <span style="color:#00B8A3">Easy</span> | [HackerRank](https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/first-occurrence-in-event-code-log/problem?isFullScreen=true)


## 🎯 Challenge
Given a sorted array of integers that may contain duplicates, return the index of the first occurrence of a target value or -1 if not found.

## ⚠️ Edge Cases
* **Empty Array:** Handled naturally as `right = -1`, which causes `left <= right` (`0 <= -1`) to evaluate to `False` on the first check and immediately returns `-1`.
* **Target at Index 0:** The condition `mid == 0` prevents an out-of-bounds index error when checking `nums[mid - 1]` and immediately confirms index `0` as the first occurrence.
* **Target with Duplicates:** If `target == nums[mid]` but `nums[mid - 1]` also equals `target`, `right` is shifted to `mid - 1` to continue searching in the left partition until the earliest occurrence is found.
* **Target Not Present:** The search space contracts until `left > right`, terminating the `while` loop cleanly and returning `-1`.

## 💡 Resolution
The algorithm modifies standard Binary Search to eagerly confirm if a target match is its first occurrence:
1. Initialize two pointers: `left = 0` and `right = len(nums) - 1`.
2. Compute the midpoint index in each iteration: `mid = (left + right) // 2`.
3. If `target == nums[mid]`:
   * Check if `mid == 0` or `nums[mid] != nums[mid - 1]`. If true, `mid` is guaranteed to be the first occurrence, so return `mid`.
   * Otherwise, a duplicate exists to the left; narrow the search to the left half by setting `right = mid - 1`.
4. If `target < nums[mid]`, discard the right partition by setting `right = mid - 1`.
5. If `target > nums[mid]`, discard the left partition by setting `left = mid + 1`.
6. Return `-1` if the loop ends without locating the target.

## ⚙️ Complexity
**Time Complexity:** $O(\log N)$ 

**Space Complexity:** $O(1)$