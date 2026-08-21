# Validate Properly Nested Brackets
**Difficulty:** <span style="color:#00B8A3">Easy</span> | [HackerRank](https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/validate-properly-nested-brackets/problem?isFullScreen=true)


## 🎯 Challenge
Given a string, check if all brackets ('()', '{}', '[]') are properly matched and nested. Return 1 if valid, otherwise return 0.

## ⚠️ Edge Cases
**No Brackets Present:** Non-bracket characters are ignored during iteration. Since the stack remains empty throughout, the function correctly returns `1`.
* **Closing Bracket First:** Encountering a closing bracket when `stack` is empty triggers `len(stack) == 0` and immediately returns `0`.
* **Mismatched Bracket Types:** Popping the top element fails the `checkBrackets` validation check and returns `0`.
* **Unclosed Opening Brackets:** Remaining open brackets left in `stack` after processing the string are caught by `if len(stack) > 0`, returning `0`.

## 💡 Resolution
The algorithm uses a **Stack (LIFO)** data structure to keep track of open brackets while ignoring all other characters:
1. Iterate through each character `letter` in `code_snippet`.
2. If `letter` is an opening bracket (`[`, `{`, `(`), push it onto the `stack`.
3. If `letter` is a closing bracket (`]`, `}`, `)`):
   * Return `0` immediately if the `stack` is empty (unmatched closing bracket).
   * Pop the top element from `stack` and verify if it matches the current closing bracket via `checkBrackets`. Return `0` if mismatched.
4. Ignore all non-bracket characters (letters, digits, whitespace, operators).
5. After the loop, return `1` if the `stack` is completely empty, or `0` if unclosed brackets remain.

## ⚙️ Complexity
**Time Complexity:** $O(N)$

**Space Complexity:** $O(N)$