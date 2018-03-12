def BubbleSort(list123) :
  n = len(list123)
  for i in range(n - 1) :
  #total number of comparison
    for j in range(n - i - 1) :
    #number of values for comparison in each loop
      if list123[j] > list123[j + 1] :
        #if the first value in each pair is greater, swith them
        tmp = list123[j]
        list123[j] = list123[j + 1]
        list123[j + 1] = tmp
  return list123



if __name__=='__main__':
	TestList=[42,12,999,75,19,-100,7,4,0,0,7,-2,3,-999,6]
	print(BubbleSort(TestList))
