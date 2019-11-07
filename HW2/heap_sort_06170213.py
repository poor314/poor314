def heapify(A,size,i):
    l=2*i+1 #左子節點
    r=2*i+2 #右子節點
    largest=i #i=最大
    
    if l<size and A[l]>A[largest]:
        largest=l 
        
    if r<size and A[r]>A[largest]:
        largest=r
        
    if largest!=i:
        A[i],A[largest]=A[largest],A[i] #交換
        
        heapify(A,size,largest)
        
        
def heapsort(A):
    size=len(A)
    
    for i in range(size,-1,-1):
        heapify(A,size,i)
    
    for i in range(size-1,0,-1):
        A[i],A[0]=A[0],A[i] #交換
        
        heapify(A,i,0)
        
A=[12,1,13,5,26,7,33]
heapsort(A)
print(A)
