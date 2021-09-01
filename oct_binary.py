# Convert from octal to binray
# Ref: https://coderhub.sa/challenge/44be3e9f-8b91-495d-91f2-c514693ff190
# Example:
# Input: octal = 123 
# Output binary = '1010011'
def oct_to_bin(octal):
	# write your code here
  octal = str(octal)
  indx = len(octal)-1
  dec = 0
  # oct to dec
  for i in range(len(octal)):
    dec = dec + int(octal[indx]) * (8**i)
    indx -= 1
  binary = ''
  # dec to binary
  while(dec != 0):
    div_remain = dec % 2
    dec = dec / 2
    binary = str(div_remain) + binary
  return binary

# ---------------------Test----------------------------

print(oct_to_bin(123))
