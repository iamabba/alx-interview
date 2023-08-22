This Python script defines a makeChange function that calculates the minimum number of coins needed to make change for a given total. It uses dynamic programming and accepts a list of coin denominations and a target total as input. If the total is not achievable with the provided coins, it returns -1. Otherwise, it returns the fewest number of coins required.

Usage
Ensure you have Python 3 installed.

Use the makeChange(coins, total) function, where coins is a list of coin values and total is the target amount.

Example:

python
Copy code
coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
# Output: 3 (2 coins of 5 and 1 coin of 1)
