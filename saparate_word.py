# Separate words at a capital letter by placing a space and converting it to a lowercase letter
# Ref: https://coderhub.sa/challenge/e35bb082-6cc1-4aa9-89f5-03077f5ab9f3
# Example:
# Input: helloWorld!
# Output = hello world!
def cap_space(txt):
  # write your code here
  res = ''
  indx = []
  for i in range(len(txt)-1):
    if txt[i].isupper():
      indx.append(i)
  for i,num in enumerate(indx):
    txt = txt[:indx[i]+i] + " " + txt[indx[i]+i:]
  return txt.lower()

# ---------------------Test----------------------------

print(cap_space('helloWorld!'))