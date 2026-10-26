# min-max-feature-scaling — AWS case

Beginner | problemset | data-stats-for-ds | data-cleaning | aws

AWS-inspired monitoring model combines numeric signals that arrive on very different scales. Before training, the team needs every feature mapped to a fixed interval, so you need to implement min-max scaling and handle the stated boundary cases correctly.

Map the values linearly so the minimum becomes 0 and the maximum becomes 1. If all values are equal (the range is zero) return all zeros.

Implement `solve(x)`.

**Returns.** Return a float NumPy vector in $[0,1]$.

### Examples

**Example 1**

Input:

```python
solve([10.0, 20.0, 30.0])
```

Output:

```text
[0.0, 0.5, 1.0]
```

**Example 2**

Input:

```python
solve([5.0, 5.0, 5.0])
```

Output:

```text
[0.0, 0.0, 0.0]
```

**Example 3**

Input:

```python
solve([-1.0, 0.0, 3.0])
```

Output:

```text
[0.0, 0.25, 1.0]
```
