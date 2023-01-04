def threeNumberSum(array, targetSum):
    # Write your code here.
    result = []
    array.sort()
    arrlen = len(array)
    for i in range(arrlen):
        for j in range(i+1,arrlen):
            for k in range(j+1,arrlen):
                if array[i] + array[j] + array[k] == targetSum:
                    result.append([array[i] , array[j] , array[k]])          
    return result





array = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
print(threeNumberSum(array,target))