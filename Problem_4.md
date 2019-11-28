# Problem4
## Design
Since in the given array there are 0s, 1s and 2s. We can start iterating the array from 0th index we can track the index of 0s and index of 2s. We know that for sure that index of 0s would start from 0th index and array would for sure end with 2s so we track the next_index of 2 can be set as len(arr) -1 th index.
Now we iterate through array. When we encounter 0 we start filling the array from beginning and 2s from the end, Automatically 1s will be placed in between 0s and 2s.
## Time Complexity
Since we have to iterate the whole array every time, the time complexity will be O(n)
**Time complexity is O(n)** 