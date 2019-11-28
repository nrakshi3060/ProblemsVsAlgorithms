# Problem3
## Design
A maximum number can be formed from given array of digits when largest digit appears at most significant position and next largest digit appears at next most significant position and so on.. Inorder to get largest digit and next largest and so on.. 
I have used quick sort to sort the array and then I am looping through sorted digits to create two numbers.
## Time Complexity
Since quick sort takes O(nlog(n)) time complexity to sort the numbers and time complexity for numbers is O(n) the total time complexity will be O(nlog(n)) + O(n). But for large inputs O(n) can be negligible.
**Time complexity is O(nlogn)**