# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which 
# are multiples of both three and five print "FizzBuzz"

count = 0
while count < 101:
	if (count % 3 == 0) and (count % 5 == 0):
		print "FizzBuzz"
		count += 1
	elif (count % 3 == 0):
		print "Fizz"
		count += 1
	elif (count % 5 == 0):
		print "Buzz"
		count += 1
	else:
		print count
		count += 1
