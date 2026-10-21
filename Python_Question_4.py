# Databricks notebook source


# COMMAND ----------

# DBTITLE 1,Question: City Skyline Construction
# MAGIC %md
# MAGIC # Question: City Skyline Construction
# MAGIC
# MAGIC ## Problem Statement
# MAGIC
# MAGIC You are a city planner managing construction along a street. There are `n` plots in a row, numbered `0` to `n-1`. You are given:
# MAGIC
# MAGIC * `heights` — a list where `heights[i]` is the **current height** of the building at plot `i`
# MAGIC * `max_height` — the maximum allowed building height (all buildings must be ≤ `max_height`)
# MAGIC
# MAGIC The city wants to **increase building heights** to maximize the total skyline value, but with these constraints:
# MAGIC
# MAGIC 1. No building may exceed `max_height`
# MAGIC 2. A building's height can only be increased, never decreased
# MAGIC 3. The **skyline must remain non-decreasing** from left to right — i.e., after modifications, `heights[i] <= heights[i+1]` for all valid `i`
# MAGIC
# MAGIC After optimizing the heights, the **skyline value** is defined as the sum of all building heights.
# MAGIC
# MAGIC Return the **maximum possible skyline value**. If it's impossible to satisfy the non-decreasing constraint (e.g., a building already exceeds `max_height`), return `-1`.
# MAGIC
# MAGIC ## Examples
# MAGIC
# MAGIC **Example 1:**
# MAGIC ```
# MAGIC Input: heights = [1, 3, 2, 4], max_height = 5
# MAGIC
# MAGIC Step 1: Check feasibility — all buildings ≤ 5. OK.
# MAGIC Step 2: Work right to left to maximize:
# MAGIC   - Building 3: keep 4 (already max possible given constraints)
# MAGIC   - Building 2: must be ≤ building 3 (4) and ≤ 5 → set to 4
# MAGIC   - Building 1: must be ≤ building 2 (4) → set to 4
# MAGIC   - Building 0: must be ≤ building 1 (4) → set to 4
# MAGIC
# MAGIC Result: [4, 4, 4, 4]
# MAGIC Skyline value = 4 + 4 + 4 + 4 = 16
# MAGIC Output: 16
# MAGIC ```
# MAGIC
# MAGIC **Example 2:**
# MAGIC ```
# MAGIC Input: heights = [2, 2, 2], max_height = 2
# MAGIC
# MAGIC All buildings already at max_height and non-decreasing.
# MAGIC Skyline value = 2 + 2 + 2 = 6
# MAGIC Output: 6
# MAGIC ```
# MAGIC
# MAGIC **Example 3:**
# MAGIC ```
# MAGIC Input: heights = [1, 5, 3], max_height = 4
# MAGIC
# MAGIC Building 1 has height 5 > max_height 4. Impossible.
# MAGIC Output: -1
# MAGIC ```
# MAGIC
# MAGIC **Example 4:**
# MAGIC ```
# MAGIC Input: heights = [1, 1, 1, 1], max_height = 10
# MAGIC
# MAGIC Work right to left:
# MAGIC   - Building 3: set to 10
# MAGIC   - Building 2: set to 10
# MAGIC   - Building 1: set to 10
# MAGIC   - Building 0: set to 10
# MAGIC
# MAGIC Result: [10, 10, 10, 10]
# MAGIC Skyline value = 40
# MAGIC Output: 40
# MAGIC ```
# MAGIC
# MAGIC ## Constraints
# MAGIC
# MAGIC * `1 <= len(heights) <= 10^5`
# MAGIC * `1 <= heights[i] <= 10^9`
# MAGIC * `1 <= max_height <= 10^9`
# MAGIC
# MAGIC ## Your Task
# MAGIC
# MAGIC Write a function `max_skyline_value(heights, max_height)` that returns the maximum possible skyline value, or `-1` if impossible.

# COMMAND ----------

# DBTITLE 1,Your Solution
def max_skyline_value(heights, max_height):
    """
    Returns the maximum possible skyline value after increasing building heights
    such that the skyline is non-decreasing and no building exceeds max_height.
    Returns -1 if impossible.

    Args:
        heights (List[int]): Current building heights.
        max_height (int): Maximum allowed building height.

    Returns:
        int: Maximum total skyline value, or -1.
    """
    # TODO: Write your solution here
    pass


# --- Test Cases ---
# Uncomment after implementing your solution
# assert max_skyline_value([1, 3, 2, 4], 5) == 16, "Test 1 Failed"
# assert max_skyline_value([2, 2, 2], 2) == 6, "Test 2 Failed"
# assert max_skyline_value([1, 5, 3], 4) == -1, "Test 3 Failed"
# assert max_skyline_value([1, 1, 1, 1], 10) == 40, "Test 4 Failed"
# assert max_skyline_value([5], 10) == 10, "Test 5 Failed"
# assert max_skyline_value([5], 3) == -1, "Test 6 Failed"
# assert max_skyline_value([3, 1, 4, 1, 5], 5) == 23, "Test 7 Failed"
# assert max_skyline_value([1, 2, 3, 4, 5], 100) == 500, "Test 8 Failed"
# assert max_skyline_value([10, 20, 30, 25, 40], 50) == 230, "Test 9 Failed"
# assert max_skyline_value([1, 100], 50) == -1, "Test 10 Failed"

print("Implement the function and uncomment the test cases to check your solution!")