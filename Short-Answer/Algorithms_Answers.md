#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

```python
a)  a = 0 # O(1)
    while (a < n * n * n): # O(n ^ 3)
      a = a + n * n # O(1)
```

This snippet will have a runtime of O(n) -> Linear time. It contains a loop and will run depending on the size on n.

```python
b)  sum = 0 # O(1)
    for i in range(n): # O(n)
      j = 1 # O(1 * n)
      while j < n: # O(n * n) -> O(n ^ 2)
        j *= 2 # O(1)
        sum += 1 # O(1)
```

This snippet will have a runtime of O(n ^ 2). It is the most dominating of all and wil run depending on the size of n

```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0 # O(1)
      return 2 + bunnyEars(bunnies-1) # O(n)
```

This snippet wll have a runtime of O(n) because it will run recursively depending on the size of n until bunnies = 0

## Exercise II

```python
  # Sample is an n-story building which is sorted from 1,2,3,...., nth floor

  # Egg gets broken if thrown off >= f
  # Doesn't get broken if thrown off <= f

  # strategy to determine the value of f such that the number of dropped + broken eggs is minimized => Binary Search

  # Get the Lowest floor
  # Get the Highest floor
  # While the Lowest floor is less than and not equal to the highest floor
    # Get middle of building
    # If egg breaks at middle
      # Set highest floor to middle and try again until it doesn't break
    # else if egg doesn't break at middle
      # set lowest to middle
    # else return middle as f

  # Time Complexity O(log n)

```
