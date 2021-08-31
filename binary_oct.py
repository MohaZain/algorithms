# Convert binary to octal 
# Ref: https://coderhub.sa/challenge/5bd914c3-ab6d-49df-bf9b-5c01ef189974
# Example:
# Input: binary = "10011100"
# Output: oct = "234"

def binary_oct(bainry):
    decim = 0
    indx = len(bainry) - 1
    for i in range(len(bainry)):
      if int(bainry[indx]) == 1:
        decim = decim + (2**i)
      indx = indx - 1    
    decim = int(decim)
    oct_indx = 1
    octi = ''
    oct_indx_zeros = 1
    x = 0
    while (decim != 0):
      x = int(decim / oct_indx)
      if x == 0: 
        octi = octi + str(decim)
        decim = 0
        oct_indx_zeros = oct_indx
        break
      if  x <= 7:
        octi = octi + str(x)
        decim =  decim - oct_indx * x
        oct_indx_zeros = oct_indx
        oct_indx = 1
      oct_indx = oct_indx * 8
    if x != 0 :
        while(oct_indx_zeros !=1 ):
            octi = octi + '0'
            oct_indx_zeros = int(oct_indx_zeros / 8)
    return 'Oct = '+octi

# ---------------------Test----------------------------
bainry = '10011100'
print(binary_oct(bainry))
print("Oct = 234")