#!/usr/bin/python3
""" Change making module.
"""

def makeChange(coins, total):
	""" Determines the fewest number of coins needed to meet a given 
	amount total when given a pile of coins of different values.
	"""
	if total <= 0:
		return 0

	# Initialize an array to store the fewes number of coins needed
	# for each amount from 0 to total
	dp = [float('inf') * (total + 1)]

	# Set the fewest number of coins needed for 0 as 0
	dp[0] = 0

	# Iterate through each coin value for coin in coins
	# For each coin value, update the fewest number of coins needed for
	# each amount from the coin value to total
	for i in range(coins, total + 1):
		dp[i] = min(dp[i], dp[i - coins] + 1)

	# If thefewest number of coins nedded for the total is still infinity,
	# it means it cannot be met by any number of coins in the list
	return dp[total] if dp[total] != float('inf') else -1