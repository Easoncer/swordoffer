# aha algrorithm


def dfs(step,ts):
	if step==len(a):
		result.append(''.join(a))
		return

	for i in range(len(a)):
		if book[i]==0:
			a[step]=ts[i]
			book[i]=1
			dfs(step+1,ts)
			book[i]=0
	return 

if __name__=="__main__":
	book=[0 for i in range(0,10)]
	n=4
	ss="aab"

	ts=list(ss)
	result=[]
	n=len(ts)
	book=[0 for i in range(len(ts))]
	a=[0 for i in range(len(ts))]
	dfs(0,ts)
	a=list(set(result))
	a.sort()
	print a
	# a=list(set(list(ss).sort()))
	# print a
	# dfs(1)
	# print 0

