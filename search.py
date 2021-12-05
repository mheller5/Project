# this file contains the search implementation of our data structures project

import buildhash
from student import student
from pybst import splaytree
from pybst import bstree
import collections


BSTree = bstree.BSTree


def main():
	# read the data into a list of student objects
	students = buildhash.readdata('data.txt')
	# create a python dictionary containing student splay trees
	codes = buildhash.buildhash(students)
	userSearch(codes)


def userSearch(codes):

	# prompt user for searches until they quit
		# get the search string
		# send it to print results
		# result = printResults(code, codes)

		code = 'J525'
		studentNum = 0
		# check whether the code is in the
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
			userChoice = 3 # MEGHAN CHANGE THIS TO USER INPUT
			key = results[numResults - userChoice].key
			# updateSplayTree(code, codes, key)
	
		else:
			print 'Could not find any student matches. Please try spelling their name another way.'
		# prompt user for a new search or to quit
		
	
# Jack's part
# def updateSplayTree(code, codes, key):
	# access the splay tree (the item in codes at code, find the node with key arg using the function in splaytree documentation)
	



if __name__ == "__main__":
	main()
