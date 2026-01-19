"""
All combinations of size r from an array
You are given an array arr[] consisting of n elements. Your task is to generate and print all possible combinations of exactly r elements from this array.
Note: A combination is a selection of items where the order does not matter. Ensure that each unique group of r elements is printed only once, regardless of order.

Example:

Input: arr = [1, 2, 3, 4], r = 2
Output: 1 2
               1 3
               1 4
               2 3
               2 4
               3 4
Explanation: We need to generate all possible combinations of size 2 from an array of size 4. The total number of such combinations is given by the formula:
4C2 = 4! / [(4 - 2)! × 2!] = 6 combinations.

Input: arr = [1, 2, 3, 4], r = 3
Output: 1 2 3
               1 2 4
               1 3 4
               2 3 4
Explanation: We need to generate all possible combinations of size 3 from an array of size 4. The total number of such combinations is given by the formula:
4C3 = 4! / [(4 - 3)! × 3!] = 4 combinations.
"""


def combineUtils(ind,r,data,result,arr):
	n=len(arr)

	if len(data) == r:
		result.append(data.copy())
		return

	if ind >= n:
		return

	data.append(arr[ind])

	combineUtils(ind+1,r,data,result,arr)
	data.pop()
	combineUtils(ind+1,r,data,result,arr)

def pair(arr,r):
	result=[]
	data = []
	combineUtils(0,r,data,result,arr)
	return result

arr = [1, 2, 3, 4]
r = 2
res = pair(arr, r)
for comb in res:
    for num in comb:
        print(num, end=" ")
    print()