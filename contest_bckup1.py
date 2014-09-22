#!/usr/bin/env python3
import math

#cord = [(1,1),(5,5),(3,9),(10,10),(100,100),(3,3),(4,4),(2,2)]

cord = []

from random import randrange as randi

'''for i in range(100000):
    cord.append((randi(1,10000), randi(1,10000)))

cord.append((1,1))
cord.append((2,1))
cord.append((10,10))'''

#code to take inputs from STDIN

first_inp = input()

topics, questions, queries = tuple(first_inp.split())

topic_id = {}
question_id = {}
query_id = []

for i in range(int(topics)):
	t_id, x_axis, y_axis = tuple(input().split())
	topic_id[int(t_id)] = (float(x_axis), float(y_axis))
	cord.append((float(x_axis), float(y_axis)))

for i in range(int(questions)):
	q_line = input().split()
	q_id = int(q_line[0])
	q_num = tuple(map(int, q_line[2:]))
	question_id[q_id] = q_num

for i in range(int(queries)):
	raw_qid = input().split()
	qid = []
	qid.append(raw_qid[0])
	qid.append(raw_qid[1])
	qid.append(tuple(map(float, raw_qid[2:])))
	query_id.append(qid)

#code to read input ends #

x = int(input("enter the value: "))
y = int(input("enter the value: "))

k = int(input("enter how many nearest elements you want: "))

point = (0.0,0.0)

dist = []

maindict={}

maxl1=0;maxdist=0;maxcord=()

for i in range(k):
	d = (math.sqrt((point[0] - cord[i][0])**2 + (point[1] - cord[i][1])**2))
	l1 = (abs(point[0] - cord[i][0]) + abs(point[1] - cord[i][1]))

	if(l1>maxl1):
		maxl1 = l1;
	if(d>maxdist):
		maxdist = d;
		maxcord = cord[i]

	dist.append(d)
	dist.append(l1)

	maindict[cord[i]] = dist;
	dist=[]

for j in range(k,len(cord)):
	newl1 = (abs(point[0] - cord[j][0]) + abs(point[1] - cord[j][1]))
	if(maxl1 < newl1):
		#do nothing
		pass
	else:
		#check and update max
		d = (math.sqrt((point[0] - cord[j][0])**2 + (point[1] - cord[j][1])**2))

		if(d < maxdist):

			del maindict[maxcord]
			maxdist = d;
			maxcord = cord[j]

			dist.append(d)
			dist.append(newl1)

			maindict[maxcord] = dist

			dist=[]
			
			#update max;
			for keys in maindict:
				if(maindict[keys][0] > maxdist):
					maxdist = maindict[keys][0]
					maxcord = keys

				maxl1 = maindict[maxcord][1]

		else:
			#do nothing
			pass

print(maindict)

tmp = []

for neighbours in maindict:
	for comp in topic_id:
		if topic_id[comp] == neighbours:
			tmp.append(comp)
			break

print(tmp)