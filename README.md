# prime-numbers

Prime numbers (revisited)
This second part is a reimplementation of the prime numbers algorithm from assignment #2, but this time using an iterator class, and then, a simpler generator class.

Structure & naming
Write a test module called test_prime.py
Write a module called prime.py
Create an iterable class called prime_factors which requires a single positional argument as a constructor
Requirements & build steps

Step 1:
Write a test that asserts that when prime_factors is called with a data type that is not an integer (e.g. a string or float), a ValueError is raised. Write the appropriate code to solve this and then commit the changes.

Step 2:
Write a test that asserts that when prime_factors is called with 1, an empty list will be generated. Solve & commit.

Step 3:
Write a test that asserts that when prime_factors is called with 2, the list [2] will be generated. Solve & commit.

Step 4:
Write a test that asserts that when prime_factors is called with 3, the list [3] will be generated. Solve & commit.

Step 5:
Write a test that asserts that when prime_factors is called with 4, the list [2, 2] will be generated. Solve & commit.

Step 6:
Write a test that asserts that when prime_factors is called with 6, the list [2, 3] will be generated. Solve & commit.

Step 7:
Write a test that asserts that when prime_factors is called with 8, the list [2, 2, 2] will be generated. Solve & commit.

Step 8:
Write a test that asserts that when prime_factors is called with 9, the list [3, 3] will be generated. Solve & commit.

Refactor
Now that we have a working iterable class backed by our test suite, we can replace the implementation with a simpler, generator function. Note: there is a caveat around generators as they are lazily evaluated – meaning, a special workaround is needed to evaluate the value parameter upon calling.
