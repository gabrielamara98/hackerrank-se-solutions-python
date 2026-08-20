# Check for Non-Identical String Rotation
**Difficulty:** <span style="color:#00B8A3">Easy</span> | [HackerRank](https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/check-non-identical-string-rotation/problem?isFullScreen=true)


## 🎯 Challenge
Given two strings s1 and s2, return 1 if s2 is a rotation of s1 but not identical to s1, otherwise return 0.

## ⚠️ Edge Cases
* **Strings of different lengths :** Immediately handled by returning `0`, as strings with unequal lengths can never be rotations of each other.
* **Identical strings :** Handled at the start by returning `0`, since the problem specifically requires a *non-identical* rotation.
* **Single-character or repeated-character identical strings :** Caught by the initial `s1 == s2` check and correctly returns `0`.
* **No matching rotation :** The loop exhausts all $N$ potential slice offsets without finding a match, returning `0`.

## 💡 Resolution
The solution evaluates possible string rotations through explicit slicing in a loop:
1. First, validate edge cases: return `0` if `s1` and `s2` differ in length or if they are already identical strings.
2. Initialize an index tracker `n = 0`.
3. Iterate while `n < len(s1)` and generate the rotated string `s1_rotation = s1[n:] + s1[:n]`.
4. Check if `s1_rotation == s2`. If a match is found, return `1`.
5. Increment `n` by 1 and repeat until all possible shift offsets have been checked.
6. If no rotation matches `s2`, return `0`.


## ⚙️ Complexity
**Time Complexity:** $O(N^2)$

**Space Complexity:** $O(N)$ 