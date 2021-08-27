import csv
file1="final.csv"
inp=[]
out=[]

with open(file1,'r') as f1:
	csvreader=csv.reader(f1,delimiter=';')
	for row in csvreader:
		inp.append(row)

for row in inp:
	print row
	print "\n"
	if row[1]!='':
		if row[1]!='0':
			out.append(row)
			print row
			print "\n"

with open("output1.csv", "w") as f:
    writer = csv.writer(f,delimiter=';')
    writer.writerows(out)
	
