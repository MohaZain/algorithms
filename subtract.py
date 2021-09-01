# subtract two number without using minus sign
# Ref: https://coderhub.sa/challenge/049c4598-d2da-4bae-9024-addfac853799
# Example:
# Input: number = 10,8
# 8 + (2) = 10
# Output = 2
def subtract(num1, num2):
	# write your code here
  les_num = 0
  lar_num = 0

  result = 0
  num = 1
  is_true = True

  if num1 < num2:
	  les_num = num1
	  lar_num = num2
  else:
	  les_num = num2
	  lar_num = num1
  while(is_true):
    if les_num + num == lar_num:
        result = num
        is_true = False
    num += 1
  if num1 < num2: return result * -1
  return result

# ---------------------Test----------------------------

x = subtract(33,60)
print(x)