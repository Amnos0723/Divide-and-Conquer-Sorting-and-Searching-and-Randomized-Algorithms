'''
The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer in the ith row of the file gives you the ith entry of an input array. 
Your task is to compute the total number of comparisons used to sort the given input file by QuickSort.  As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.
You should not count comparisons one-by-one.  Rather, when there is a recursive call on a subarray of length m, you should simply add m−1 to your running total of comparisons.  (This is because the pivot element is compared to each of the other m−1 elements in the subarray in this recursive call.)
WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you differing numbers of comparisons.  For this problem, you should implement the Partition subroutine exactly as it is described in the video lectures (otherwise you might get the wrong answer).
DIRECTIONS FOR PROBLEM 1:
For the first part of the programming assignment, you should always use the first element of the array as the pivot element.
DIRECTIONS FOR PROBLEM 2:
Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot element.  Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures.Recall from the lectures that, just before the main Partition subroutine, you should exchange the pivot element (i.e., the last element) with the first element.
DIRECTIONS FOR PROBLEM 3:
Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule.  [The primary motivation behind this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly sorted or reverse sorted.]  In more detail, you should choose the pivot as follows.  Consider the first, middle, and final elements of the given array.  (If the array has odd length it should be clear what the "middle" element is; for an array with even length 2k, use the kth element as the "middle" element. So for the array 4 5 6 7,  the "middle" element is the second one ---- 5 and not 6!)  Identify which of these three elements is the median (i.e., the one whose value is in between the other two), and use this as your pivot.  As discussed in the first and second parts of this programming assignment, be sure to implement Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before the main Partition subroutine).EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.SUBTLE POINT: A careful analysis would keep track of the comparisons made in identifying the median of the three candidate elements.  You should NOT do this.  That is, as in the previous two problems, you should simply add m−1 to your running total of comparisons every time you recurse on a subarray with length m.
'''
## pick the first element as the pivot
def quick_sort_first(lis):
  if len(lis)==0:
    return 0
  elif len(lis)==1:
    return 0
  elif len(lis)==2:
    return 1
  else:
    pivot=lis[0]
    i=0
    j=1
    for index in range(1,len(lis)):
      if lis[index]<pivot:
        if i==j:
          i=i+1
          j=j+1
        else:
          temp=lis[index]
          lis[index]=lis[i+1]
          lis[i+1]=temp
          i=i+1
          j=j+1
      else:
        j=j+1
    temp=lis[i]
    lis[i]=lis[0]
    lis[0]=temp
    return len(lis)-1+quick_sort_first(lis[:i])+quick_sort_first(lis[i+1:])
    


## pick the last element as the pivot
def quick_sort_last(lis):
  if len(lis)==0:
    return 0
  elif len(lis)==1:
    return 0
  elif len(lis)==2:
    return 1
  else:
    temp=lis[-1]
    lis[-1]=lis[0]
    lis[0]=temp
    
    pivot=lis[0]
    temp
    i=0
    j=1
    for index in range(1,len(lis)):
      if lis[index]<pivot:
        if i==j:
          i=i+1
          j=j+1
        else:
          temp=lis[index]
          lis[index]=lis[i+1]
          lis[i+1]=temp
          i=i+1
          j=j+1
      else:
        j=j+1
        
    temp=lis[i]
    lis[i]=lis[0]
    lis[0]=temp
    
    return len(lis)-1+quick_sort_last(lis[:i])+quick_sort_last(lis[i+1:])

import math
import statistics

## pick the median element as the pivot
def quick_sort_median(lis):
  if len(lis)==0:
    return 0
  elif len(lis)==1:
    return 0
  elif len(lis)==2:
    return 1
  else:
    median=math.floor((len(lis)-1)/2)
    comparelis=[lis[0],lis[median],lis[-1]]
    if lis[0]==statistics.median(comparelis):
      index=0
    elif lis[-1]==statistics.median(comparelis):
      index=-1
    else:
      index=median
    #print("choose ",lis[index]," from ",lis[0],lis[median],lis[-1])  
    
    temp=lis[index]
    lis[index]=lis[0]
    lis[0]=temp
    
    pivot=lis[0]
    temp
    i=0
    j=1
    for index in range(1,len(lis)):
      if lis[index]<pivot:
        if i==j:
          i=i+1
          j=j+1
        else:
          temp=lis[index]
          lis[index]=lis[i+1]
          lis[i+1]=temp
          i=i+1
          j=j+1
      else:
        j=j+1
        
    temp=lis[i]
    lis[i]=lis[0]
    lis[0]=temp
    
    return len(lis)-1+quick_sort_median(lis[:i])+quick_sort_median(lis[i+1:])

lis=[1,23,65,4,654,8,4]
print(len(lis))
#print(quick_sort_first(lis))
#print(quick_sort_last(lis))
print(quick_sort_median(lis))
