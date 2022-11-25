# Code by @AmiMotefaker

# Find Armstrong Number in an Interval

# Armstrong Number:
# In numerical number theory, the Armstrong number# definition is:
# the number in any given number base, which forms the total of the same number, 
# when each of its digits is raised to the power of the number of digits in the number.

# For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.


## check Armstrong numbers between lower and upper number
lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
