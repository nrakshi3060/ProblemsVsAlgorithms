# Problem 6
## Design 
This problem is solved by using Divide and conquer technique. The given array is divided into number of sub arrays, such a way that the smallest sub array is either of length one or length 2. In case of length one max and min of the sub array is the same element. in case of sub arrays with length 2 we need just one comparision to determine the max and min. Later we then compare max's and  min's of these fragments of sub arrays to determine min and max of the given array. 
##Time Complexity: O(n)
Total number of comparisons: let number of comparisons be T(n). T(n) can be written as follows:             
  T(n) = T(floor(n/2)) + T(ceil(n/2)) + 2  
  T(2) = 1
  T(1) = 0
If n is a power of 2, then we can write T(n) as:
   T(n) = 2T(n/2) + 2 
After solving above recursion, we get
  T(n)  = 3n/2 -2 
Thus, the approach does 3n/2 -2 comparisons if n is a power of 2. And it does more than 3n/2 -2 comparisons if n is not a power of 2. which can approximated to O(n)