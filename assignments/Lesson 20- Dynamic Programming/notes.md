Dynamic Programming Quiz

1. Thanks to dynamic programming,
    Fibonacci is solvable in linear time by storing partial solutions 
    Fibonacci is solvable in logarithmic time by recursively dividing the search space in half. 
    Fibonacci is solvable in quadratic time by backtracking through the search space of possibilities. 
    Fibonacci is solvable in constant time via a special math formula. 

2. Define the terms of memoization, tabulation, and dynamic programming.
    Memoization
        Recursively storing calculated solutions so that they can used in future function calls
    Tabulation
        Iteratively storing calculated solutions to use in the next step
    Dynamic Programming
        An algorithmic technique where redundant operations are avoided by recognizing repeated subproblems.
    Divide and Conquer
        An algorithmic technique where a problem is composed of subproblems that do not have overlapping solutions.
    Greedy
        Any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage with the intent of finding a global optimum.

    An algorithm that takes `O(N*M)` time (quadratic)
    Calculating the difference between two strings
    Exhaustively searching through all possible options

-----------------------------------------

3. Do an Edit Distance table
    
4. Identify whether a particular algorithm ends up being solvable with Dynamic Programming.
      Djikstra's Algorithm can solve single-source shortest path 
      Floyd's Algorithm can solve all-source shortest path 
      First Fit Heuristic can solve the 0-1 Knapsack algorithm 
      All algorithms can be solved more efficiently using Dynamic Programming 
      Depth-first Search can solve the Connected Graph problem 
      Wagner–Fischer algorithm can solve Edit Distance 
      Merge sort can solve the Sorting Problem
      Binary Search can solve the Search Problem


5. Which of the following would prevent a problem from being solved with dynamic programming?
    True: The problem cannot be divided into smaller problems.
    True: Subproblems do not appear more than once.
    False: The input of the problem cannot be stored as a 2D array.
    False: The problem requires exponential time.
    

6. What is the best upper bound for each of the following?
    Naive recursive fibonacci: exponential
    Memoized fibonacci: linear
    Tabulated fibonacci: linear

    
7. When you memoize the fibonacci algorithm in Python, what is an upper bound for the **space** that it requires?
    Constant, because we can solve the problem "in-place"
    Linear, because the size of the call stack and a memoization dictionary,
    Linear, because we have repeated subproblems
    Quadratic, because we have both a call stack and a memoization dictionary
    Quadratic, because we have repeated subproblems
    Exponential, because we have repeated subproblems


8. True or false:
    True: Any function can be memoized by storing its arguments and return values, even if it does not affect its time complexity.
    False: Any function can be tabulated by storing its array elements in a table.
    True: Any dynamic programming algorithm can be expressed as a recurrence relation.
    False: Any program that is recursive can be turned into a Dynamic Programming algorithm.
    

9. The Subset Sum problem can be solved more efficiently with tabulation than without. Which statements are true?
    True: The top row represents the solution for a given desired sum.
    False: The top row represents the largest value seen in the subset.
    True: In order to determine if the sum of a set `X` is equal to `S`, it helps to know what values smaller than `S` can be formed from the subsets of `X`.
    True: The vertical axis of the table represents the subset of values where the value at left is added to the previous row.
    True: A cell of the table contains True if there exists a subset of the values for that row that equal the sum represented by the column.
    False: The cells of the table contains an integer representing how many solutions there are in a neighboring cell.
    
    
10. What is the best definition for the term "pseudo-polynomial time"?
    False: A time complexity bounded by a polynomial, such as `n^k`, where `n` is the length of input and `k` is a constant.
    True: A time complexity bounded by a polynomial, such as `W^k`, where `W` is the numeric size of the input and `k` is a constant.
    False: A time complexity that are not actually bounded by a polynomial, but are still less than exponential time.
    False: A time complexity bounded by a logarithmic expression, such as `log(n)`, where `n` is the length of the input.
    False: A synonym for "worst case lower bound".
    False: A synonym for "best case upper bound".
    

11. (Extra Credit) Where does the name come from?
    The approach is actually irrelevantly named compared to what it does. 
    The approach uses dynamic memory, as opposed to static memory. 
    The approach requires a dynamic array. 
    The technique involves a programmer dynamically considering many possible aspects. 
    The technique can only be used in a dynamic programming language, like Python. 
    
