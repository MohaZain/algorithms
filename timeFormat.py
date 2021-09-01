# Convert time between 24 to 12  
# Ref: https://coderhub.sa/challenge/627b881a-1624-4521-9f90-6f54b07e6faa
# Example:
# Input: time = 13:40 
# Output binary = '1010011'
def convert_time(time):
  if time[-2:len(time)] == 'am':
    if time[0:2] == '12':
      return '00'+time[2:5]
    else : return time[0:-2]
  elif time[-2:len(time)] == 'pm':
     ti = time.split(":")
     x = int(ti[0]) + 12  
     return str(x)+':'+ti[1][:-2]
  else:
     ti = time.split(":")
     if ti[0] >= '13':
        x = int(ti[0]) - 12
        return str(x)+':'+ti[1]+' pm'
     else:
        return time+' am'
  # return converted_time

# ---------------------Test----------------------------

print('Input 13:40 Output ',convert_time('13:40'))
print('Input 6:20 pm Output ',convert_time('6:20 pm'))