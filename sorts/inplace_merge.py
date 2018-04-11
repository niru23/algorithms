
def merge_sort(a,l,r):
    if l< r:
       m =(l+(r-1))/2
       merge_sort(a,l,m)
       merge_sort(a,m+1,r)
       merge_inplace(a,l,m,r)
        
def merge_inplace(a,l,m,r):
    n1 =m-l+1
    n2 =r-m
    # create temp array
    L=[0]*n1
    R=[0]*n2
    # copy data into temp array
    for i in range(0,n1):
        L[i] =a[l+i]
    for i in range(0,n2):
        R[i] =a[m+1+i]
    i =0
    j =0
    k =1
    while i < n1 and j <n2:
          if L[i] <=R[j]:
              a[k] =L[i]
              i+=1
          else:
              a[k] =R[j]
              j+=1
          k+=1
    if i < n1:
       a[k] =L[i]
       i+=1
       k+=1
    if j< n2:
       a[k] =R[j]
       j+=1
       k+=1
    
aa = [54, 26, 93, 17, 77, 31, 44, 55, 20]       
merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20],0,8)        
print aa
