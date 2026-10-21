# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# DBTITLE 1,Question 1: Happy Customers
# MAGIC %md
# MAGIC # Question 1: Happy Customers
# MAGIC
# MAGIC ## Problem Statement
# MAGIC
# MAGIC A restaurant collects customer satisfaction scores as an array of integers. A customer is considered **happy** if their satisfaction score is **strictly greater than the average** of all customer scores.
# MAGIC
# MAGIC Given an array of integers `scores`, return the **count of happy customers**.
# MAGIC
# MAGIC ## Examples
# MAGIC
# MAGIC **Example 1:**
# MAGIC ```
# MAGIC Input: scores = [3, 6, 1, 8, 2]
# MAGIC Output: 2
# MAGIC Explanation: The average is (3+6+1+8+2)/5 = 4.0. Only scores 6 and 8 are greater than 4.0, so 2 customers are happy.
# MAGIC ```
# MAGIC
# MAGIC **Example 2:**
# MAGIC ```
# MAGIC Input: scores = [5, 5, 5, 5]
# MAGIC Output: 0
# MAGIC Explanation: The average is 5.0. No score is strictly greater than 5.0.
# MAGIC ```
# MAGIC
# MAGIC **Example 3:**
# MAGIC ```
# MAGIC Input: scores = [10]
# MAGIC Output: 0
# MAGIC Explanation: The average is 10.0. The single score is not strictly greater than itself.
# MAGIC ```
# MAGIC
# MAGIC ## Constraints
# MAGIC
# MAGIC * `1 <= len(scores) <= 100`
# MAGIC * `1 <= scores[i] <= 100`
# MAGIC
# MAGIC ## Your Task
# MAGIC
# MAGIC Write a function `count_happy_customers(scores)` that returns the number of happy customers.

# COMMAND ----------

def count_happy_customers(scores):
    if len(scores) == 1 or len(scores) == 0:
        return 0
    else:
        count = 0
        avg = sum(scores)//len(scores)
        print(avg)
        for i in scores:
            if i > avg:
                count +=1
        return count
 # --- Test Cases ---
assert count_happy_customers([3, 6, 1, 8, 2]) == 2, "Test 1 Failed"
print(count_happy_customers([3, 6, 1, 8, 2]), 'Case 1')
assert count_happy_customers([5, 5, 5, 5]) == 0, "Test 2 Failed"
print(count_happy_customers([5, 5, 5, 5]), 'Case 2')
assert count_happy_customers([10]) == 0, "Test 3 Failed"
print(count_happy_customers([10]), 'Case 3')
assert count_happy_customers([1, 2, 3, 4, 5]) == 2, "Test 4 Failed"
print(count_happy_customers([1, 2, 3, 4, 5]), 'Case 4')
assert count_happy_customers([100, 1]) == 1, "Test 5 Failed"   
print(count_happy_customers([100, 1]), 'Case 5')
print('Passed')

# COMMAND ----------

# DBTITLE 1,Solution
def count_happy_customers(scores):
    """
    Returns the number of customers whose score is strictly greater
    than the average of all scores.

    Args:
        scores (List[int]): List of customer satisfaction scores.

    Returns:
        int: Count of happy customers.
    """
    #Your solution here
    sum_rating = 0
    for i in scores:
        sum_rating = sum_rating + i
    total_customer = len(scores)
    average_rating = sum_rating / total_customer

    count = 0
    for i in scores:
        if i > average_rating:
            count += 1
    return count



# --- Test Cases ---
assert count_happy_customers([3, 6, 1, 8, 2]) == 2, "Test 1 Failed"
assert count_happy_customers([5, 5, 5, 5]) == 0, "Test 2 Failed"
assert count_happy_customers([10]) == 0, "Test 3 Failed"
assert count_happy_customers([1, 2, 3, 4, 5]) == 2, "Test 4 Failed"
assert count_happy_customers([100, 1]) == 1, "Test 5 Failed"

print("All test cases passed!")

# COMMAND ----------

# DBTITLE 1,Question 2: Parking Lot Availability
# MAGIC %md
# MAGIC # Question 2: Parking Lot Availability
# MAGIC
# MAGIC ## Problem Statement
# MAGIC
# MAGIC A parking lot has `n` parking spots arranged in a single row, numbered from `0` to `n-1`. Each spot is either **occupied** (`1`) or **empty** (`0)`, represented as a list called `spots`.
# MAGIC
# MAGIC A driver wants to park in the spot that is **closest to the entrance** (located at position `0`, i.e., the beginning of the row). Find the index of the **first empty spot** in the list.
# MAGIC
# MAGIC If no spot is available, return `-1`.
# MAGIC
# MAGIC ## Examples
# MAGIC
# MAGIC **Example 1:**
# MAGIC ```
# MAGIC Input: spots = [1, 1, 0, 1, 0]
# MAGIC Output: 2
# MAGIC Explanation: Spot 0 is occupied, spot 1 is occupied, spot 2 is empty. The first empty spot is at index 2.
# MAGIC ```
# MAGIC
# MAGIC **Example 2:**
# MAGIC ```
# MAGIC Input: spots = [0, 1, 1, 1]
# MAGIC Output: 0
# MAGIC Explanation: Spot 0 is already empty, so the driver parks right at the entrance.
# MAGIC ```
# MAGIC
# MAGIC **Example 3:**
# MAGIC ```
# MAGIC Input: spots = [1, 1, 1, 1]
# MAGIC Output: -1
# MAGIC Explanation: All spots are occupied. Return -1.
# MAGIC ```
# MAGIC
# MAGIC ## Constraints
# MAGIC
# MAGIC * `1 <= len(spots) <= 1000`
# MAGIC * `spots[i]` is either `0` or `1`
# MAGIC
# MAGIC ## Your Task
# MAGIC
# MAGIC Write a function `find_first_empty_spot(spots)` that returns the index of the first empty parking spot, or `-1` if none exist.

# COMMAND ----------

# DBTITLE 1,Your Solution
def find_first_empty_spot(spots):
    """
    Returns the index of the first empty parking spot (value 0),
    or -1 if all spots are occupied.

    Args:
        spots (List[int]): List where 0 = empty, 1 = occupied.

    Returns:
        int: Index of first empty spot, or -1.
    """
    # TODO: Write your solution here
    output = -1
    for i in range(len(spots)): 
        if spots[i] == 0:
            output = i
            break
    return output

# -- Test Cases --
# Uncomment the asserts after implementing your solution
assert find_first_empty_spot([1, 1, 0, 1, 0]) == 2, "Test 1 Failed"
assert find_first_empty_spot([0, 1, 1, 1]) == 0, "Test 2 Failed"
assert find_first_empty_spot([1, 1, 1, 1]) == -1, "Test 3 Failed"
assert find_first_empty_spot([0]) == 0, "Test 4 Failed"
assert find_first_empty_spot([1, 0, 0, 1]) == 1, "Test 5 Failed"

print("All test cases passed")

# COMMAND ----------



# COMMAND ----------

# DBTITLE 1,My Solution: Q2 - Parking Lot
# --- My Solution: Question 2 (Parking Lot Availability) ---

def find_first_empty_spot(spots):
    for i, spot in enumerate(spots):
        if spot == 0:
            return i
    return -1


# Test
assert find_first_empty_spot([1, 1, 0, 1, 0]) == 2
assert find_first_empty_spot([0, 1, 1, 1]) == 0
assert find_first_empty_spot([1, 1, 1, 1]) == -1
assert find_first_empty_spot([0]) == 0
assert find_first_empty_spot([1, 0, 0, 1]) == 1
print("Question 2 — All test cases passed!")

# COMMAND ----------

# DBTITLE 1,My Solution: Q1 - Happy Customers
# --- My Solution: Question 1 (Happy Customers) ---

def count_happy_customers(scores):
    avg = sum(scores) / len(scores)
    return sum(1 for s in scores if s > avg)


# Test
assert count_happy_customers([3, 6, 1, 8, 2]) == 2
assert count_happy_customers([5, 5, 5, 5]) == 0
assert count_happy_customers([10]) == 0
assert count_happy_customers([1, 2, 3, 4, 5]) == 2
assert count_happy_customers([100, 1]) == 1
print("Question 1 — All test cases passed!")