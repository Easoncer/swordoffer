def quickSort(templist,left,right):
	if left<right:
		temp=partition(templist,left,right)
		quickSort(templist,left,temp-1)
		quickSort(templist,temp+1,right)

def partition(templist,left,right):
	key=templist[right]
	i=left
	for j in range(left,right):
		if templist[j]<key:
			temp=templist[j]
			templist[j]=templist[i]
			templist[i]=temp
			i+=1
	temp=templist[i]
	templist[i]=templist[right]
	templist[right]=temp
	return i

if __name__=="__main__":
	array=[8,10,9,6,16,5,13,26,18,2,45,34,23,1,7]
	quickSort(array,0,len(array)-1)
	print array	


