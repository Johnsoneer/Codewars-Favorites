def count_ones(n):
	
    count = 0
    list_n = []
    bins = bin(n)
    for x in str(bins):
    	list_n.append(x)
    for x in list_n[2:len(list_n)+1]:
    	if x == '1':
        	count += 1
    return count

def bits_war(numbers):
    
    count_even = 0 
    count_odd = 0
    for x in numbers:
    	if x % 2 == 0 and x > 0:
        	count_even += count_ones(x)
        elif x%2 == 0 and x < 0:
        	count_even -= count_ones(x)
        elif x%2 != 0 and x > 0:
        	count_odd += count_ones(x)
        elif x%2 != 0 and x < 0:
        	count_odd -= count_ones(x)

    if count_even < count_odd:
    	 return "odds win"
    if count_even > count_odd:
    	return "evens win"
    else:
    	return "tie"
