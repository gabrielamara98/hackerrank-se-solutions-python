# Check Palindrome by Filtering Non-Letters
**Difficulty:** <span style="color:#00B8A3">Easy</span> | [HackerRank](https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/check-palindrome-filter-non-letters/problem?isFullScreen=true)


## 🎯 Challenge
Given a string containing letters, digits, and symbols, determine if it reads the same forwards and backwards when considering only alphabetic characters (case-insensitive).

## ⚠️ Edge Cases
* **Strings with non-alphabetic characters :** Filtered correctly during iteration using `.isalpha()`, ensuring digits and symbols are completely ignored before testing.
* **Mixed case letters :** Converted to lowercase using `.lower()` during filtering so case differences do not invalidate matching letters.
* **Empty or non-alphabetic input :** The filtered string `cd` becomes empty `""`. Since `"" == ""`, the algorithm returns `1` (an empty string is vacuously a palindrome).
* **Single alphabetic character :** The filtered string length is 1, reversing it yields the same single character, correctly returning `1`.

## 💡 Resolution
The solution follows a two-pass string construction and reversal approach:
1. Iterate through each character of the input `code` and extract only alphabetic letters (`x.isalpha()`).
2. Convert every valid letter to lowercase (`x.lower()`) and append it to a clean string `cd`.
3. Reconstruct a reversed version of `cd` (`palindrome_test`) by iterating backwards from `len(cd) - 1` down to `0`.
4. Compare `cd` directly with `palindrome_test`: return `1` if they are equal, otherwise return `0`.

## ⚙️ Complexity
**Time Complexity:** $O(N)$

**Space Complexity:** $O(N)$ 
