# this file contains the search implementation of our data structures project

import buildhash
from student import student
from pybst import splaytree

# Main Driver
def main():
	# read the data into a list of student objects
	students = buildhash.readdata('data.txt')
	# create a python dictionary containing student splay trees
	codes = buildhash.buildhash(students)
	userSearch(codes)

# Drives user search by continuously:
# 	1. Asking for a student name
# 	2. Read input and convert to hash
# 	3. Retrieve and display level order hash splay results
# 	4. Ask for a selection
# 	5. Call to splay the selected result
#	Until user enters q
# Params:
#		codes: the dictionary containing all hash's splay trees
def userSearch(codes):

	# prompt user for searches until they quit
		# get the search string
		# send it to print results
		# result = printResults(code, codes)
	while(1):

		name = raw_input("Enter student name (or q to quit): ")

		
		if name == "q":
			break

		code = buildhash.get_code(name)
		studentNum = 0

		# check whether the code is in the dict
		if code in codes.keys():
			numResults = codes[code].get_element_count()
			results = codes[code].postorder()

			# go through list in reverse order
			listIndex = numResults - 1
			while listIndex >= 0:
				studentNum +=1
				print str(studentNum) + ': ' + results[listIndex].value.fname + ' ' + results[listIndex].value.email + ' ' + str(results[listIndex].value.idnum)
				listIndex-=1

			# ask user for the number they would like to pick or to press 0 if none are correct
			userChoice = raw_input("Enter number (or 0 if no matches): ")

			if int(userChoice) is 0:
				continue

			key = results[numResults - int(userChoice)].key
			# updateSplayTree(code, codes, key)
	
		else:
			print 'Could not find any student matches. Please try spelling their name another way.'
		
	
# Jack's part
# **** After you finish your code, uncomment line 58 so that the part above can implement your function ****
# def updateSplayTree(code, codes, key):
	# access the splay tree (the item in codes at code, find the node with key arg using the function in splaytree documentation)
	



if __name__ == "__main__":
	main()
