def search2(a,key):
	low=0
	high=len(a)-1
	while low<=high:
		mid=(low+high)/2
		if a[mid]<key:
			low  = mid+1
		elif a[mid]>key:
			high = mid-1
		else :
			return a[mid]
	return -1

if __name__=="__main__":
	a=[3,5,6,8,9,12,34,36]
	print search2(a,8)

