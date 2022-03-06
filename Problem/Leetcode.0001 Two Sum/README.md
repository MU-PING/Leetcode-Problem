# Leetcode.0001 Two Sum
## 程式簡介
`Leetcode.0001`；`Easy`
### 簡述
* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
* You may assume that each input would have **exactly one solution**, and you may not use the same element twice.
* You can return the answer in any order.


Example 1
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
Example 2
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
Example 3
```
Input: nums = [3,3], target = 6
Output: [0,1]
```
Constraints:  
![image](https://user-images.githubusercontent.com/93152909/156933387-96cc9dba-9e50-4789-9360-43c9ddd0e01e.png)

### 範例圖
* `approach1.py`：`Python`；`Hash Table`
  * <img align="middle" src="https://render.githubusercontent.com/render/math?math=Time:O(n)">
  * <img src="https://render.githubusercontent.com/render/math?math=Space:O(n)">

### 其他解法
* `Brute Force`
  * <img align="middle" src="https://render.githubusercontent.com/render/math?math=Time:O(n^2)">
  * <img src="https://render.githubusercontent.com/render/math?math=Space:O(1)">
  
