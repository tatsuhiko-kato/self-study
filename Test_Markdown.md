<details>
<summary>Click to expand: How can I capture and print exceptions in Python?</summary>

**Question:**
Please provide a sample code to capture all exceptions and print the exception class and description.

**Answer:**
```python
try:
    # Your code that might raise exceptions
    x = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("Exception class:", type(e).__name__)
    print("Description:", str(e))