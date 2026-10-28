# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# DBTITLE 1,Python Coding Lab — 10 Questions
# MAGIC %md
# MAGIC # Python Coding Lab — 10 Questions
# MAGIC
# MAGIC Difficulty: Easy to Medium · Suggested time: 60–75 minutes
# MAGIC
# MAGIC Each question is in its own cell below with a function stub and test cases. Implement each function, uncomment the asserts, and run to verify!
# MAGIC

# COMMAND ----------

# DBTITLE 1,Q1: Second-Largest Number
# MAGIC %md
# MAGIC ## Q1: Find the Second-Largest Number
# MAGIC
# MAGIC **Difficulty:** Easy | **Topic:** Lists
# MAGIC
# MAGIC Given a list of integers, return the **second-largest distinct number** without using `sort()` or `sorted()`.
# MAGIC
# MAGIC **Example:**
# MAGIC ```
# MAGIC Input: [10, 5, 8, 10, 7]
# MAGIC Output: 8
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Q1 Solution
def second_largest(nums):
    """Return the second-largest distinct number without sorting."""
    largest = None
    second = None
    for i in nums:
        if largest is None or i > largest:
            second, largest = largest, i
        elif i != largest and (second is None or i > second):
            second = i
    return second




# --- Test Cases ---
print(second_largest([10, 5, 8, 10, 7]))
assert second_largest([10, 5, 8, 10, 7]) == 8, "Test 1 Failed"
assert second_largest([1, 2, 3, 4, 5]) == 4, "Test 2 Failed"
assert second_largest([5, 5, 5]) is None, "Test 3 Failed"
assert second_largest([100]) is None, "Test 4 Failed"
assert second_largest([7, 3, 9, 3, 9, 1]) == 7, "Test 5 Failed"

print("All Q1 tests passed!")

# COMMAND ----------

# DBTITLE 1,Q2: Character Frequency
# MAGIC %md
# MAGIC ## Q2: Count Character Frequency
# MAGIC
# MAGIC **Difficulty:** Easy | **Topic:** Dictionaries
# MAGIC
# MAGIC Count how many times each character appears in a string. **Ignore spaces** and treat uppercase and lowercase letters as the same.
# MAGIC
# MAGIC **Example:**
# MAGIC ```
# MAGIC Input: "Data Engineer"
# MAGIC Output: {'d': 1, 'a': 2, 't': 1, 'e': 3, 'n': 2, 'g': 1, 'i': 1, 'r': 1}
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Q2 Solution
def char_frequency(s):
    """Return a dictionary of character frequencies (case-insensitive, ignore spaces)."""
    dic1 = {}
    for ch in s.lower():
        if ch != " ":
            dic1[ch] = dic1.get(ch, 0) + 1
    return dic1



# --- Test Cases ---
print(char_frequency("Data Engineer"))
assert char_frequency("Data Engineer") == {'d': 1, 'a': 2, 't': 1, 'e': 3, 'n': 2, 'g': 1, 'i': 1, 'r': 1}, "Test 1 Failed"
assert char_frequency("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}, "Test 2 Failed"
assert char_frequency("AaA") == {'a': 3}, "Test 3 Failed"
assert char_frequency("") == {}, "Test 4 Failed"
assert char_frequency("Hi Hi") == {'h': 2, 'i': 2}, "Test 5 Failed"

print("All Q2 tests passed!")

# COMMAND ----------

def char_frequency(s):
    """Return a dictionary of character frequencies (case-insensitive, ignore spaces)."""
    dic1 = {}
    for i in list(s):
        if i.lower() in dic1 and not i.isspace():
            dic1[i.lower()] +=1
        elif not i.isspace():
            dic1[i.lower()] = 1
    return dic1


# --- Test Cases ---
print(char_frequency("Data Engineer"))
assert char_frequency("Data Engineer") == {'d': 1, 'a': 2, 't': 1, 'e': 3, 'n': 2, 'g': 1, 'i': 1, 'r': 1}, "Test 1 Failed"
assert char_frequency("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}, "Test 2 Failed"
assert char_frequency("AaA") == {'a': 3}, "Test 3 Failed"
assert char_frequency("") == {}, "Test 4 Failed"
assert char_frequency("Hi Hi") == {'h': 2, 'i': 2}, "Test 5 Failed"

print("All Q2 tests passed!")

# COMMAND ----------

# DBTITLE 1,Q3: Remove Duplicates
# MAGIC %md
# MAGIC ## Q3: Remove Duplicates While Preserving Order
# MAGIC
# MAGIC **Difficulty:** Easy | **Topic:** Lists
# MAGIC
# MAGIC Remove duplicate values from a list while keeping the **first occurrence** of each value. Do not use `set()` as the final output.
# MAGIC
# MAGIC **Example:**
# MAGIC ```
# MAGIC Input: [3, 1, 3, 2, 1, 4]
# MAGIC Output: [3, 1, 2, 4]
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Q3 Solution
def remove_duplicates(lst):
    """Remove duplicates preserving first-occurrence order. Return a list."""
    li = []
    for item in lst:
        if item not in li:
            li.append(item)
    return li

print(remove_duplicates([3, 1, 3, 2, 1, 4]))
# --- Test Cases ---
assert remove_duplicates([3, 1, 3, 2, 1, 4]) == [3, 1, 2, 4], "Test 1 Failed"
assert remove_duplicates([1, 1, 1, 1]) == [1], "Test 2 Failed"
assert remove_duplicates([]) == [], "Test 3 Failed"
assert remove_duplicates([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1], "Test 4 Failed"
assert remove_duplicates([1, 2, 1, 2, 3, 3]) == [1, 2, 3], "Test 5 Failed"

print("All Q3 tests passed!")

# COMMAND ----------

# DBTITLE 1,Q4: First Non-Repeating Character
# MAGIC %md
# MAGIC ## Q4: Find the First Non-Repeating Character
# MAGIC
# MAGIC **Difficulty:** Medium | **Topic:** Strings + Dictionaries
# MAGIC
# MAGIC Return the **first character** that appears exactly once in a string. Return `None` if every character repeats.
# MAGIC
# MAGIC **Example:**
# MAGIC ```
# MAGIC Input: "swiss"
# MAGIC Output: 'w'
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Q4 Solution
def first_non_repeating(s):
    """Return the first character that appears exactly once, or None."""
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in s:
        if counts[ch] == 1:
            return ch
    return None


# --- Test Cases ---
assert first_non_repeating("swiss") == 'w', "Test 1 Failed"
assert first_non_repeating("aabbcc") is None, "Test 2 Failed"
assert first_non_repeating("abcdef") == 'a', "Test 3 Failed"
assert first_non_repeating("aabbccd") == 'd', "Test 4 Failed"
assert first_non_repeating("") is None, "Test 5 Failed"

print("All Q4 tests passed!")

# COMMAND ----------

# DBTITLE 1,Q5: Anagram Check
# MAGIC %md
# MAGIC ## Q5: Check Whether Two Strings Are Anagrams
# MAGIC
# MAGIC **Difficulty:** Easy | **Topic:** Strings
# MAGIC
# MAGIC Return `True` if two strings contain the same letters with the same frequencies, ignoring spaces and capitalization.
# MAGIC
# MAGIC **Example:**
# MAGIC ```
# MAGIC Input: "Dormitory", "Dirty room"
# MAGIC Output: True
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Q5 Solution
def is_anagram(s1, s2):
    """Return True if s1 and s2 are anagrams (ignore spaces and case)."""
    a = sorted(s1.replace(" ", "").lower())
    b = sorted(s2.replace(" ", "").lower())
    return a == b


# --- Test Cases ---
assert is_anagram("Dormitory", "Dirty room") == True, "Test 1 Failed"
assert is_anagram("listen", "silent") == True, "Test 2 Failed"
assert is_anagram("hello", "world") == False, "Test 3 Failed"
assert is_anagram("", "") == True, "Test 4 Failed"
assert is_anagram("a b c", "cba") == True, "Test 5 Failed"

print("All Q5 tests passed!")

# COMMAND ----------

# DBTITLE 1,Q6: Pairs Sum to Target
# MAGIC %md
# MAGIC ## Q6: Find Pairs That Sum to a Target
# MAGIC
# MAGIC **Difficulty:** Medium | **Topic:** Lists + Sets
# MAGIC
# MAGIC Return the **unique value pairs** whose sum equals the target. Each pair should be ordered `(smaller, larger)`, and the result should not contain duplicate pairs.
# MAGIC
# MAGIC **Example:**
# MAGIC ```
# MAGIC Input: nums = [2, 4, 3, 5, 7, 3], target = 6
# MAGIC Output: [(2, 4), (3, 3)]
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Q6 Solution
def find_pairs(nums, target):
    """Return unique value pairs (smaller, larger) that sum to target."""
    seen = set()
    pairs = set()
    for n in nums:
        complement = target - n
        if complement in seen:
            pairs.add((min(n, complement), max(n, complement)))
        seen.add(n)
    return sorted(pairs)


# --- Test Cases ---
assert find_pairs([2, 4, 3, 5, 7, 3], 6) == [(2, 4), (3, 3)], "Test 1 Failed"
assert find_pairs([1, 2, 3, 4, 5], 10) == [], "Test 2 Failed"
assert find_pairs([5, 5, 5, 5], 10) == [(5, 5)], "Test 3 Failed"
assert find_pairs([1, 9, 2, 8, 3, 7], 10) == [(1, 9), (2, 8), (3, 7)], "Test 4 Failed"
assert find_pairs([], 5) == [], "Test 5 Failed"

print("All Q6 tests passed!")

# COMMAND ----------

# DBTITLE 1,Q7: Merge Overlapping Intervals
# MAGIC %md
# MAGIC ## Q7: Merge Overlapping Intervals
# MAGIC
# MAGIC **Difficulty:** Medium | **Topic:** Sorting + Intervals
# MAGIC
# MAGIC Given a list of `[start, end]` intervals, merge all overlapping intervals and return them sorted by start.
# MAGIC
# MAGIC **Example:**
# MAGIC ```
# MAGIC Input: [[1, 3], [2, 6], [8, 10], [9, 12]]
# MAGIC Output: [[1, 6], [8, 12]]
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Q7 Solution
def merge_intervals(intervals):
    """Merge overlapping intervals and return sorted by start."""
    if not intervals:
        return []
    ordered = sorted(intervals, key=lambda iv: iv[0])
    merged = [list(ordered[0])]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


# --- Test Cases ---
assert merge_intervals([[1, 3], [2, 6], [8, 10], [9, 12]]) == [[1, 6], [8, 12]], "Test 1 Failed"
assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]], "Test 2 Failed"
assert merge_intervals([[1, 4], [2, 3]]) == [[1, 4]], "Test 3 Failed"
assert merge_intervals([[5, 10], [1, 3], [2, 6]]) == [[1, 10]], "Test 4 Failed"
assert merge_intervals([[7, 9]]) == [[7, 9]], "Test 5 Failed"

print("All Q7 tests passed!")

# COMMAND ----------

# DBTITLE 1,Q8: Most Frequent Word
# MAGIC %md
# MAGIC ## Q8: Find the Most Frequent Word
# MAGIC
# MAGIC **Difficulty:** Medium | **Topic:** Strings + Dictionaries
# MAGIC
# MAGIC Given a sentence, return the word that occurs **most often**, ignoring capitalization and basic punctuation (commas, periods). If multiple words tie, return the one that appears **first**.
# MAGIC
# MAGIC **Example:**
# MAGIC ```
# MAGIC Input: "Spark is fast, and Spark is scalable."
# MAGIC Output: 'spark'
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Q8 Solution
def most_frequent_word(sentence):
    """Return the most frequent word (lowercase, ignore punctuation). Ties → first appearing."""
    words = []
    for w in sentence.lower().split():
        w = w.strip(",.!?;:")
        if w:
            words.append(w)
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    best = None
    best_count = 0
    for w in words:
        if counts[w] > best_count:
            best = w
            best_count = counts[w]
    return best


# --- Test Cases ---
assert most_frequent_word("Spark is fast, and Spark is scalable.") == 'spark', "Test 1 Failed"
assert most_frequent_word("hello hello world") == 'hello', "Test 2 Failed"
assert most_frequent_word("one two three") == 'one', "Test 3 Failed"
assert most_frequent_word("a b a b a") == 'a', "Test 4 Failed"
assert most_frequent_word("test, test. test!") == 'test', "Test 5 Failed"

print("All Q8 tests passed!")

# COMMAND ----------

# DBTITLE 1,Q9: Flatten Nested List
# MAGIC %md
# MAGIC ## Q9: Flatten a Nested List
# MAGIC
# MAGIC **Difficulty:** Medium | **Topic:** Lists + Recursion
# MAGIC
# MAGIC Flatten a list nested to **arbitrary depth** into a single list. Assume elements are integers or lists containing more integers or lists.
# MAGIC
# MAGIC **Example:**
# MAGIC ```
# MAGIC Input: [1, [2, [3, 4]], 5]
# MAGIC Output: [1, 2, 3, 4, 5]
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Q9 Solution
def flatten(lst):
    """Flatten a list of arbitrary depth into a single list."""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


# --- Test Cases ---
assert flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5], "Test 1 Failed"
assert flatten([1, 2, 3]) == [1, 2, 3], "Test 2 Failed"
assert flatten([]) == [], "Test 3 Failed"
assert flatten([[1, [2, [3, [4, [5]]]]]]) == [1, 2, 3, 4, 5], "Test 4 Failed"
assert flatten([1, [], [2, [], 3]]) == [1, 2, 3], "Test 5 Failed"

print("All Q9 tests passed!")

# COMMAND ----------

# DBTITLE 1,Q10: Group by Department
# MAGIC %md
# MAGIC ## Q10: Group Records by Department
# MAGIC
# MAGIC **Difficulty:** Medium | **Topic:** Lists + Dictionaries
# MAGIC
# MAGIC Given employee records (list of dicts with `name`, `dept`, `salary`), group employee names by department and calculate the **average salary** for each department.
# MAGIC
# MAGIC **Example:**
# MAGIC ```
# MAGIC Input: [{'name':'Asha','dept':'IT','salary':60000},
# MAGIC         {'name':'Ravi','dept':'IT','salary':80000},
# MAGIC         {'name':'Mina','dept':'HR','salary':50000}]
# MAGIC Output: {'IT': {'employees': ['Asha', 'Ravi'], 'avg_salary': 70000.0},
# MAGIC          'HR': {'employees': ['Mina'], 'avg_salary': 50000.0}}
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Q10 Solution
def group_by_department(employees):
    """Group employees by department with names and average salary."""
    groups = {}
    for emp in employees:
        dept = emp["dept"]
        if dept not in groups:
            groups[dept] = {"employees": [], "salaries": []}
        groups[dept]["employees"].append(emp["name"])
        groups[dept]["salaries"].append(emp["salary"])
    return {
        dept: {
            "employees": info["employees"],
            "avg_salary": sum(info["salaries"]) / len(info["salaries"]),
        }
        for dept, info in groups.items()
    }


# --- Test Cases ---
result = group_by_department([{'name':'Asha','dept':'IT','salary':60000}, {'name':'Ravi','dept':'IT','salary':80000}, {'name':'Mina','dept':'HR','salary':50000}])
assert result == {'IT': {'employees': ['Asha', 'Ravi'], 'avg_salary': 70000.0}, 'HR': {'employees': ['Mina'], 'avg_salary': 50000.0}}, f"Test 1 Failed: {result}"

result = group_by_department([{'name':'A','dept':'X','salary':100}, {'name':'B','dept':'X','salary':200}, {'name':'C','dept':'Y','salary':300}])
assert result == {'X': {'employees': ['A', 'B'], 'avg_salary': 150.0}, 'Y': {'employees': ['C'], 'avg_salary': 300.0}}, f"Test 2 Failed: {result}"

result = group_by_department([])
assert result == {}, f"Test 3 Failed: {result}"

result = group_by_department([{'name':'Zoe','dept':'Eng','salary':100000}])
assert result == {'Eng': {'employees': ['Zoe'], 'avg_salary': 100000.0}}, f"Test 4 Failed: {result}"

result = group_by_department([{'name':'A','dept':'IT','salary':60}, {'name':'B','dept':'HR','salary':50}, {'name':'C','dept':'IT','salary':80}])
assert result == {'IT': {'employees': ['A', 'C'], 'avg_salary': 70.0}, 'HR': {'employees': ['B'], 'avg_salary': 50.0}}, f"Test 5 Failed: {result}"

print("All Q10 tests passed!")