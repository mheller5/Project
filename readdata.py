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
