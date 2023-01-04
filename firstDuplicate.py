def firstDuplicateValue(array):
    # Write your code here.
    result = len(array) + 1
    for i,num in enumerate(array):   
        for j in range(i + 1,len(array)):
            # print(i,'-----',j)
            print(array[i] ,'------', array[j])
            if array[i] == array[j]:
                if j < result:
                    result = j
    if result == len(array) + 1:
        return -1
    return array[result] 



# print(firstDuplicateValue(array=[2, 1, 5, 2, 3, 3, 4]))
print(firstDuplicateValue(array=[1, 2, 3, 3, 2, 6, 7]))