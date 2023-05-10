#Complexity analysis 
#Solution- 01 Time complexity- O(nlogn) Space complexity- O(1)
def findThreeLargestNumbers(array):
	array.sort()
	iniElement = len(array)-3
	return array[iniElement: ]
   
#Solution- 02 Time complexity- O(n) Space complexity- O(1)

if __name__ == "__main__":
    array = [0,74,21,87,45,61,71,72,73]
    print("Output=",findThreeLargestNumbers(array))