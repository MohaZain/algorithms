
def binary_oct(bainry):
    decim = 0
    indx = len(bainry) - 1
    for i in range(len(bainry)):
      if int(bainry[indx]) == 1:
        decim = decim + (2**i)
      indx = indx - 1
    # write your code here
    decim = int(decim)
    print(decim)
    oct_indx = 1
    octi = ''
    while (decim != 0):
      x = int(decim / oct_indx)
      if x == 0: 
        octi = octi + str(decim)
        decim = 0
        break
      if  x <= 7:
        octi = octi + str(x)
        decim =  decim - oct_indx * x
        oct_indx = 1
      oct_indx = oct_indx * 8
    return octi
bainry = '10011'
# 25
x = binary_oct(bainry)
print(x)