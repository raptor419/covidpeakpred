f=open("only_function.txt").read()
f=f.split("\n")
arr=[]

for i in range(0,len(f),11):
	arr.append(f[i:i+11])

for i in range(len(arr)):
	a=(arr[i][6])
	b=arr[i][7]
	# print(a)
	a=a.replace('  result = (unsigned int)','')
	if('*(_BYTE *)a1' in a):
		a=a.replace('*(_BYTE *)a1','a1[0]')
	a=a.replace('*(_BYTE *)','')
	a=a.replace('(a1 + ','a1[')
	a=a.replace(') ','] ')
	a=a.replace('));','] ')[1:]
	# print('s.add')
	b=b.split()[-2]
	print('s.add(('+a+')=='+b+')')
