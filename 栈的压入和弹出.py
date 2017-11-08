def IsPopOrder( pushV, popV):
	# write code here
	temp=[]
	for i in pushV:
		temp.append(i)
		while len(temp) and temp[-1]==popV[0]:
			temp.pop()
			popV.pop(0)

	return True if len(temp) is 0 else False

if __name__=="__main__":
	print IsPopOrder([1,2,3,4,5],[4,5,3,2,1])
