# this file contains the search implementation of our data structures project

import buildhash
from student import student
from pybst import splaytree


def main():
	# read the data into a list of student objects
	students = buildhash.readdata('data.txt')
	# create a python dictionary containing student splay trees
	codes = buildhash.buildhash(students)
	# printResults('J525', codes)
	# printResults('H76', codes)


def userSearch(codes):

	# prompt user for searches until they quit
		# get the search string
		# send it to print results
		result = printResults(code, codes)
			# prompt user to enter the number depending on their pick if printResults did not return 0
			# call function to splay that student to the top
		# continue looping through 
		 
#Meredith's part
# prints the elements in the splay tree using a level order traversal so most recent are at top
# Params:
# 	code: the hash string of the looked up name
# 	codes: the dictionary containing all hashes and their splay trees in the data
# Return:
# 	returns the number of students in the splay tree for its code in codes, or 0 if the search isn't in codes
def printResults(code, codes):
	studentNum = 0
	# check whether the code is in the
	if code in codes.keys():
		numResults = codes[code].get_element_count()
		# self.codes[code].levelorder()
		
		# print type(splaytree.levelorder(codes[code]))
		print numResults
		return numResults
	else:
		print 'Could not find any student matches. Please try spelling their name another way.'
		return studentNum
		
	
# Jack's part
# def updateSplayTree():
	
	
	



if __name__ == "__main__":
	main()
