# Leetcode.0004 Median of Two Sorted Arrays
## 程式簡介
`Leetcode.0004`；`Hard`
### 簡述
* Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

* The overall run time complexity should be `O(log (m+n))`.


Example 1
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```
Example 2
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

Constraints:  
![image](https://user-images.githubusercontent.com/93152909/158287422-11f29871-e069-4a9c-85d0-3a283bbbcb53.png)

### 範例圖
* `approach1.py`：`Python`；`Binary Search`
  *  `Worst Time: O(min(log n, log m))` `Space:O(1)`
  *  `n: len(nums1)` `m: len(nums2)`

  <img src="https://user-images.githubusercontent.com/93152909/158291419-6e84c717-f638-4b30-8271-ecb0a5bcfe89.png" width="750px">
  
  ![image](https://user-images.githubusercontent.com/93152909/158287945-9cc42d36-02c5-4b06-856f-82efef38be88.png)



