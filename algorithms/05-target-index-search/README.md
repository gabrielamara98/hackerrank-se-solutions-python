# Target Index Search
**Difficulty:** <span style="color:#00B8A3">Easy</span> | [HackerRank](https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/lookup-with-binary-search/problem?isFullScreen=true)


## 🎯 Challenge
Given a sorted array of distinct integers and a target value, return the index of the target or -1 if not found.

## ⚠️ Edge Cases
* **Target Not Present:** The `while` loop terminates when `left > right` without finding the target, safely returning `-1`.
* **Single-Element Array:** The initial state has `left = 0` and `right = 0`. The loop executes once, evaluates `mid = 0`, finds the target, and correctly returns `0`.
* **Target at Boundaries:** Evaluates boundaries seamlessly without out-of-bounds index errors as `left` and `right` pointers narrow down to index `0` or `len(nums) - 1`.
* **Empty Array:** Handled cleanly as `right = -1`, causing `left <= right` (`0 <= -1`) to evaluate to `False` immediately and return `-1`.

## 💡 Resolution
The solution implements the standard **Binary Search** algorithm on a sorted array:
1. Initialize two pointers: `left = 0` and `right = len(nums) - 1`.
2. Iterate using a `while left <= right` loop.
3. Compute the midpoint index dynamically: `mid = (left + right) // 2`.
4. If `nums[mid] == target`, the element is found; return `mid`.
5. If `target < nums[mid]`, discard the right half by updating `right = mid - 1`.
6. If `target > nums[mid]`, discard the left half by updating `left = mid + 1`.
7. If the loop completes without finding `target`, return `-1`.

## ⚙️ Complexity
**Time Complexity:** $O(\log N)$ 

**Space Complexity:** $O(1)$