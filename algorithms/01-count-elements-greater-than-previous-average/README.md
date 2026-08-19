# Count Elements Greater Than Previous Average
**Difficulty:** <span style="color:#00B8A3">Easy</span> | [Hacker Rank](https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average/problem?isFullScreen=true)


## 🎯 Challenge
Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.

## ⚠️ Edge Cases
* **Array with fewer than 2 elements (`len < 2`):** Handled at the start by returning `0`, as it is impossible to evaluate a previous average without at least one historical value.
* **Array with zero or duplicate values:** The comparison uses the strictly greater-than operator (`>`), preventing false positives when the current metric exactly equals the previous average.
* **Iteration Start (`x = 1`):** Iteration starts at index 1 to ensure the division `average / x` never triggers a division-by-zero error.

## 💡 Resolution
Instead of recalculating the average from scratch for every element — which would require a nested loop resulting in $O(N^2)$ time complexity —, the solution uses a **single-pass running sum** approach:
1. Initialize a running sum variable (`average`) with the value of the first element `responseTimes[0]`.
2. Iterate through the array starting from the second element (`index 1`).
3. For each element, compute the previous average dynamically by dividing the running sum by the number of preceding elements (`average / x`).
4. If the current value is greater than this average, increment the `count` tracker.
5. Add the current element's value to the running sum before moving to the next iteration.

## ⚙️ Complexity
**Time Complexity:** $O(N)$ 

**Space Complexity:** $O(1)$