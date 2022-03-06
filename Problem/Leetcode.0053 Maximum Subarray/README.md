# Leetcode.0053 Maximum Subarray
## 程式簡介
`Leetcode.0053`；`Easy`
### 簡述
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

* Input：整數陣列
* Output：最大的連續子陣列之合

Example 1
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```
Example 2
```
Input: nums = [1]
Output: 1
```
Example 3
```
Input: nums = [5,4,-1,7,8]
Output: 23
```
Constraints:

<img src="https://render.githubusercontent.com/render/math?math=1<=">   nums.length  <img src="https://render.githubusercontent.com/render/math?math=<=10^5">  
<img src="https://render.githubusercontent.com/render/math?math=-10^4<="> nums[ i ] <img src="https://render.githubusercontent.com/render/math?math=<=10^4">

### 範例圖
* `approach1.py`：`Python`；`Dynamic Programming` - O(<img src="https://render.githubusercontent.com/render/math?math=n">)

  ![image](https://user-images.githubusercontent.com/93152909/139852988-9e7f2cec-1305-4df2-b1af-bdcea0a7b3e9.png)

### 其他解法
* `Brute Force` - O(<img src="https://render.githubusercontent.com/render/math?math=n^2">)
* `Divide and Conquer` - O(<img src="https://render.githubusercontent.com/render/math?math=n">)
  
