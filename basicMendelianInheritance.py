with open('rosalind_iprb.txt', 'r') as f:
	line = f.readline()
	k = float(line[:2])
	m = float(line[3:5])
	n = float(line[6:8])
	print(k, m, n)
	tot = float(k+m+n)
	print (1 - (n/tot)*((n-1)/(tot-1)) - (n/tot)*(m/(tot-1)) - (m/tot)*((m-1)/(tot-1))*0.25)
