# Reads in student data and stores it in a student array

from student import student

f = open('data.txt', 'r')

students = list()
for line in f:
	the_line = line.split(',')
	if(the_line == 3):
		s = student(the_line[0], the_line[1], the_line[2])
		students.append(s)

f.close()

codes = dict()
for s in students:
	found = 0
	sCode = get_code(s)

	for key in codes:
		if key == sCode:
			codes[sCode] += 1
			found = 1

		if found == 0:
			codes[sCode] = 1
