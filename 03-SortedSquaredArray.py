#Complexity analysis
#Solution- 01 Time complexity- O(n^2) Space complexity- O(1)
#Approach used- Two pointers
def sortedSquaredArray(array):
    result = [0] * len(array)
    min = 0
    max = len(array) - 1
    i = len(array) -1
    while min <= max:
        if abs(array[min]) > abs(array[max]):
            result[i] = array[min] * array[min]
            min +=1
        else:
            result[i] = array[max] * array[max]
            max -=1
        i -= 1
    return result
