# maximum-subarray
## 程式簡介
### 簡述
> [Leetcode-53題](https://leetcode.com/problems/maximum-subarray/)，使用 Dynamic Programming 技術實作

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

1 <= nums.length <= <img src="https://render.githubusercontent.com/render/math?math=10^5">  
<img src="https://render.githubusercontent.com/render/math?math=-10^4"> <= nums[ i ] <= <img src="https://render.githubusercontent.com/render/math?math=10^4">

### 範例圖
* leetcode.py：符合leetcode的寫法  

  ![image](https://user-images.githubusercontent.com/93152909/139852988-9e7f2cec-1305-4df2-b1af-bdcea0a7b3e9.png)

* main.py：將leetcode.py改寫並補充「Maximum subarray」  

  ![image](https://user-images.githubusercontent.com/93152909/139862612-7294e767-8981-4654-914d-e94b6559fce0.png)


### 解題技巧與分析
* 主要三種解法的時間複雜度比較

  * 暴力法：O(<img src="https://render.githubusercontent.com/render/math?math=n^2">)
  * Dynamic Programming：O(<img src="https://render.githubusercontent.com/render/math?math=n">)
  * Divide and Conquer：O(<img src="https://render.githubusercontent.com/render/math?math=n">)
  
