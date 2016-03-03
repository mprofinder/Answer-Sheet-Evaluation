import collections, re

import reg1
import sys

#To read all the inputs from the file
reader = open('train.tsv', 'r' )
SET = 1
for row in reader:
	line = row.split('\t')
	if not line[1] == str(SET):  continue
	Id = int(line[0])
	s1 = int(line[2])
	text = line[4]
	exp = []
	exp=reg1.reg()
	if any(regex.match(text) for regex in exp):
		print ('Some regex matched!')
		print('Id:\t%d' % Id)	
		print ("\n") 
		print ('Score:\t%d' % s1)
		print ("\n")
		print ('Text:\t%s' % text)
		print ("\n")
		




