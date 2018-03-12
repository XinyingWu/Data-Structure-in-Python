def MergeSort(seq):
	if len(seq)<=1:
		return seq
	mid=int(len(seq)/2)
	left=MergeSort(seq[:mid])
	right=MergeSort(seq[mid:])
	return merge(left,right)

def merge(left,right):
	result=[]
	i = 0
	j = 0
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	result+=left[i:]
	result+=right[j:]
	return result

if __name__=='__main__':
	TestList=[42,12,999,75,19,-100,7,4,0,0,7,-2,3,-999,6]
	print(MergeSort(TestList))
	
