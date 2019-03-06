#Given 2 strands of DNA this is a basic program to count
#the number of differences/point mutations

with open('rosalind_hamm.txt', 'r') as f:
	strand1 = f.readline()
	print "strand 1 = ", strand1
	strand2 = next(f)
	print "strand 2 = ", strand2
	#print(len(strand1))
	#print(len(strand2))
	cnt = 0
	for i in xrange(len(strand1)):
			if strand1[i] != strand2[i]:
				cnt+=1
	print("amount of mutations: ", cnt)

