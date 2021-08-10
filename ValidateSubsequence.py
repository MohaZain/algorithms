# Subsequence of an array is a set of number that are in the same order they appear in the array
# Example array [1,2,3,4] subsequence [1] or [1,2] [2,3,4] ...etc
def isValidSubsequence(array, sequence):
    # Write your code here.
    arrLen = len(array)
    count = 0
    for i in range(arrLen):
    	if array[i] == sequence[count]:
    	    count = count + 1
        if count >= len(sequence):
            return True            
    return False

# ---------------------Test True----------------------------
array = [5, 1, 22, 25, 6, -1, 8, 10]
seq =  [1, 6, -1, 10]
print('True == ',isValidSubsequence(array,seq))
# ---------------------Test False----------------------------
array = [5, 1, 22, 25, 6, -1, 8, 10]
seq =  [5, 1, 22, 25, 6, -1, 8, 10, 12]
print('False == ',isValidSubsequence(array,seq))
