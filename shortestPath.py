_=float('inf')

def ShortestPath(graph,n):
	distance=[0]*n
	flag=[False]*n
	step=[0]*n
	flag[0]=True
	k=0
	for i in range(n):
		distance[i]=graph[k][i]

	for j in range(n-1):
		connect=_
		for i in range(n):
			if distance[i]<connect and not flag[i]:
				connect=distance[i]
				k=i
                # not connet with each other  
		if k==0: 
			return
		flag[k]=True
		for i in range(n):
			if distance[i]>distance[k]+graph[k][i]:
				distance[i]=distance[k]+graph[k][i]
				step[i]=k
#		print(k)
	return distance,step


if __name__=='__main__':
	n=6
	MyGraph=[
			[0,6,3,_,_,_],
			[6,0,2,5,_,_],
			[3,2,0,3,4,_],
			[_,5,3,0,2,3],
			[_,_,4,2,0,5],
			[_,_,_,3,5,0],
			]
	distance,step=ShortestPath(MyGraph,n)
	print(distance)
	print(step)
