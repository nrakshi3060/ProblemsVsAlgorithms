# Problem 2
## Design 1
Rotated sorted array means that some element in the array arr[i] > arr[i+1] that element can be considered as pivot. for example in array nums = [4,5,6,7,0,1,2], element 7 can be considered as pivot.
In this solution, I am finding the pivot first using binary search method and now the array is divided into two halves.
Since it is rotated array both halves will be sorted, If the target is greater than or equal to first element number can be searched first half or otherwise in the second half.
We can use binary search method to find the target in either halves.
## Time Complexity
Since finding the pivot involves binary search method and searching the target in sub arrays also involves binary search method the time complexity can be 2O(log(n)) but for higher values 2 can be neglected.
**Time complexity is O(log(n))** 
## Design 2
Since the given array is rotated sorted array, when array is divided into two sub arrays one of the array will be still sorted. We can check if the target lies between value at start index and value at mid index. if it exits we recursively search the sub array find the target. 
Otherwise we can search in the sub array by dividing it into halves and again we would have sorted and unsorted array.
## Time Complexity
Since we are searching the target using binary search method in sorted array the time complexity will be O(log(n))
**Time complexity is O(log(n))** 