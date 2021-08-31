
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
        print(x,oct_indx_zeros,oct_indx)
        oct_indx_zeros = oct_indx
        oct_indx = 1
      oct_indx = oct_indx * 8
    if x != 0 :
        while(oct_indx_zeros !=1 ):
            octi = octi + '0'
            print(oct_indx_zeros)
            oct_indx_zeros = int(oct_indx_zeros / 8)
    return octi
bainry = '10011100'
# 25
x = binary_oct(bainry)
print(x)