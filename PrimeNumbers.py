# Fun to find Prime numbers in array 
# Ref: https://coderhub.sa/challenge/d122bc96-d15b-483f-8fda-c937c8bcd833
# Example:
# Input: nums = [53, 20, 71]
# Output: [53, 71]
def primes_nums(array):
  # write your code here
  arr_prime =[]
  for num in array:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
          is_prime = False
    if is_prime:
      arr_prime.append(num)    
  return arr_prime


# ---------------------Test----------------------------
arr1 = [53, 20, 71]
x = primes_nums(arr1)
print(x)