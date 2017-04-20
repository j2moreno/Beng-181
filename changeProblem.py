import sys

def change(money,coins):
	change = {}
	change[0] = 0

	for i in range(1,money+1):
		change[i] = float("inf")
		for element in coins:
			if i >= int(element):
				if change[i - int(element)] + 1 < change[i]:
					change[i] = change[i-int(element)] + 1
				

	return change[money]



filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []
diffCoins = data[0].split(",")

result = change(19414,diffCoins)
print result
