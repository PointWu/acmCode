#!/usr/bin/env python3

#力扣
#https://leetcode-cn.com/problems/palindrome-number/

class Solution:
	def isPalindrome(self, x: int) -> bool:
		s = list(str(x))
		t = s[::-1]
		return t==s