#!/usr/bin/env python3

#https://exercise.acmcoder.com/online/online_judge_ques?ques_id=1660&konwledgeId=134
#赛码


import math

n = int(input())
for i in range(n):
	d = ['a','b','c','d','e','f','g','h','i','j','k','l']
	s = 1
	str1 = input()
	for j in range(11):
		m = len([jj for jj in d if jj < str1[j]])
		d.remove(str1[j])
		s += m * math.factorial(11 - j)
	print(s)
	