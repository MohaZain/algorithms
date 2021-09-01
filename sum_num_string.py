# function receives two string values, if the two inputs contain numbers add the numbers 
# and if one of the inputs contains characters, returns -1 
# Ref: https://coderhub.sa/challenge/033163c2-91be-4f1b-b0c0-01aff0811448
# Example:
# Input: num1 = '4' num2 = '6'
# Output = '10'
def addStrNums(num1, num2):
	# write your code here
  try:
    num1_int = int(num1)
    num2_int = int(num2)
    return str(num1_int + num2_int)
  except:
    return -1
  
# ---------------------Test----------------------------

print(addStrNums('1','5'))
