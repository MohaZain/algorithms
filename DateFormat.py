from datetime import datetime

# Format date with type string with diffrent style 
# Ref: https://coderhub.sa/challenge/c93a5e09-2578-42ec-95db-88d1e87d6459
# Example:
# Input: date = "2019/02/14"
# Output: "2019/02/14 | 2019-02-14 | 02/14/2019"

# Solution 1
def date_format_1(date):
  # write your code here
  date_object_fromat1 = datetime.strptime(date, '%Y/%m/%d').date()
  date_object_format2 = date_object_fromat1.strftime('%m/%d/%Y')
  return date+' | '+ str(date_object_fromat1)+' | '+str(date_object_format2)
  
# Solution 2  
def date_format_2(date):
  # write your code here
  f1 = date.replace("/", "-")
  f2 = date[4:7].replace("/", "") +'/'+date[7:len(date)].replace("/", "") +'/'+date[0:4]
  return date+' | '+f1+' | '+f2

# ---------------------Test----------------------------
date = "2019/02/14"
print(date_format_1(date))
print(date_format_2(date))
print("2019/02/14 | 2019-02-14 | 02/14/2019")