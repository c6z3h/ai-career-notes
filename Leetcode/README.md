## Summary
* Global Ranking: [Top 11.99%](https://leetcode.com/c6z3h/)
* Current Focus: Dynamic Programming

## Focus Area
- [ ] [Detailed Explanation on Dynamic Programming, Leetcode](https://leetcode.com/explore/learn/card/dynamic-programming/)
- [ ] [Dynamic Programming](https://leetcode.com/study-plan/dynamic-programming/)
  
  
  
  
  
  
## My Coding Tests
### 1. AI Singapore: AI Apprentice Test
### 2. Grab: (1) DevOps, (2) DSAI Test
### 3. GovTech: Technological Associate Programme Test
### 4. Shopee: ML Engineer (Fresh Grad) Test, 14 July 2021
- 2 questions in 60 min, proctored with camera, microphone, screen_share (Glider.AI).
- Similar to Leetcode Easy / medium.
- (1) Strings: Substring matching (2) Sort and search: k-th largest integer in array.
### 5. ByteDance: SWE - HBase, tbc

## Lessons from LeetCode
### 0. Algorithms and Data Structures (ADS)
Continuing [Part 3 of ADS lectures by MIT[08:43]](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/lecture-12-searching-and-sorting/). Irrelevant to ADS, [problem sets 4 and 5](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/) may be good practice if there is time.

Time Complexity Desirability: O(1) > O(logn) {reduce problem in half each time, bisection seach} > O(n) > O(nlogn) [{Timsort}](https://en.wikipedia.org/wiki/Timsort) > O(n^c) {nested loops} > O(c^n)

### 1. Brute Force Works, Just Not As Well On Big Problems.
Brute force methods are usually the easiest, first thing to think of. For an example, see two-sum.py. Beyond the initial solution, one should think of answers that help reduce computational time and/or space. This is related to the idea of **space and time complexity.** In the example of two-sum.py, we see that sacrificing some space by saving values into a **dictionary lookup** instead of double for-loops help reduce time complexity from O(n^2) to O(n), 4000ms to 40ms!

### 2. Binary Search Algorithm
By implementing the low = 0, high = len(array), n = (high - low)//2 and iterating over that, the search space effectively can be halved. This greatly reduces computational time.

### 3. Creativity
Check out the creative solutions on LeetCode discussion pages!
