# Mohammed zain aljoufi

# function that will take string and return dict of key"latter in the string" 
# value = how many the letter was repeated 
# example str = programming  return {"p":1,"r":2 .. }
def countLetter (str):
    # complixity n
    str_dict= {}
    # the function loop each latter in a string 
    # if letter already added in the dictionary will add 1 to its value 
    # 
    for letter in str:
        if letter in str_dict:
            str_dict[letter] = str_dict[letter] + 1
        else:
            str_dict[letter] = 1
        # print(letter)
    return str_dict



print("out h:1, e:1, l:2, o:1 |||| ",countLetter(str="hello"))
print("out l:1, e:2, g:1, n:1, |||| ",countLetter(str="legend"))

print("----------------------------------------------------")

# function take list of sorted number and return the minimum number that are not in the array
# and not less or equal 0 
def minNum (arr):
    arr_length = len(arr)
    # if the array contain only one value 
    if arr_length == 1:
        # will check first :
        # if array value == 1 then return 2 
        # else it will be > 1 then return 1 as a minimum number
        if arr[0] == 1:
            return 2
        else :
            return 1
     # if the array contain two values
    elif arr_length == 2:
        # if value of index 0 > 1 then return 1
        if arr[0] > 1:
            return 1
        # if index 1 is 2 and already index 0 is 1 then the min number is 3
        elif arr[1] == 2:
            return 3
        # else index[0] is 1 and index[1] > 2 then return min number is 2 
        else: 
            return 2
    else:
        for i in range(arr_length):
#            edit if the first index not equal 1
            if arr[0] != 1:
                return 1
            # when loop reach to last index
            # and there is no range between the index's will return arr[last_index] + 1 
            # Examole [1,2,3,4,5] should return 6
            elif i == arr_length - 1:
                return arr[i] + 1
            elif arr[i+1] - arr[i] != 1:
                return arr[i] + 1
# test list with one index    
print("number = 1 output ",minNum(arr=[1]))
print("number = 2 output ",minNum(arr=[2]))
print("number = 3 output ",minNum(arr=[3]))
# test list with two index    
print("number = 2,10 output ",minNum(arr=[2,10]))
print("number = 1,2 output ",minNum(arr=[1,2]))
print("number = 1,4 output ",minNum(arr=[1,4]))
# test list     
print("number = 1,10,20 output ",minNum(arr=[1,10,20]))
print("number = 1,2,3,4,5,6 output ",minNum(arr=[1,2,3,4,5,6]))
print("number = 2,3,4,5,6 output ",minNum(arr=[2,3,4,5,6]))
