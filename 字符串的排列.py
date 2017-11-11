# aha algrorithm


def dfs(step):
	if step==n:
		result.append(''.join(a))
		return

	for i in range(len(ts)):
		if book[i]==0:
			a[step]=ts[i]
			book[i]=1
			dfs(step+1)
			book[i]=0
	return 

if __name__=="__main__":
	book=[0 for i in range(0,10)]
	n=4
	ss="aad"

	ts=list(ss)
	result=[]
	ts.sort()
	n=len(ts)
	book=[0 for i in range(n)]
	a=[0 for i in range(n)]
	dfs(0)
	print list(set(result))
	# a=list(set(list(ss).sort()))
	# print a
	# dfs(1)
	# print 0

