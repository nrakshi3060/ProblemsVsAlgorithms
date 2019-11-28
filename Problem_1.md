# Problem 1
## Design
Lets say floor square root of a number *x* is *s*. We can safely say that s lies between  0 and the number **0 <= s <= x**. We can use binary search to find s. 
We can find mid = (start + end)//2. If mid*mid is equal to number we return the number, if the value of mid*mid is less than number than we search the right half else the left half.
## Time Complexity
Time complexity : **O(log(n))**
Since we are using binary search for finding the answer time complexity is O(log(n))