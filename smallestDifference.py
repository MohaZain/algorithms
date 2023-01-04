def smallestDifference(arr, arr2):
    # Write your code here.
    # print(arr, arr2)
    arr.sort()
    arr2.sort() 
    pair = []
    diff = arr[len(arr)-1] + arr2[len(arr2)-1]
    indx_one = 0 
    indx_two = 0
    while indx_one < len(arr) and indx_two < len(arr2):
        ebs_check = abs(arr[indx_one] - arr2[indx_two])
        if ebs_check < diff:
            diff = ebs_check
            pair = [arr[indx_one] , arr2[indx_two]]
        if arr[indx_one] > arr2[indx_two]:
            indx_two += 1
        else:
            indx_one += 1
    print(arr,arr2)
    return pair

    # return arrayOne_sort,arrayTwo_sort





# x = [-1,5,10,20,28,3]
# print(x[len(x)-1])
print(smallestDifference([-1,5,10,20,28,3], [26,134,135,15,17]))