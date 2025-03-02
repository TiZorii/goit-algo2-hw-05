# Homework for the topic "Algorithms for Working with Big Data"

To begin, you need to install the dependencies using the following command:

`pip install -r requirements.txt.`

Next, you should download a dataset from a real log file `lms-stage-access.log`, which contains information about IP addresses.

## Task 1. Checking Password Uniqueness Using Bloom Filter

Create a function to check password uniqueness using a Bloom Filter. This function should determine whether a password has been used before, without the need to store the actual passwords.

### Technical Requirements

1. Implement a `BloomFilter` class that supports adding elements to the filter and checking the presence of an element in the filter.

2. Implement the `check_password_uniqueness` function, which uses an instance of `BloomFilter` and checks a list of new passwords for uniqueness. It should return the check result for each password.

3. Ensure proper handling of all data types. Passwords should be processed as plain strings, without hashing. Empty or invalid values should also be considered and handled appropriately.

4. The function and class should work with large datasets, using minimal memory.

### How to Run

```
python task_1.py
```

## Task 2. Comparing HyperLogLog Performance with Exact Count of Unique Elements

Create a script to compare the exact count of unique elements with the count using HyperLogLog.

### Technical Requirements

1. Download a dataset from a real log file `lms-stage-access.log`, which contains information about IP addresses.

2. Implement a method for the exact count of unique IP addresses using the `set` data structure.

3. Implement a method for approximating the count of unique IP addresses using `HyperLogLog`.

4. Compare the methods in terms of execution time.

### How to Run

```
python task_2.py
```

