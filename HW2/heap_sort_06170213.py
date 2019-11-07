def heapify(A,size,i):
    l=2*i+1 
    r=2*i+2 
    largest=i 
    
    if l<size and A[l]>A[largest]:
        largest=l
        
    if r<size and A[r]>A[largest]:
        largest=r
        
    if largest!=i:
        A[i],A[largest]=A[largest],A[i] 
        
        heapify(A,size,largest)
def heapsort(A):
    size=len(A)
    
    for i in range(size,-1,-1):
        heapify(A,size,i)
    
    for i in range(size-1,0,-1):
        A[i],A[0]=A[0],A[i]
        
        heapify(A,i,0)
        
A=[12,1,13,5,26,7,33]
heapsort(A)
print(A)
