# Leetcode.0001 Two Sum
## 程式簡介
`Leetcode.0001`；`Easy`
### 簡述
* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
* You may assume that each input would have exactly one solution, and you may not use the same element twice.
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
* 1 <= nums.length <= <img src="https://render.githubusercontent.com/render/math?math=10^5">  
* <img src="https://render.githubusercontent.com/render/math?math=-10^4"> <= nums[ i ] <= <img src="https://render.githubusercontent.com/render/math?math=10^4">

### 範例圖
* `approach1.py`：`Python`；`Dynamic Programming` - O(<img src="https://render.githubusercontent.com/render/math?math=n">)

  ![image](https://user-images.githubusercontent.com/93152909/139852988-9e7f2cec-1305-4df2-b1af-bdcea0a7b3e9.png)

### 其他解法
* `Brute Force` - O(<img src="https://render.githubusercontent.com/render/math?math=n^2">)
* `Divide and Conquer` - O(<img src="https://render.githubusercontent.com/render/math?math=n">)
  
