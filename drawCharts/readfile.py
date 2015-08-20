import io
from pylab import *
import datetime

format = '%Y-%m-%d %H:%M:%S'

def str_to_index(time):
	t = datetime.datetime.strptime(time, format)
	hour = t.timetuple().tm_hour
	mins = t.timetuple().tm_min
	index = hour*30 + mins/2
	return index

date = "2015-08-19"
f = open('1440042030961_sportdata.txt')
resere = 0
x = []
y = []
y2 = []
i = 0
for line in f:
	# print line
	
	data = line.split(',')
	time = data[0]
	# str_to_index(time)
	walk = int(data[1])
	run = int(data[2])
	fastrun = int(data[3])
	allsport = walk + run + fastrun
	vigor = int(data[5])
	walkdog = int(data[6])
	vigor = (vigor*vigor)/float(54054)

	if date in data[0]:
		index = str_to_index(time)
		cur_index = len(x)
		while index > cur_index:
			x.append(cur_index)
			y.append(0)
			y2.append(0)
			cur_index += 1
		x.append(index)
		y.append(walkdog)
		y2.append(allsport)
		resere += int(data[5])
		# print data[0] + '\t' + str(int(data[1]) + int(data[2]) + int(data[3])) +'\t' + str(walkdog)
# print 'total: ' + str(resere)
print x
print y
plot(x,y)
plot(x,y2)
show()