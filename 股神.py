#!/usr/bin/env python3
#https://exercise.acmcoder.com/online/online_judge_ques?ques_id=1664&konwledgeId=134
# 赛码

def StockCalculation(n):
	money = 1 #钱
	day = 1 #天数
	up = 1 #涨幅
	while day < n:
		if day + up + 1 <= n:
			money = money + up - 1
			day = day + up + 1
			up = up + 1
		else:
			money = money + (n - day)
			break
	return money


while True:
	n = int(input()) #买股票的第n天
	print(StockCalculation(n))