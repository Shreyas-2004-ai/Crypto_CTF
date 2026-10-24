### ACTIVITY1_INTRO.PY

# CryptoHack – Great Snakes

## Challenge Information

- **Platform:** CryptoHack
- **Challenge:** Great Snakes
- **Category:** Introduction
- **Concept:** Python, ASCII, Bitwise XOR

## Challenge Description

The challenge provides a Python script containing a list of encoded integers. Our objective is to understand the code and execute it to retrieve the hidden flag.

## Python Code

```python
import sys

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))
```

## Code Explanation

### 1. Importing the sys Module

```python
import sys
```

The `sys` module provides information about the Python interpreter, including its version.

### 2. Checking the Python Version

```python
if sys.version_info.major == 2:
```

Checks whether the program is running on Python 2 and displays a warning because Python 2 is no longer supported.

### 3. Encoded Integer List

```python
ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
```

The list contains integer values representing characters encoded using the XOR operation.

### 4. Decoding Using XOR

```python
print("".join(chr(o ^ 0x32) for o in ords))
```

- `0x32` represents the decimal value `50`.
- `^` performs bitwise XOR between each integer and `50`.
- `chr()` converts the decoded ASCII value into a character.
- `join()` combines all decoded characters into a single string.

**Example:**

```python
81 ^ 0x32 = 99
chr(99) = 'c'
```

The same operation is repeated for every integer in the list.

## Output

```text
Here is your flag:
crypto{z3n_0f_pyth0n}
```

## Flag

`crypto{z3n_0f_pyth0n}`

## Conclusion

This challenge demonstrates how Python can decode XOR-encoded data. It introduces important concepts such as ASCII values, hexadecimal notation, bitwise XOR operations, and character conversion.

The key observation is that XOR is reversible: applying the same XOR key again restores the original data.