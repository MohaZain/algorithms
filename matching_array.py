# Matching Array 
# Ref: https://coderhub.sa/challenge/5eaa3159-d969-41d5-8401-85dd7d59fbe2
# Example:
# Input: arr1 = ['w','s'] arr2=['s','w']
# Output = true
def match_arrays(array1, array2):
	# write your code here
  if len(array1) != len(array2):
    return False
  for word in array1:
    if word not in array2:
      return False
  return True
# ---------------------Test----------------------------
arr1 = ["word1", "wo", "word2"]
arr2 = ["word2", "word1", "wo"]
print(match_arrays(arr1,arr2))
