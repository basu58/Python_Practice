# Databricks notebook source


# COMMAND ----------

# DBTITLE 1,Question: Exam Seating Arrangement
# MAGIC %md
# MAGIC # Question: Exam Seating Arrangement
# MAGIC
# MAGIC ## Problem Statement
# MAGIC
# MAGIC A classroom has students appearing for an exam. You are given a list `students` where each element is a tuple `(student_name, roll_number)` representing the order in which students arrived at the exam hall.
# MAGIC
# MAGIC The exam hall has seats arranged in a **single row** with seat numbers starting from `1`. The invigilator follows these rules to assign seats:
# MAGIC
# MAGIC 1. Students are seated **in the order they arrived**
# MAGIC 2. The **first** student sits at seat `1`
# MAGIC 3. For each subsequent student, if their **roll number is even**, they sit at the **next available seat from the front**; if their **roll number is odd**, they sit at the **next available seat from the end** of the row
# MAGIC
# MAGIC After all students are seated, return a list of tuples `(seat_number, student_name)` sorted by seat number in ascending order.
# MAGIC
# MAGIC ## Examples
# MAGIC
# MAGIC **Example 1:**
# MAGIC ```
# MAGIC Input: students = [("Alice", 101), ("Bob", 102), ("Charlie", 103), ("Diana", 104)]
# MAGIC
# MAGIC Seating process:
# MAGIC - Alice (roll 101, odd)  → seat from end → seat 4
# MAGIC - Bob   (roll 102, even) → seat from front → seat 1
# MAGIC - Charlie (roll 103, odd) → seat from end → seat 3
# MAGIC - Diana (roll 104, even) → seat from front → seat 2
# MAGIC
# MAGIC Output: [(1, "Bob"), (2, "Diana"), (3, "Charlie"), (4, "Alice")]
# MAGIC ```
# MAGIC
# MAGIC **Example 2:**
# MAGIC ```
# MAGIC Input: students = [("Zara", 10), ("Mike", 15)]
# MAGIC
# MAGIC Seating process:
# MAGIC - Zara (roll 10, even)  → seat from front → seat 1
# MAGIC - Mike (roll 15, odd)   → seat from end → seat 2
# MAGIC
# MAGIC Output: [(1, "Zara"), (2, "Mike")]
# MAGIC ```
# MAGIC
# MAGIC **Example 3:**
# MAGIC ```
# MAGIC Input: students = [("Solo", 99)]
# MAGIC
# MAGIC Output: [(1, "Solo")]
# MAGIC ```
# MAGIC
# MAGIC ## Constraints
# MAGIC
# MAGIC * `1 <= len(students) <= 100`
# MAGIC * `students[i]` is a tuple `(name: str, roll_number: int)`
# MAGIC * `roll_number` is a positive integer
# MAGIC * All seat numbers are unique and range from `1` to `n`
# MAGIC
# MAGIC ## Your Task
# MAGIC
# MAGIC Write a function `assign_seats(students)` that returns the seating arrangement as a list of `(seat_number, student_name)` tuples sorted by seat number.

# COMMAND ----------

# DBTITLE 1,Your Solution
def assign_seats(students):
    """
    Assigns seats to students based on arrival order and roll number parity.
    Even roll → seat from front, Odd roll → seat from end.

    Returns list of (seat_number, student_name) sorted by seat number.
    """
    # TODO: Write your solution here
    pass


# --- Test Cases ---
# Uncomment after implementing your solution
# result = assign_seats([("Alice", 101), ("Bob", 102), ("Charlie", 103), ("Diana", 104)])
# assert result == [(1, "Bob"), (2, "Diana"), (3, "Charlie"), (4, "Alice")], f"Test 1 Failed: {result}"

# result = assign_seats([("Zara", 10), ("Mike", 15)])
# assert result == [(1, "Zara"), (2, "Mike")], f"Test 2 Failed: {result}"

# result = assign_seats([("Solo", 99)])
# assert result == [(1, "Solo")], f"Test 3 Failed: {result}"

# result = assign_seats([("A", 2), ("B", 4), ("C", 6)])
# assert result == [(1, "A"), (2, "B"), (3, "C")], f"Test 4 Failed: {result}"

# result = assign_seats([("A", 1), ("B", 3), ("C", 5)])
# assert result == [(1, "C"), (2, "B"), (3, "A")], f"Test 5 Failed: {result}"

# result = assign_seats([("P", 2), ("Q", 1), ("R", 4), ("S", 3)])
# assert result == [(1, "P"), (2, "R"), (3, "S"), (4, "Q")], f"Test 6 Failed: {result}"

print("Implement the function and uncomment the test cases to check your solution!")