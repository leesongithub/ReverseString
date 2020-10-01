# This is a Python script to reverse a string.
# Leeson Chen
# September 15 2018

words = input("Enter the string to be reversed: ")
for x in range(len(words)):
	#print x
	print words[len(words) - x - 1],
	# adding a comma to the end stops a new line from printing
	
# jesus h christ python is so easy to use
# I love you smart snek

#Or a simpler one using string slicing

words=words.split()
words=words[::-1]
print(*words)
