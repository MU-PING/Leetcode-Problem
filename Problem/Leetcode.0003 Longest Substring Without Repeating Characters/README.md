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
![image](https://user-images.githubusercontent.com/93152909/157143914-8875681f-0590-47f6-8d16-6384ef60294a.png)

### 範例圖
* `approach1.py`：`Python`；`Sliding Window`
  *  `Time:O(2n)` `Space:O(m)`
  *  `m: the size of the charset/alphabet` 
  
  ![image](https://user-images.githubusercontent.com/93152909/158290393-f8ee52cf-0308-4aa6-bb4c-510bd67e36e7.png)

