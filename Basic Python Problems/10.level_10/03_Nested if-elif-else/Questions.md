# Topic 3 — Nested `if-elif-else`

## Q9. Grade Calculator

Write a program that takes marks.

Use nested conditions to print:

- 90 or more → `A+`
- 80–89 → `A`
- 70–79 → `B`
- 60–69 → `C`
- 40–59 → `D`
- Below 40 → `Fail`

First check whether marks are at least 40, then use a nested `if-elif-else` to classify the passing marks.

### Test Case 1

**Input**
```text
95
```

**Output**
```text
A+
```

### Test Case 2

**Input**
```text
84
```

**Output**
```text
A
```

### Test Case 3

**Input**
```text
72
```

**Output**
```text
B
```

### Test Case 4

**Input**
```text
65
```

**Output**
```text
C
```

### Test Case 5

**Input**
```text
45
```

**Output**
```text
D
```

### Test Case 6

**Input**
```text
32
```

**Output**
```text
Fail
```

---

## Q10. Age Group

Write a program that takes age.

Use nested conditions to classify:

- 60 or above → `Senior`
- 18–59 → `Adult`
- 13–17 → `Teenager`
- 5–12 → `Child`
- Below 5 → `Small Child`

### Test Case 1

**Input**
```text
65
```

**Output**
```text
Senior
```

### Test Case 2

**Input**
```text
25
```

**Output**
```text
Adult
```

### Test Case 3

**Input**
```text
15
```

**Output**
```text
Teenager
```

### Test Case 4

**Input**
```text
9
```

**Output**
```text
Child
```

### Test Case 5

**Input**
```text
3
```

**Output**
```text
Small Child
```

---

## Q11. Number Type

Write a program that takes an integer.

First determine whether the number is:

- Positive
- Negative
- Zero

Inside the positive and negative branches, use another conditional structure to determine whether the number is even or odd.

### Test Case 1

**Input**
```text
18
```

**Output**
```text
Positive Even
```

### Test Case 2

**Input**
```text
13
```

**Output**
```text
Positive Odd
```

### Test Case 3

**Input**
```text
-12
```

**Output**
```text
Negative Even
```

### Test Case 4

**Input**
```text
-7
```

**Output**
```text
Negative Odd
```

### Test Case 5

**Input**
```text
0
```

**Output**
```text
Zero
```

---

## Q12. Divisibility Category

Write a program that takes an integer.

- If the number is positive:
  - If divisible by both 2 and 3 → `Divisible by 2 and 3`
  - Else if divisible by 2 → `Divisible by 2`
  - Else if divisible by 3 → `Divisible by 3`
  - Otherwise → `Not Divisible by 2 or 3`
- If the number is zero or negative, print `Not Positive`.

### Test Case 1

**Input**
```text
12
```

**Output**
```text
Divisible by 2 and 3
```

### Test Case 2

**Input**
```text
14
```

**Output**
```text
Divisible by 2
```

### Test Case 3

**Input**
```text
15
```

**Output**
```text
Divisible by 3
```

### Test Case 4

**Input**
```text
25
```

**Output**
```text
Not Divisible by 2 or 3
```

---