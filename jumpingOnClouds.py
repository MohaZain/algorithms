# The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads.
# For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.
# Ref: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Example:
# input = [0 0 0 0 1 0]
# output = 3
def jumpingOnClouds(c):
    # Write your code here
    jumb_c = 0
    can_jum = []
    for i in range(len(c)):
      if c[i] == 0:
        can_jum.append(i)

    for i in range(len(can_jum)):
      if i == 0 or i == len(can_jum)-1:
        continue
      if can_jum[i] - can_jum[i-1] == 1 and can_jum[i+1] - can_jum[i]  == 1:
        can_jum.pop(i)
    jumb_c = len(can_jum)-1
    return jumb_c
    # ---------------------Test----------------------------

path =[0,0,1,0,0,1,0]
print(jumpingOnClouds(path))
# output = 4  ,
