import collections, re

import regg1,reg2
import sys

#To read all the inputs from the file
reader = open('train.tsv', 'r' )
SET = 1
count1= 0
pats = []
pats.append( re.compile(r"(\w+ ){0,100}((what)|(which)|(type of)|(conditions)) (\w* ){0,10}((drying)|(dry))\w*") )#6
#pats.append( re.compile(r"[\w+|\. ]{0,100}((what)|(which)|(type of)|(conditions)) (\w* ){0,10}((drying)|(dry))\w*") )
for row in reader:
	line = row.split('\t')
	if not line[1] == str(SET):  continue
	Id = int(line[0])
	text = line[4]
	for reg in pats:
		if(re.match(reg,text)):
			print(reg)
			print("\n")
			print(Id)
			print(text)
			count1=count1+1
			print('-----------------------------------------\n')

	'''for reg in exp:
		if(re.match(reg,text)):
			#print("\n")
			#print(text)
			#print("-----------------\n")
			count1=count1+1;
		
		for i in exp:					 
		if any(regex.match(text) for regex in exp):
			print('Id:\t%d' % Id)'''
		 
	#if any(regex.match(text) for regex in exp):
	#	print ('Some regex matched!')
	#	print('Id:\t%d' % Id)	
	#	print ("\n") 
	#	print ('Score:\t%d' % s1)
	#	print ("\n")
	#	print ('Text:\t%s' % text)
	#	print ("\n")'''

#if(regex.match(es) for regex in exp):
#	print("It has matched\n")
#	print(exp[regex])'''


print (count1)

'''SET=2
count2=0
for row in reader:
	line = row.split('\t')
	if not line[1] == str(SET):  continue
	Id = int(line[0])
	text = line[2]
	#print(Id)
	print("\n")
	for reg in exp2:
		if(re.match(reg,text)):
			#print("\n")
			#print(text)
			#print("-----------------\n")
			count2=count2+1;
print(count2)'''	
