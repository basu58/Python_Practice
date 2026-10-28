# Databricks notebook source


# COMMAND ----------

# DBTITLE 1,Question: Transaction Reconciliation
# MAGIC %md
# MAGIC # Question: Transaction Reconciliation
# MAGIC
# MAGIC ## Problem Statement
# MAGIC
# MAGIC A bank processes a list of transactions where each transaction has an `amount`. Given an array of transaction `amounts` and a `target` sum, find **all unique pairs of indices** `(i, j)` where `i < j` and `amounts[i] + amounts[j] == target`.
# MAGIC
# MAGIC Return the pairs as a list of tuples `[(i, j), ...]` sorted in **ascending order** — first by `i`, then by `j`.
# MAGIC
# MAGIC **Important:**
# MAGIC * You may not pair an element with itself (i.e., `i == j` is not allowed)
# MAGIC * Each pair `(i, j)` must be unique (no duplicate pairs in the output)
# MAGIC * If no pairs exist, return an empty list `[]`
# MAGIC * The array may contain **duplicate values** — each duplicate is a separate element at a different index. Do NOT remove duplicates.
# MAGIC
# MAGIC ## Examples
# MAGIC
# MAGIC **Example 1:**
# MAGIC ```
# MAGIC Input: amounts = [2, 7, 11, 15], target = 9
# MAGIC Output: [(0, 1)]
# MAGIC Explanation: 2 + 7 = 9, indices (0, 1) is the only valid pair.
# MAGIC ```
# MAGIC
# MAGIC **Example 2:**
# MAGIC ```
# MAGIC Input: amounts = [3, 3, 3, 3], target = 6
# MAGIC Output: [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
# MAGIC Explanation: Every pair of 3s sums to 6. All unique index pairs are included.
# MAGIC ```
# MAGIC
# MAGIC **Example 3:**
# MAGIC ```
# MAGIC Input: amounts = [1, 5, 3, 7, 2], target = 8
# MAGIC
# MAGIC Pairs:
# MAGIC - 1 + 7 = 8 → (0, 3)
# MAGIC - 5 + 3 = 8 → (1, 2)
# MAGIC
# MAGIC Output: [(0, 3), (1, 2)]
# MAGIC ```
# MAGIC
# MAGIC **Example 4:**
# MAGIC ```
# MAGIC Input: amounts = [1, 2, 3], target = 100
# MAGIC Output: []
# MAGIC Explanation: No pair sums to 100.
# MAGIC ```
# MAGIC
# MAGIC ## Constraints
# MAGIC
# MAGIC * `2 <= len(amounts) <= 10^4`
# MAGIC * `-10^9 <= amounts[i] <= 10^9`
# MAGIC * `-10^9 <= target <= 10^9`
# MAGIC * Your solution should be more efficient than O(n²) brute force for full credit
# MAGIC
# MAGIC ## Your Task
# MAGIC
# MAGIC Write a function `find_transaction_pairs(amounts, target)` that returns all unique index pairs whose values sum to the target.

# COMMAND ----------

# DBTITLE 1,Your Solution
def find_transaction_pairs(amounts, target):
    """
    Returns all unique pairs of indices (i, j) where i < j
    and amounts[i] + amounts[j] == target.

    Pairs are sorted first by i, then by j.

    Args:
        amounts (List[int]): Transaction amounts.
        target (int): Target sum.

    Returns:
        List[Tuple[int, int]]: All valid index pairs.
    """
    # TODO: Write your solution here
    li = []
    #amounts = list(dict.fromkeys(amounts))
    for i in range(0, len(amounts)-1):
        for j in range(i+1, len(amounts)):
            if i < j and (amounts[i] + amounts[j] == target):
                li.append((i, j))
    return sorted(li)

# --- Test Cases ---
# Uncomment after implementing your solution
result = find_transaction_pairs([2, 7, 11, 15], 9)
assert result == [(0, 1)], f"Test 1 Failed: {result}"

result = find_transaction_pairs([3, 3, 3, 3], 6)
assert result == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], f"Test 2 Failed: {result}"

result = find_transaction_pairs([1, 5, 3, 7, 2], 8)
assert result == [(0, 3), (1, 2)], f"Test 3 Failed: {result}"

result = find_transaction_pairs([1, 2, 3], 100)
assert result == [], f"Test 4 Failed: {result}"

result = find_transaction_pairs([0, 0, 0], 0)
assert result == [(0, 1), (0, 2), (1, 2)], f"Test 5 Failed: {result}"

result = find_transaction_pairs([-1, 1, 0, 2], 1)
assert result == [(0, 3), (1, 2)], f"Test 6 Failed: {result}"

result = find_transaction_pairs([5, 5, 5, 5, 5], 10)
assert result == [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)], f"Test 7 Failed: {result}"

result = find_transaction_pairs([1], 1)
assert result == [], f"Test 8 Failed: {result}"

result = find_transaction_pairs([1, -1, 2, -2, 3, -3], 0)
assert result == [(0, 1), (2, 3), (4, 5)], f"Test 9 Failed: {result}"

result = find_transaction_pairs([4, 4, 4, 4], 8)
assert result == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], f"Test 10 Failed: {result}"

print("Implement the function and uncomment the test cases to check your solution!")

# COMMAND ----------

# DBTITLE 1,My Solution: Hash Map Approach
# --- My Solution: Hash Map Approach (O(n)) ---

def find_transaction_pairs(amounts, target):
    seen = {}  # value -> list of indices where that value was seen
    result = []

    for i, val in enumerate(amounts):
        complement = target - val
        if complement in seen:
            for j in seen[complement]:
                result.append((j, i))  # j < i since j was seen earlier
        seen.setdefault(val, []).append(i)

    return sorted(result)


# --- Test Cases ---
result = find_transaction_pairs([2, 7, 11, 15], 9)
assert result == [(0, 1)], f"Test 1 Failed: {result}"

result = find_transaction_pairs([3, 3, 3, 3], 6)
assert result == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], f"Test 2 Failed: {result}"

result = find_transaction_pairs([1, 5, 3, 7, 2], 8)
assert result == [(0, 3), (1, 2)], f"Test 3 Failed: {result}"

result = find_transaction_pairs([1, 2, 3], 100)
assert result == [], f"Test 4 Failed: {result}"

result = find_transaction_pairs([0, 0, 0], 0)
assert result == [(0, 1), (0, 2), (1, 2)], f"Test 5 Failed: {result}"

result = find_transaction_pairs([-1, 1, 0, 2], 1)
assert result == [(0, 3), (1, 2)], f"Test 6 Failed: {result}"

result = find_transaction_pairs([5, 5, 5, 5, 5], 10)
assert result == [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)], f"Test 7 Failed: {result}"

result = find_transaction_pairs([1], 1)
assert result == [], f"Test 8 Failed: {result}"

result = find_transaction_pairs([1, -1, 2, -2, 3, -3], 0)
assert result == [(0, 1), (2, 3), (4, 5)], f"Test 9 Failed: {result}"

result = find_transaction_pairs([4, 4, 4, 4], 8)
assert result == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], f"Test 10 Failed: {result}"

print("All 10 test cases passed!")