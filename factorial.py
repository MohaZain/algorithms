# Factorial o!
# Ref: https://coderhub.sa/challenge/c617fadc-c5de-4265-8bf5-f7cca98a4572
# Example:
# Input: number = 5
# 5! = 1 * 2 * 3 * 4 * 5 = 120
# Output = 120
def factorial(number):
  # write your code here
  fact = 2
  for i in range(3,number+1):  
      fact = i * fact
  return fact

# ---------------------Test----------------------------

print(factorial(5))