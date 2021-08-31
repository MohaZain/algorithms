def oddsVsEvens(num):
  # write your code here
  count_odd = 0
  count_even = 0
  for i in range(num+1):
      u =  i % 2 
      print(i,' remain = ', u)
      if (i % 2) == 0:
        count_even = count_even + i
      else:
        count_odd = count_odd + i
  print('even = ',count_even,'odd=', count_odd)
  if count_even > count_odd: 
    return 'even'
  elif count_even < count_odd:
    return 'odd'
  else: 
      return 'equal'
      
number = 20
print(oddsVsEvens(number))
# print("Oct = 234")