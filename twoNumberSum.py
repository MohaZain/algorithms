def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    print(array)
    for i in range(len(array)):
        pointer = i 
        for j in range(len(array[i+1:])):
            pointer +=1
            if array[i] + array[pointer] == target:
                return [array[i] , array[pointer]]

    return []


arr = [3,5,-4,8,11,1,-1,6]
target = 10 

print(twoNumberSum(arr,target))