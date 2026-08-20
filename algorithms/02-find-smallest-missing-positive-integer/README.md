# Find Smallest Missing Positive Integer
**Difficulty:** <span style="color:#00B8A3">Easy</span> | [HackerRank](https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/find-smallest-missing-positive-integer/problem?isFullScreen=true)


## 🎯 Challenge
Given an unsorted integer array, find the smallest missing positive integer. The algorithm should run in linear time and use $O(1)$ auxiliary space.

## ⚠️ Edge Cases
* **Array with Non-Positives or Zeros (`[-3, -1, 0]`):** No swaps occur. 
* **Already Sorted Array (`[1, 2, 3]`):** No swaps occur. The algorithm scans through all elements and returns `len(orderNumbers) + 1` (which is `4`).
* **Duplicate Numbers (`[1, 1, 2]`):** The condition `element != orderNumbers[element-1]` prevents infinite loops by skipping duplicates that are already in their valid position.
* **Out-of-Range / Large Numbers (`[100, 1000, -50]`):** The condition `element <= len(orderNumbers)` ensures numbers larger than the array length are ignored, as they cannot affect the smallest missing positive.
* **Single-Element Arrays (`[1]` or `[2]`):** Returns `2` for `[1]` and `1` for `[2]` without going out of bounds.

## 💡 Resolution
The algorithm uses the **Cyclic Sort** pattern to solve the problem in linear time and $O(1)$ auxiliary space:
1. Initialize a pointer `x = 0` to iterate through `orderNumbers`.
2. While `x < len(orderNumbers)`, check if the current element (`element`) is positive, within the array's bounds ($1 \le \text{element} \le N$), and not already in its correct target index (`element != orderNumbers[element-1]`).
3. If valid and misplaced, swap `orderNumbers[x]` with `orderNumbers[element-1]` without advancing `x`, so the new element at `x` is evaluated next.
4. If invalid or already correctly placed, increment `x` by 1.
5. After rearranging, make a second pass through the array. Return the first missing value $i + 1$ where `orderNumbers[i] != i + 1`.
6. If all positions $1 \dots N$ are present, return $N + 1$.

## ⚙️ Complexity
**Time Complexity:** $O(N)$

**Space Complexity:** $O(1)$ 