#Complexity analysis
#Solution- 01 Time complexity- O(n^2) Space complexity- O(1)
def isValidSubsequence(array, sequence):
    arrStart = 0
    seqStart = 0
    #Return true when length of sequence is zero
    if len(sequence) == 0:
        return True
    while arrStart < len(array):
        if array[arrStart] == sequence[seqStart]:
            seqStart += 1
        if len(sequence) == seqStart:
            break
        arrStart += 1
    return (seqStart == len(sequence))


    