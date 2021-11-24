# Builds the hash table
# By: Jack Galassi, Meghan Novak, Kaitlyn Fare, Meredith Heller

from student import student

# read in each line (which is a student) to a list of students
f = open('data.txt', 'r')

students = list()
for line in f:
	the_line = line.split(',')
	if(len(the_line) == 3):
		full_name = the_line[0] + " " + the_line[1]
		s = student(full_name, the_line[2].rstrip())
		students.append(s)

f.close()

# runs algorithm on a given string word to return the phonetic hashing string codestring
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



# go through the list of students and hash each name
# currently incrementing the value, in the future implement splay tree
codes = dict()
for s in students:
	sCode = get_code(s.fname)

	if sCode in codes.keys():
		codes[sCode] +=1
	else:
		codes[sCode] = 1
		
print(codes)



