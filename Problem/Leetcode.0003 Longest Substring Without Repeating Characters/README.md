# Leetcode.0003 Longest Substring Without Repeating Characters
## 程式簡介
`Leetcode.0003`；`Medium`
### 簡述
* Given a string s, find the length of the longest substring without repeating characters.


Example 1
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
Example 2
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
Example 3
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```
Constraints:  
![image](https://user-images.githubusercontent.com/93152909/156933387-96cc9dba-9e50-4789-9360-43c9ddd0e01e.png)

### 範例圖
* `approach1.py`：`Python`；`Hash Table`
  *  `Time:O(n)` `Space:O(n)`
  
  ![image](https://user-images.githubusercontent.com/93152909/157088797-df0dfc5b-573a-4483-aca9-b554f71cc201.png)

