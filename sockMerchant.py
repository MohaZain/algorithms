# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# Ref: https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Example:
# Input: color = [10, 20, 20, 10, 10, 30, 50, 10, 20] , num of pair (length) = 9
# Output = 3
# there is 2 pair of color 10 and one pair of color 20
def sockMerchant(n, ar):
    # Write your code here
    num_use = []
    pair = 0
    for num in ar:
      if num in num_use:
        continue
      sock_pair = ar.count(num)
      if sock_pair % 2 == 1:
        sock_pair = sock_pair - 1

      sock_pair = sock_pair / 2
      pair = pair + sock_pair
      num_use.append(num)
    return pair

    # ---------------------Test----------------------------

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9
print(sockMerchant(n, ar))
