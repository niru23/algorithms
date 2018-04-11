#!/usr/bin/python

'''
simple quick sort algorithm best case nlog(n) worst case n2
using recursion
'''

def quick_sort(array,start,end):
    # partition the list
    if start < end:
        pivot=partition(array,start,end)
         # sort both halves
        quick_sort(array,start,pivot-1)
        quick_sort(array,pivot+1,end)
    return array
    
def partition(array,start,end):
    pivot =array[start]
    left = start+1
    right =end
    done =False
    while not done:
          while left <= right and array[left]<=pivot:
                left =left+1
          while right >= left and array[right]>=pivot:
                right= right -1
          # move items less than pivote to right vice versa
          if right < left:
              done =True
          else:
             # swap places
             temp =array[left]
             array[left] =array[right]
             array[right] =temp
    #swapping pivote 
    temp =array[start]
    array[start] =array[right]
    array[right] =temp
    return right
          







