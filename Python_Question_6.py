# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///


# COMMAND ----------

# DBTITLE 1,Question: Meeting Room Scheduler
# MAGIC %md
# MAGIC # Question: Meeting Room Scheduler
# MAGIC
# MAGIC ## Problem Statement
# MAGIC
# MAGIC A company schedules meetings throughout the day. Each meeting is represented as an interval `(start, end)` where `start` is the meeting start time and `end` is the meeting end time.
# MAGIC
# MAGIC Due to a scheduling system glitch, some meetings **overlap** with each other. Your task is to **merge all overlapping meetings** and return a list of **non-overlapping intervals** that cover all the time ranges of the original meetings.
# MAGIC
# MAGIC Two intervals `(a, b)` and `(c, d)` **overlap** if:
# MAGIC * `c <= b` (the next meeting starts before or exactly when the current one ends)
# MAGIC
# MAGIC When merging, the new interval becomes `(min(a, c), max(b, d))`.
# MAGIC
# MAGIC ## Examples
# MAGIC
# MAGIC **Example 1:**
# MAGIC ```
# MAGIC Input: meetings = [[1, 3], [2, 6], [8, 10], [15, 18]]
# MAGIC
# MAGIC Step 1: Sort by start time → [[1, 3], [2, 6], [8, 10], [15, 18]]
# MAGIC Step 2: Merge:
# MAGIC   - [1, 3] and [2, 6] overlap (2 <= 3) → merge to [1, 6]
# MAGIC   - [1, 6] and [8, 10] don't overlap (8 > 6) → keep separate
# MAGIC   - [8, 10] and [15, 18] don't overlap (15 > 10) → keep separate
# MAGIC
# MAGIC Output: [[1, 6], [8, 10], [15, 18]]
# MAGIC ```
# MAGIC
# MAGIC **Example 2:**
# MAGIC ```
# MAGIC Input: meetings = [[1, 4], [4, 5]]
# MAGIC
# MAGIC [1, 4] and [4, 5] overlap (4 <= 4) → merge to [1, 5]
# MAGIC
# MAGIC Output: [[1, 5]]
# MAGIC ```
# MAGIC
# MAGIC **Example 3:**
# MAGIC ```
# MAGIC Input: meetings = [[1, 4], [2, 3]]
# MAGIC
# MAGIC [1, 4] and [2, 3] overlap (2 <= 4) → merge to [1, 4] (the inner interval is absorbed)
# MAGIC
# MAGIC Output: [[1, 4]]
# MAGIC ```
# MAGIC
# MAGIC **Example 4:**
# MAGIC ```
# MAGIC Input: meetings = [[5, 10], [1, 3], [2, 6]]
# MAGIC
# MAGIC Step 1: Sort by start time → [[1, 3], [2, 6], [5, 10]]
# MAGIC Step 2: Merge:
# MAGIC   - [1, 3] and [2, 6] overlap (2 <= 3) → merge to [1, 6]
# MAGIC   - [1, 6] and [5, 10] overlap (5 <= 6) → merge to [1, 10]
# MAGIC
# MAGIC Output: [[1, 10]]
# MAGIC ```
# MAGIC
# MAGIC ## Constraints
# MAGIC
# MAGIC * `1 <= len(meetings) <= 10^4`
# MAGIC * `meetings[i] = [start_i, end_i]`
# MAGIC * `0 <= start_i < end_i <= 10^6`
# MAGIC * Intervals are NOT necessarily sorted
# MAGIC
# MAGIC ## Your Task
# MAGIC
# MAGIC Write a function `merge_meetings(meetings)` that returns a list of merged non-overlapping intervals sorted by start time.

# COMMAND ----------

# DBTITLE 1,Your Solution
def merge_meetings(meetings):
    """
    Merges all overlapping meeting intervals.

    Args:
        meetings (List[List[int]]): List of [start, end) intervals.

    Returns:
        List[List[int]]: Merged non-overlapping intervals sorted by start time.
    """
    # Step 1: Sort meetings by start time
    meetings = sorted(meetings)
    # Step 2: Merge overlapping meetings one by one
    merged = []
    for start, end in meetings:
        if merged and start <= merged[-1][1]:
            # Overlaps with the last merged meeting -> extend it
            merged[-1][1] = max(merged[-1][1], end)
        else:
            # No overlap -> add as a new meeting
            merged.append([start, end])

    return merged


# --- Test Cases ---
# Uncomment after implementing your solution
result = merge_meetings([[1, 3], [2, 6], [8, 10], [15, 18]])
assert result == [[1, 6], [8, 10], [15, 18]], f"Test 1 Failed: {result}"

# result = merge_meetings([[1, 4], [4, 5]])
# assert result == [[1, 5]], f"Test 2 Failed: {result}"

# result = merge_meetings([[1, 4], [2, 3]])
# assert result == [[1, 4]], f"Test 3 Failed: {result}"

# result = merge_meetings([[5, 10], [1, 3], [2, 6]])
# assert result == [[1, 10]], f"Test 4 Failed: {result}"

# result = merge_meetings([[7, 9]])
# assert result == [[7, 9]], f"Test 5 Failed: {result}"

# result = merge_meetings([[1, 2], [3, 4], [5, 6]])
# assert result == [[1, 2], [3, 4], [5, 6]], f"Test 6 Failed: {result}"

# result = merge_meetings([[1, 5], [2, 6], [3, 7], [4, 8]])
# assert result == [[1, 8]], f"Test 7 Failed: {result}"

# result = merge_meetings([[8, 10], [1, 2], [3, 5], [4, 6]])
# assert result == [[1, 2], [3, 6], [8, 10]], f"Test 8 Failed: {result}"

# result = merge_meetings([[1, 4], [1, 3]])
# assert result == [[1, 4]], f"Test 9 Failed: {result}"

# result = merge_meetings([[1, 2], [2, 3], [3, 4]])
# assert result == [[1, 4]], f"Test 10 Failed: {result}"

print("Implement the function and uncomment the test cases to check your solution!")