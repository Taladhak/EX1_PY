def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  

    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.

    # YOUR CODE HERE
    total = 0  # Initialize a variable to hold the sum
    for num in nums:  # Iterate through each number in the list
        total += num  # Add the current number to the total sum
    return total  # Return the total sum after the loop

print("sum_nums returned", sum_nums([1, 2, 3, 4]))
