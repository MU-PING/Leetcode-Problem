# Leetcode.0005 Longest Palindromic Substring
## 程式簡介
`Leetcode.0005`；`Medium`
### 簡述
* Given a string s, return the longest palindromic substring in s.

Example 1
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```
Example 2
```
Input: s = "cbbd"
Output: "bb"
```

Constraints:  
![image](https://user-images.githubusercontent.com/93152909/177420145-b45e82b4-ee0b-4cc8-a21b-b0df7fc692c1.png)


### 範例圖
* `approach1.py`：`Python`；`Dynamic Programming`
  *  `Worst Time:O(n^2)` `Space:O(n^2)`
  
  ![image](https://user-images.githubusercontent.com/93152909/177418946-3f0d2ddd-3d65-430b-ab1c-a41664997b11.png)
  
  * DP數學式
  
    ![image](https://user-images.githubusercontent.com/93152909/177419482-5ee32135-14f3-4628-851f-c5b738dd6d60.png)
  
  * DP概念圖
  
    <img src="https://user-images.githubusercontent.com/93152909/177419179-4b7a95bf-f8e6-4460-9af1-a9182360df32.png" alt="Girl in a jacket" width="600">

  * 備註： 當測資過大時可能會 `Time Limit Exceeded`，推測是table的建立太耗時間。。
