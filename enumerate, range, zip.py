# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
def find_mismatches(expected, actual):
  size = range(1, len(expected))
  li = [p for p in zip(size, expected, actual) if p[1] != p[2]]
  print(li)
expected = [100, 200, 150, 100, 250]
actual   = [100, 180, 150, 320, 200]
find_mismatches(expected, actual)

# COMMAND ----------

# DBTITLE 1,Question: Delivery Route Auditor
# MAGIC %md
# MAGIC # Question: Delivery Route Auditor
# MAGIC
# MAGIC ## Problem Statement
# MAGIC
# MAGIC A delivery company has `n` stops on a route. You are given:
# MAGIC
# MAGIC * `expected_times` — a list of expected arrival times (in minutes from start) for each stop
# MAGIC * `actual_times` — a list of actual arrival times
# MAGIC * `tolerance` — a grace period in minutes
# MAGIC
# MAGIC A stop is considered **delayed** if `actual_time > expected_time + tolerance`.
# MAGIC
# MAGIC Write a function `audit_delivery_route(expected_times, actual_times, tolerance)` that returns a list of tuples, where each tuple contains:
# MAGIC
# MAGIC ```
# MAGIC (stop_number, expected_time, actual_time, delay_minutes)
# MAGIC ```
# MAGIC
# MAGIC * `stop_number` starts from `1` (not 0)
# MAGIC * `delay_minutes` is `actual_time - expected_time` (only for delayed stops)
# MAGIC * Only include **delayed** stops in the result
# MAGIC
# MAGIC ## Requirements
# MAGIC
# MAGIC Your solution **must** use all three:
# MAGIC * `range` — to generate stop numbers
# MAGIC * `zip` — to pair expected and actual times
# MAGIC * `enumerate` — to iterate through the zipped pairs with index
# MAGIC
# MAGIC ## Examples
# MAGIC
# MAGIC **Example 1:**
# MAGIC ```
# MAGIC Input: expected_times = [10, 25, 40, 60, 75]
# MAGIC        actual_times   = [12, 22, 45, 68, 72]
# MAGIC        tolerance = 5
# MAGIC
# MAGIC Output: [(4, 60, 68, 8)]
# MAGIC
# MAGIC Explanation:
# MAGIC - Stop 1: 12 <= 10+5 = 15 → on time
# MAGIC - Stop 2: 22 <= 25+5 = 30 → on time
# MAGIC - Stop 3: 45 <= 40+5 = 45 → on time (not strictly greater)
# MAGIC - Stop 4: 68 > 60+5 = 65 → delayed by 8 min
# MAGIC - Stop 5: 72 <= 75+5 = 80 → on time
# MAGIC ```
# MAGIC
# MAGIC **Example 2:**
# MAGIC ```
# MAGIC Input: expected_times = [5, 10, 15]
# MAGIC        actual_times   = [5, 10, 15]
# MAGIC        tolerance = 0
# MAGIC
# MAGIC Output: []
# MAGIC Explanation: All stops arrived exactly on time. No delays.
# MAGIC ```
# MAGIC
# MAGIC ## Constraints
# MAGIC
# MAGIC * `1 <= len(expected_times) <= 100`
# MAGIC * `len(expected_times) == len(actual_times)`
# MAGIC * `0 <= expected_times[i], actual_times[i] <= 1000`
# MAGIC * `0 <= tolerance <= 60`
# MAGIC
# MAGIC ## Your Task
# MAGIC
# MAGIC Write a function `audit_delivery_route(expected_times, actual_times, tolerance)` using `range`, `zip`, and `enumerate`.

# COMMAND ----------

# DBTITLE 1,Your Solution

def audit_delivery_route(expected_times, actual_times, tolerance):
    """
    Returns a list of tuples for delayed stops:
    (stop_number, expected_time, actual_time, delay_minutes)

    Must use: range, zip, and enumerate.
    """
    # TODO: Write your solution here
    size = range(1, len(expected_times)+1)
    li = []
    for i in zip(size, expected_times, actual_times):
        if i[2] > i[1] + tolerance:
            li.append((i[0], i[1], i[2], i[2] - i[1]))

    return li


result = audit_delivery_route([10, 25, 40, 60, 75], [12, 22, 45, 68, 72], 5)
assert result == [(4, 60, 68, 8)], f"Test 1 Failed: {result}"

result = audit_delivery_route([5, 10, 15], [5, 10, 15], 0)
assert result == [], f"Test 2 Failed: {result}"

result = audit_delivery_route([20, 30, 40, 50], [25, 30, 50, 52], 3)
assert result == [(1, 20, 25, 5), (3, 40, 50, 10)], f"Test 3 Failed: {result}"

# Test 4: Single stop, delayed
result = audit_delivery_route([10], [20], 5)
assert result == [(1, 10, 20, 10)], f"Test 4 Failed: {result}"

# Test 5: Single stop, on time
result = audit_delivery_route([10], [12], 5)
assert result == [], f"Test 5 Failed: {result}"

# Test 6: All stops delayed
result = audit_delivery_route([10, 20, 30], [20, 30, 40], 0)
assert result == [(1, 10, 20, 10), (2, 20, 30, 10), (3, 30, 40, 10)], f"Test 6 Failed: {result}"

# Test 7: Large tolerance, all on time
result = audit_delivery_route([10, 20, 30], [15, 25, 35], 100)
assert result == [], f"Test 7 Failed: {result}"

# Test 8: Exact match, zero tolerance
result = audit_delivery_route([50, 50, 50, 50], [50, 50, 50, 50], 0)
assert result == [], f"Test 8 Failed: {result}"

# Test 9: Last stop delayed only
result = audit_delivery_route([10, 20, 30], [10, 20, 40], 5)
assert result == [(3, 30, 40, 10)], f"Test 9 Failed: {result}"

# Test 10: First stop delayed only
result = audit_delivery_route([10, 20, 30], [20, 20, 30], 5)
assert result == [(1, 10, 20, 10)], f"Test 10 Failed: {result}"

# Test 11: Two stops, both delayed
result = audit_delivery_route([10, 20], [25, 35], 5)
assert result == [(1, 10, 25, 15), (2, 20, 35, 15)], f"Test 11 Failed: {result}"

# Test 12: Large input, mixed delays
result = audit_delivery_route([5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [5, 12, 15, 25, 25, 40, 35, 48, 45, 60], 3)
assert result == [(4, 20, 25, 5), (6, 30, 40, 10), (8, 40, 48, 8), (10, 50, 60, 10)], f"Test 12 Failed: {result}"

# Test 13: Alternating delay and on-time
result = audit_delivery_route([10, 10, 10, 10], [20, 10, 20, 10], 5)
assert result == [(1, 10, 20, 10), (3, 10, 20, 10)], f"Test 13 Failed: {result}"

print('All Test-Cases Passed')

# COMMAND ----------

# DBTITLE 1,My Solution: Delivery Route Auditor
# --- My Solution: Delivery Route Auditor ---

def audit_delivery_route(expected_times, actual_times, tolerance):
    stop_numbers = range(1, len(expected_times) + 1)
    result = []
    for idx, (stop, exp_t, act_t) in enumerate(zip(stop_numbers, expected_times, actual_times)):
        if act_t > exp_t + tolerance:
            result.append((stop, exp_t, act_t, act_t - exp_t))
    return result


# Test
result = audit_delivery_route([10, 25, 40, 60, 75], [12, 22, 45, 68, 72], 5)
assert result == [(4, 60, 68, 8)], f"Test 1 Failed: {result}"

result = audit_delivery_route([5, 10, 15], [5, 10, 15], 0)
assert result == [], f"Test 2 Failed: {result}"

result = audit_delivery_route([20, 30, 40, 50], [25, 30, 50, 52], 3)
assert result == [(1, 20, 25, 5), (3, 40, 50, 10)], f"Test 3 Failed: {result}"

# Edge case: last stop IS delayed — catches the range bug
result = audit_delivery_route([10, 20, 30], [12, 22, 40], 5)
assert result == [(3, 30, 40, 10)], f"Test 4 Failed: {result}"

print("All test cases passed!")