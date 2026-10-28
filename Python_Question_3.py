# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///


# COMMAND ----------

# DBTITLE 1,Question: Bookshelf Organizer
# MAGIC %md
# MAGIC # Question: Bookshelf Organizer
# MAGIC
# MAGIC ## Problem Statement
# MAGIC
# MAGIC You have a collection of books, each with a **height** and **thickness** (width). You want to arrange them on a bookshelf with a fixed **shelf width** `W`.
# MAGIC
# MAGIC Books must be placed **in the given order** — you cannot rearrange them. You place books left to right on the current shelf. If a book doesn't fit on the current shelf (i.e., the total thickness would exceed `W`), you start a **new shelf** above.
# MAGIC
# MAGIC Each shelf's height is equal to the **tallest book** on that shelf. The total height of the bookshelf is the **sum of all shelf heights**.
# MAGIC
# MAGIC Given a list of `books` where each book is `[thickness, height]`, and a shelf width `W`, return the **minimum total height** of the bookshelf.
# MAGIC
# MAGIC ## Examples
# MAGIC
# MAGIC **Example 1:**
# MAGIC ```
# MAGIC Input: books = [[1, 3], [2, 4], [1, 2], [3, 1]], W = 4
# MAGIC
# MAGIC Shelf arrangement:
# MAGIC - Shelf 1: Book 0 (th=1, h=3) + Book 1 (th=2, h=4) → total thickness = 3 ≤ 4, shelf height = max(3,4) = 4
# MAGIC - Shelf 2: Book 2 (th=1, h=2) + Book 3 (th=3, h=1) → total thickness = 4 ≤ 4, shelf height = max(2,1) = 2
# MAGIC
# MAGIC Total height = 4 + 2 = 6
# MAGIC Output: 6
# MAGIC ```
# MAGIC
# MAGIC **Example 2:**
# MAGIC ```
# MAGIC Input: books = [[1, 1], [1, 1], [1, 1]], W = 1
# MAGIC
# MAGIC Each book is thickness 1, shelf width is 1, so one book per shelf:
# MAGIC - Shelf 1: height 1
# MAGIC - Shelf 2: height 1
# MAGIC - Shelf 3: height 1
# MAGIC
# MAGIC Total height = 1 + 1 + 1 = 3
# MAGIC Output: 3
# MAGIC ```
# MAGIC
# MAGIC **Example 3:**
# MAGIC ```
# MAGIC Input: books = [[4, 5], [2, 3]], W = 4
# MAGIC
# MAGIC - Shelf 1: Book 0 (th=4, h=5) → thickness = 4 ≤ 4, shelf height = 5
# MAGIC - Shelf 2: Book 1 (th=2, h=3) → thickness = 2 ≤ 4, shelf height = 3
# MAGIC
# MAGIC Total height = 5 + 3 = 8
# MAGIC Output: 8
# MAGIC ```
# MAGIC
# MAGIC ## Constraints
# MAGIC
# MAGIC * `1 <= len(books) <= 100`
# MAGIC * `1 <= books[i][0] (thickness) <= W`
# MAGIC * `1 <= books[i][1] (height) <= 1000`
# MAGIC * `1 <= W <= 1000`
# MAGIC
# MAGIC ## Your Task
# MAGIC
# MAGIC Write a function `min_shelf_height(books, W)` that returns the minimum total height of the bookshelf.

# COMMAND ----------

# DBTITLE 1,Your Solution
def min_shelf_height(books, W):
    """
    Returns the minimum total height of the bookshelf.

    Books must be placed in order. If the current shelf can't fit
    the next book (thickness exceeds W), start a new shelf.
    Each shelf's height = tallest book on that shelf.

    Args:
        books (List[List[int]]): Each book is [thickness, height].
        W (int): Maximum shelf width.

    Returns:
        int: Minimum total height of all shelves.
    """
    # dp[i] = minimum total height for the first i books.
    # For each i, try every possible group of trailing books that can share
    # the last shelf (walk backwards while total thickness <= W).
    n = len(books)
    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        thickness = 0
        shelf_height = 0
        for j in range(i - 1, -1, -1):
            thickness += books[j][0]
            if thickness > W:
                break
            shelf_height = max(shelf_height, books[j][1])
            dp[i] = min(dp[i], dp[j] + shelf_height)
    return dp[n]


# --- Test Cases ---
# Note: Tests 1 and 8 originally expected 6 and 8, but per the problem's own
# rules a better (valid) arrangement exists, so the true minimum is lower:
#   Test 1: [[1,3],[2,4],[1,2],[3,1]] -> books 0,1,2 fit on one shelf
#           (thickness 1+2+1=4 <= 4, height max(3,4,2)=4) + book 3 alone (1) = 5
#   Test 8: [[2,1],[2,5],[2,1],[2,1]] -> shelves [0,1] and [2,3]
#           (thickness 4 <= 4 each) -> max(1,5) + max(1,1) = 6
assert min_shelf_height([[1, 3], [2, 4], [1, 2], [3, 1]], 4) == 5, "Test 1 Failed"
assert min_shelf_height([[1, 1], [1, 1], [1, 1]], 1) == 3, "Test 2 Failed"
assert min_shelf_height([[4, 5], [2, 3]], 4) == 8, "Test 3 Failed"
assert min_shelf_height([[2, 5]], 4) == 5, "Test 4 Failed"
assert min_shelf_height([[1, 1], [1, 2], [1, 3], [1, 4]], 4) == 4, "Test 5 Failed"
assert min_shelf_height([[3, 3], [3, 3], [3, 3]], 6) == 6, "Test 6 Failed"
assert min_shelf_height([[1, 10], [1, 1], [1, 1]], 3) == 10, "Test 7 Failed"
assert min_shelf_height([[2, 1], [2, 5], [2, 1], [2, 1]], 4) == 6, "Test 8 Failed"

print("All tests passed!")