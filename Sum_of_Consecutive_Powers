"""This problem was tricky. Given a range, it asked to return all the numbers in that range where the number (N) was equal too the
sum of each individual digit raised to the consecutive power. For example: 89 = 8^1 + 9^2. Also, 135 = 1^1 + 3^2 + 5^3. The goal was
to find the numbers that satisfied that quality given a certain range. Good learning tool for those who haven't used imap before."""


from itertools import imap

def sum_pow(n):
    digit_list = []
    sum = 0
    for x in str(n):
    	digit_list.append(int(x))
    sqs_list = list(imap(pow, digit_list, list(range(1,len(digit_list)+1))))
    for x in sqs_list:
    	sum += x
    if sum == n:
    	return True
    else:
    	return False
      
#testing my first funcion
print sum_pow(1676)

def sum_dig_pow(a, b):
	
    return_list = []
    for x in range(a,b+1):
    	if sum_pow(x)== True:
      		return_list.append(x)
    return return_list

#just a test
print sum_dig_pow(500,3000)
