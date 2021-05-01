# AC

y = lambda x: x>>1

def subsetSum(l, i, target_sum, memo=dict()):
	key = i, target_sum
	if key in memo:
		return memo[key]

	if target_sum == 0:
		return True
	if i == len(l):
		return False

	to_return = subsetSum(l, i+1, target_sum, memo) or subsetSum(l, i+1, target_sum-l[i], memo)
	memo[key] = to_return
	return to_return



def make_good(l):
	for i in range(len(l)):
		if l[i] & 1:	# odd
			return i+1	# 1-based index

	# all items are even
	return(make_good(list(map(y, l))))


if __name__ == '__main__':
	n = int(input())
	l = list(map(int, input().split()))

	if sum(l) & 1==1 or not subsetSum(l, 0, sum(l)//2):	
		print(0)

	else:

		res = make_good(l)
		print(1)
		print(res)

