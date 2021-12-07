# Builds the hash table
# By: Jack Galassi, Meghan Novak, Kaitlyn Fare, Meredith Heller

from student import student
from pybst import splaytree


# reads in each line (lines should consist of each student field delimited by commas) to a list of students, return the list
# Params:
# 	filename: a string of an existing file in the same directory
# Return:
# 	list of student objects
def readdata(filename):

	f = open(filename, 'r')

	students = list()
	i = 1;
	for line in f:
		the_line = line.split(',')
		if(len(the_line) == 3):
			full_name = the_line[0] + " " + the_line[1]
			s = student(full_name, the_line[2].rstrip(), i)
			students.append(s)
			i+=1

	f.close()
	return students


# runs algorithm on a given string word to return the phonetic hashing string codestring
# Params:
# 	word: a string that represents the name or phrase to be converted to a phonetic hash
# Return:
#		the phonetic hash string
def get_code(word):
	code = ['', '', '', '']
	index = 0
	prevletter = word[0].upper()
	for letter in word:
		if(not(letter.isalpha())): continue;
		if(index > 3): break;
		letter = letter.upper()
		if(letter == 'B' or letter == 'F' or letter == 'P' or letter == 'V'):
			code[index] = 1
		elif(letter == 'C' or letter == 'G' or letter == 'J' or letter == 'K' or letter == 'Q' or letter == 'S' or letter == 'X' or letter == 'Z'):
			code[index] = 2
		elif(letter == 'D' or letter == 'T'):
			code[index] = 3
		elif(letter == 'L'):
			code[index] = 4
		elif(letter == 'M' or letter == 'N'):
			code[index] = 5
		elif(letter == 'R'):
			code[index] = 6

		if(index > 0):
			if(prevcode == code[index] and (prevletter == 'A' or prevletter == 'E' or prevletter == 'I' or prevletter == 'O' or prevletter == 'U' or prevletter == 'Y')):
				prevcode = code[index]
				index += 1
			elif(prevcode != code[index] and letter != 'A' and letter != 'E' and letter != 'I' and letter != 'O' and letter != 'U' and letter != 'Y' and letter != 'H' and letter != 'W'):
				prevcode = code[index]
				index += 1
     
		if(index == 0):
			prevcode = code[index]
			code[index] = letter
			index +=1
		
		prevletter = letter

	while(index < 4):
		code[index] = 0
		index+=1

	# convert the list to a string
	codestring = ""
	for element in code:
		if( type(element) == int):
			codestring+=str(element)
		else:
			codestring+=element
	return codestring



# go through the list of students and build python dictionary (hash table)
# key in dictionary: student name hash string
# value in dictionary: splay tree
# if the key is already in the dictionary, add a node in the splay tree for that student
# if the key is not in the dictionary, make a new splay tree and insert a node for that student
# Params:
# 	students: a list of student objects
# Return:
#		a dictionary in of phonetic hash string keys, splay tree values
def buildhash(students):

	codes = dict()
	for s in students:
		sCode = get_code(s.fname)
		# the string is already in the hash, means splay tree is already in just add a node
		if sCode in codes.keys():
			codes[sCode].insert(s.idnum, s)
		# the string is not in the hash, add it and create new splay tree with information
		else:
			codes[sCode] = splaytree.SplayTree([[s.idnum, s]])
	# print codes['J525'].get_element_count()
	stuff = codes['J525'].levelorder
	return codes



# TESTING:
# a single student instance
# studentA = students[0]
# studentAHash = get_code(studentA.fname)
# studentATree = codes[studentAHash]

# test get_element_count function
# count = studentATree.get_element_count()

# test: check to make sure there are 15 splay trees with at least 8 nodes
# params: codes, a python dictionary containing value of type splay tree
# prints how many splay trees have at least 8 nodes
def testNumBigSplays(codes):

	numBigSplays = 0
	for hashString in codes:
		count = codes[hashString].get_element_count()
		if count > 7:
			numBigSplays+=1
	print "There are " + str(numBigSplays) + " splays with at least 8 nodes."
