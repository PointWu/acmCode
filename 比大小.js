/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * 
 * 力扣  https://leetcode-cn.com/problems/two-sum/
 * 暴力能解决 要什么优雅
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
};