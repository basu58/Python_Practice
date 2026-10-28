# Databricks notebook source
# DBTITLE 1,Python Question 8 — Find a Subset That Sums to Target
# MAGIC %md
# MAGIC # Python Question 8 — Find a Subset That Sums to Target
# MAGIC
# MAGIC Difficulty: Medium · Topic: Recursion / Dynamic Programming
# MAGIC
# MAGIC Read the question in the next cell, implement the function stub, then uncomment the asserts and run to verify!

# COMMAND ----------

# DBTITLE 1,Q: Subset Sum — Best Matching Subset
# MAGIC %md
# MAGIC ## Q: Subset Sum — Find the Best Matching Subset
# MAGIC
# MAGIC **Difficulty:** Medium | **Topic:** Recursion / Dynamic Programming
# MAGIC
# MAGIC Given a list of **positive integers** `nums` and a **positive integer** `target`, return a subset (a list) of `nums` whose elements sum **exactly** to `target`.
# MAGIC
# MAGIC **Conditions:**
# MAGIC 1. Each element in `nums` may be used **at most once** (a true subset — you cannot reuse the same position twice, but duplicate values in the list count as separate elements).
# MAGIC 2. If multiple subsets sum to `target`, return the one with the **fewest elements**.
# MAGIC 3. If there is still a tie, return the **lexicographically smallest** subset (compare the sorted subsets element by element).
# MAGIC 4. Return the subset **sorted in ascending order**.
# MAGIC 5. If no subset sums to `target`, return `None`.
# MAGIC
# MAGIC **Examples:**
# MAGIC ```
# MAGIC Input: nums = [1, 2, 3, 4, 5], target = 9
# MAGIC Output: [4, 5]        # [2, 3, 4] also sums to 9, but has more elements
# MAGIC
# MAGIC Input: nums = [3, 34, 4, 12, 5, 2], target = 9
# MAGIC Output: [4, 5]        # fewest elements; [2, 3, 4] also works but is longer
# MAGIC
# MAGIC Input: nums = [2, 4, 6, 8], target = 5
# MAGIC Output: None          # even numbers can never sum to an odd target
# MAGIC
# MAGIC Input: nums = [1, 1, 2], target = 2
# MAGIC Output: [2]           # [1, 1] also sums to 2, but [2] has fewer elements
# MAGIC
# MAGIC Input: nums = [5], target = 5
# MAGIC Output: [5]
# MAGIC ```
# MAGIC
# MAGIC **Follow-up:** Can you solve it without generating every possible subset explicitly (i.e., better than O(2^n) brute force)? Think about sorting `nums` in descending order and pruning branches whose remaining sum can no longer reach `target`.

# COMMAND ----------

# DBTITLE 1,Q Solution Stub
def find_subset(nums, target):
    """Return the smallest subset of nums (sorted ascending) that sums exactly to target.

    Rules:
      - Each element may be used at most once (duplicates in nums are distinct elements).
      - If multiple subsets qualify, prefer the one with the fewest elements;
        break ties by returning the lexicographically smallest sorted subset.
      - Return None if no subset sums to target.
    """
    # TODO: implement
    best = [None] * (target + 1)
    best[0] = []

    def key(subset):
        # fewest elements first, then smallest when read largest-to-smallest
        return (len(subset), subset[::-1])

    for n in nums:
        for s in range(target, n - 1, -1):
            if best[s - n] is not None:
                candidate = sorted(best[s - n] + [n])
                if best[s] is None or key(candidate) < key(best[s]):
                    best[s] = candidate

    return best[target]


# --- Test Cases ---
print(find_subset([1, 2, 3, 4, 5], 9))                 # [4, 5]
assert find_subset([1, 2, 3, 4, 5], 9) == [4, 5], "Test 1 Failed"
assert find_subset([3, 34, 4, 12, 5, 2], 9) == [4, 5], "Test 2 Failed"
assert find_subset([2, 4, 6, 8], 5) is None, "Test 3 Failed"
assert find_subset([1, 1, 2], 2) == [2], "Test 4 Failed"
assert find_subset([5], 5) == [5], "Test 5 Failed"
assert find_subset([1, 2, 3], 7) is None, "Test 6 Failed"
assert find_subset([2, 2, 3], 4) == [2, 2], "Test 7 Failed"
assert find_subset([10, 7, 5, 3, 2], 12) == [5, 7], "Test 8 Failed"
print("All tests passed!")