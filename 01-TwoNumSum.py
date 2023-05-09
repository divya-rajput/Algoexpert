#Complexity analysis
#Solution- 01 Time complexity- O(n^2) Space complexity- O(1)
def twoNumberSum(array, targetSum):
	for i in range(len(array)):
		j = len(array)-1
		while j > i:
			if(array[i]+array[j])==targetSum:
				return [array[i],array[j]]
			else:
				j -= 1
	return []

#Solution- 02 Time complexity- O(n) Space complexity- O(n)
def twoNumberSum(array, targetSum):
    numbers = []
    table = []
    for firstNum in array:
        secondNum = targetSum - firstNum
        if secondNum  in table:
            numbers.append(firstNum)
            numbers.append(secondNum)
            return numbers
        else:
            table.append(firstNum)
    return numbers
