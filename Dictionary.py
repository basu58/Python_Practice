# Databricks notebook source
# DBTITLE 1,Python Dictionary — Complete Guide
# MAGIC %md
# MAGIC # Python Dictionary — Complete Guide
# MAGIC
# MAGIC A **dictionary** is an unordered, mutable (changeable), and indexed collection of key-value pairs. Each key must be **unique** and **immutable** (e.g., strings, numbers, tuples). Values can be anything.
# MAGIC
# MAGIC ## Creating a Dictionary
# MAGIC
# MAGIC ```python
# MAGIC # Empty dictionary
# MAGIC empty_dict = {}
# MAGIC
# MAGIC # Dictionary with key-value pairs
# MAGIC student = {"name": "Basudev", "age": 25, "city": "Bhubaneswar"}
# MAGIC
# MAGIC # Using dict() constructor
# MAGIC person = dict(name="Alice", age=30, city="New York")
# MAGIC
# MAGIC # Dictionary with different value types
# MAGIC mixed = {"name": "Bob", "scores": [90, 85, 95], "active": True}
# MAGIC ```
# MAGIC
# MAGIC ## Key Rules
# MAGIC * Keys must be **unique** — duplicate keys overwrite earlier values
# MAGIC * Keys must be **immutable** — strings, numbers, tuples (lists are NOT allowed as keys)
# MAGIC * Values can be **any type** — including lists, dicts, functions, etc.

# COMMAND ----------

# DBTITLE 1,Built-in Functions Reference
# MAGIC %md
# MAGIC ## Built-in Dictionary Functions
# MAGIC
# MAGIC ### View Methods
# MAGIC | Method | Returns | Description |
# MAGIC |---|---|---|
# MAGIC | `.keys()` | `dict_keys` | All keys in the dictionary |
# MAGIC | `.values()` | `dict_values` | All values in the dictionary |
# MAGIC | `.items()` | `dict_items` | All key-value pairs as tuples |
# MAGIC
# MAGIC ### Modify Methods
# MAGIC | Method | Returns | Description |
# MAGIC |---|---|---|
# MAGIC | `.update(other)` | `None` | Adds/updates key-value pairs from another dict or iterable |
# MAGIC | `.pop(key)` | value | Removes and returns the value for the key (error if key missing) |
# MAGIC | `.pop(key, default)` | value | Same but returns default if key missing |
# MAGIC | `.popitem()` | tuple | Removes and returns the last inserted key-value pair |
# MAGIC | `.setdefault(key, default)` | value | Returns value if key exists, else inserts key with default and returns it |
# MAGIC | `.clear()` | `None` | Removes all key-value pairs (empties the dict) |
# MAGIC | `.copy()` | dict | Returns a shallow copy of the dictionary |
# MAGIC
# MAGIC ### Class Method
# MAGIC | Method | Returns | Description |
# MAGIC |---|---|---|
# MAGIC | `dict.fromkeys(keys, value)` | dict | Creates a new dict from a sequence of keys with an optional default value |

# COMMAND ----------

# DBTITLE 1,View Methods: keys, values, items
# === View Methods: keys(), values(), items() ===

employee = {"name": "Alice", "dept": "Engineering", "salary": 75000, "level": 3}

# .keys() — get all keys
print("Keys:", list(employee.keys()))

# .values() — get all values
print("Values:", list(employee.values()))

# .items() — get all key-value pairs as tuples
print("Items:", list(employee.items()))

# Iterating with .items() — most common pattern
print("\nIterating:")
for key, value in employee.items():
    print(f"  {key} → {value}")

# COMMAND ----------

# DBTITLE 1,Modify Methods: update, pop, popitem, setdefault
# === Modify Methods: update(), pop(), popitem(), setdefault() ===

inventory = {"apple": 50, "banana": 30, "cherry": 15}
print("Original:", inventory)

# .update() — merge another dict into current
inventory.update({"apple": 60, "grape": 25})  # updates apple, adds grape
print("\nAfter update:", inventory)

# .pop(key) — remove and return value for a key
removed = inventory.pop("banana")
print(f"\nPopped 'banana': {removed}")
print("After pop:", inventory)

# .pop(key, default) — safe pop with default
removed_safe = inventory.pop("mango", "Not found")
print(f"\nPopped 'mango' (safe): {removed_safe}")

# .popitem() — remove and return last inserted pair
last_pair = inventory.popitem()
print(f"\nPopitem (last pair): {last_pair}")
print("After popitem:", inventory)

# .setdefault(key, default) — get value if key exists, else set default
print("\nSetdefault 'apple' (exists):", inventory.setdefault("apple", 100))   # returns 60 (existing)
print("Setdefault 'orange' (new):", inventory.setdefault("orange", 40))     # inserts 40, returns 40
print("After setdefault:", inventory)

# COMMAND ----------

# DBTITLE 1,copy, clear, fromkeys
# === copy(), clear(), fromkeys() ===

# .copy() — shallow copy (new dict, same values)
original = {"a": 1, "b": [2, 3]}
copied = original.copy()
copied["a"] = 99          # doesn't affect original (int is immutable)
copied["b"].append(4)     # DOES affect original's list (shallow copy!)
print("Original:", original)  # 'a' unchanged, but 'b' list was modified
print("Copy:", copied)

# .clear() — remove all key-value pairs
temp = {"x": 10, "y": 20}
temp.clear()
print("\nAfter clear:", temp)  # {}

# dict.fromkeys() — create dict from a sequence of keys
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "unknown")
print("\nfromkeys:", new_dict)

# Without default value — all values are None
none_dict = dict.fromkeys(keys)
print("fromkeys (no default):", none_dict)

# COMMAND ----------

# DBTITLE 1,Dictionary Comprehension & Nested Dicts
# MAGIC %md
# MAGIC ## Dictionary Comprehension
# MAGIC
# MAGIC A concise way to create dictionaries using a single expression.
# MAGIC
# MAGIC **Syntax:**
# MAGIC ```python
# MAGIC {key_expr: value_expr for item in iterable if condition}
# MAGIC ```
# MAGIC
# MAGIC **Example:**
# MAGIC ```python
# MAGIC # Square of numbers 1-5
# MAGIC squares = {x: x**2 for x in range(1, 6)}
# MAGIC # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# MAGIC
# MAGIC # Filter even numbers only
# MAGIC even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# MAGIC # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
# MAGIC ```
# MAGIC
# MAGIC ## Nested Dictionaries
# MAGIC
# MAGIC A dictionary inside a dictionary — useful for grouping related data.
# MAGIC
# MAGIC ```python
# MAGIC students = {
# MAGIC     "alice": {"age": 20, "grade": "A"},
# MAGIC     "bob": {"age": 22, "grade": "B"}
# MAGIC }
# MAGIC # Access: students["alice"]["age"] → 20
# MAGIC ```

# COMMAND ----------

# DBTITLE 1,Comprehension & Nested Dicts Examples
# === Dictionary Comprehension & Nested Dicts ===

# Dictionary comprehension — square of numbers 1-5
squares = {x: x**2 for x in range(1, 6)}
print("Squares:", squares)

# With filter — only even numbers
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("Even squares:", even_squares)

# Nested dictionary
students = {
    "alice": {"age": 20, "grade": "A", "subjects": ["math", "physics"]},
    "bob": {"age": 22, "grade": "B", "subjects": ["chemistry", "biology"]}
}
print("\nNested dict — alice's age:", students["alice"]["age"])
print("Nested dict — bob's subjects:", students["bob"]["subjects"])

# Iterating a nested dictionary
print("\nAll students:")
for name, info in students.items():
    print(f"  {name}: age={info['age']}, grade={info['grade']}, subjects={info['subjects']}")

# Practical: word frequency counter using dictionary
sentence = "the cat sat on the mat the cat ran"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print("\nWord frequency:", word_count)

# COMMAND ----------

# DBTITLE 1,Practice Questions
# MAGIC %md
# MAGIC # Your Turn — Practice Questions
# MAGIC
# MAGIC Try solving these questions in a new code cell below:
# MAGIC
# MAGIC **Q1.** Given a dictionary `scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}`, find and print the name of the student with the **highest score** using dictionary methods.
# MAGIC
# MAGIC **Q2.** Given a string `"hello world hello python world world"`, use a dictionary to count the frequency of each word. Print the result as a dictionary.
# MAGIC
# MAGIC **Q3.** Create a dictionary using **dictionary comprehension** that maps numbers 1 to 10 to their **cubes**, but only include numbers that are **divisible by 3**.
# MAGIC
# MAGIC **Q4.** Given a nested dictionary `company = {"eng": {"size": 50, "lead": "Alice"}, "sales": {"size": 20, "lead": "Bob"}}`, write code to print the **total size** (sum of all department sizes).
# MAGIC
# MAGIC **Q5.** Given two dictionaries `dict1 = {"a": 1, "b": 2, "c": 3}` and `dict2 = {"b": 20, "d": 40}`, merge them using `.update()` and explain what happens to the key `"b"`.
# MAGIC
# MAGIC Write your answers below! 👇

# COMMAND ----------

# === Solutions to Practice Questions ===

# Q1. Student with the highest score
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}
top_student = max(scores, key=scores.get)  # max over keys, comparing their values
print(f"Q1. Top student: {top_student} with {scores[top_student]}")

# Q2. Word frequency counter
text = "hello world hello python world world"
frequency = {}
for word in text.split():
    frequency[word] = frequency.get(word, 0) + 1
print(f"\nQ2. Word frequency: {frequency}")

# Q3. Dict comprehension — cubes of numbers 1-10 divisible by 3
cubes = {x: x**3 for x in range(1, 11) if x % 3 == 0}
print(f"\nQ3. Cubes (divisible by 3): {cubes}")

# Q4. Total size across departments in a nested dict
company = {"eng": {"size": 50, "lead": "Alice"}, "sales": {"size": 20, "lead": "Bob"}}
total_size = sum(dept["size"] for dept in company.values())
print(f"\nQ4. Total company size: {total_size}")

# Q5. Merging with .update() — dict2 values overwrite dict1 on shared keys
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "d": 40}
dict1.update(dict2)
print(f"\nQ5. After update: {dict1}")
print("Q5. The key 'b' was overwritten: dict2's value 20 replaced dict1's value 2.")
print("    (update() gives priority to the dict being merged in, for any shared keys)")

# COMMAND ----------

# DBTITLE 1,Creating & Accessing
# === Creating & Accessing Dictionaries ===

# Creating dictionaries
student = {"name": "Basudev", "age": 25, "city": "Bhubaneswar"}
print("Student dict:", student)

# Accessing values using [] brackets
print("\nName:", student["name"])

# Accessing using get() — returns None if key doesn't exist (no error)
print("Age:", student.get("age"))
print("Grade (missing key):", student.get("grade"))          # None
print("Grade (with default):", student.get("grade", "Not assigned"))  # Custom default

# Adding / updating a key-value pair
student["grade"] = "A"
student["age"] = 26  # update existing key
print("\nAfter adding/updating:", student)

# Deleting a key-value pair
del student["city"]
print("After deleting 'city':", student)

# Check if key exists
print("\n'age' in student?", "age" in student)
print("'city' in student?", "city" in student)

# Length of dictionary
print("Length:", len(student))