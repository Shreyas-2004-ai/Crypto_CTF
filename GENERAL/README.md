# CryptoHack CTF — Introduction Challenges

This README documents the Python solutions, explanations, and lessons learned from four CryptoHack challenges: **ASCII**, **Hex**, **Base64**, and **Bytes and Big Integers**.

> These exercises use encoding and representation conversions. ASCII, hexadecimal, and Base64 are **not encryption** and do not provide confidentiality.

## Challenges at a glance

| Challenge | Input representation | Operation | Result |
| --- | --- | --- | --- |
| ASCII | Decimal character codes | `chr()` and `join()` | `crypto{ASCII_pr1nt4bl3}` |
| Hex | Hexadecimal text | `bytes.fromhex()` | `crypto{You_will_be_working_with_hex_strings_a_lot}` |
| Base64 | Hexadecimal text | Hex → bytes → Base64 | `crypto/Base+64+Encoding+is+Web+Safe/` |
| Bytes and Big Integers | Large decimal integer | `long_to_bytes()` | `crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}` |

## 1. ASCII

**Objective:** Convert a list of decimal ASCII values into a readable flag.

```python
ascii_values = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

flag = "".join(chr(value) for value in ascii_values)
print(flag)
```

**Output:**

```text
crypto{ASCII_pr1nt4bl3}
```

**Explanation:** ASCII assigns numerical codes to characters. `chr(99)` gives `c`, for example. The generator converts every number to a character and `"".join(...)` combines them. The reverse operation, `ord('c')`, returns `99`.

**Takeaway:** `chr()` converts an integer code to a character; `ord()` converts a character to its integer code.

## 2. Hex

**Objective:** Decode a hexadecimal string into bytes and read the text.

```python
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

decoded_bytes = bytes.fromhex(hex_string)
flag = decoded_bytes.decode("utf-8")
print(flag)
```

**Output:**

```text
crypto{You_will_be_working_with_hex_strings_a_lot}
```

**Explanation:** Each two hexadecimal digits encode one byte. For example, `63` (hex) = `99` (decimal) = `c` (ASCII). `bytes.fromhex()` reconstructs the byte sequence, and `.decode('utf-8')` displays it as text. The reverse conversion is `decoded_bytes.hex()`.

**Takeaway:** Hex is a readable representation of bytes, not a cipher.

## 3. Base64

**Objective:** First decode the supplied hex string into bytes, then encode those bytes as Base64 text.

```python
import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

raw_bytes = bytes.fromhex(hex_string)
encoded_bytes = base64.b64encode(raw_bytes)
flag = encoded_bytes.decode("ascii")
print(flag)
```

**Output:**

```text
crypto/Base+64+Encoding+is+Web+Safe/
```

**Explanation:** `bytes.fromhex()` produces the original binary data. `base64.b64encode()` converts it into printable Base64 bytes. `.decode('ascii')` makes the result a Python string. Base64 represents every three bytes using four 6-bit symbols, with padding where necessary.

### Error encountered and fix

The original script was named `base64.py`. Running `import base64` then imported that local script instead of Python's standard-library `base64` module, causing:

```text
AttributeError: partially initialized module 'base64' has no attribute 'b64encode'
```

**Fix:** Rename the file to `base64_challenge.py`. If necessary, remove the stale `base64` entry inside `__pycache__` and rerun the renamed script.

**Takeaway:** Avoid naming scripts after standard-library modules such as `base64.py`, `json.py`, `socket.py`, or `random.py`.

## 4. Bytes and Big Integers

**Objective:** Convert a large decimal integer back into the message bytes used in number-based cryptography such as RSA.

Install the dependency with the Python interpreter you use to run the script:

```powershell
python -m pip install pycryptodome
```

**Solution:**

```python
from Crypto.Util.number import long_to_bytes, bytes_to_long

number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

message_bytes = long_to_bytes(number)
flag = message_bytes.decode("utf-8")
print(flag)

# Optional verification: converting back recovers the input integer.
assert bytes_to_long(message_bytes) == number
```

**Output:**

```text
crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
```

**Explanation:** Cryptographic mathematics often works with integers, while text is stored as bytes. `bytes_to_long()` interprets a byte sequence as one big-endian integer; `long_to_bytes()` converts that integer back to bytes. UTF-8 decoding then produces readable text.

**Takeaway:** Converting text to an integer is a representation step used before mathematical cryptographic operations; it is not encryption on its own.

## Summary of useful Python functions

| Function | Conversion |
| --- | --- |
| `chr(n)` | Integer character code → character |
| `ord(c)` | Character → integer character code |
| `bytes.fromhex(s)` | Hex string → bytes |
| `data.hex()` | Bytes → hex string |
| `base64.b64encode(data)` | Bytes → Base64 bytes |
| `base64.b64decode(data)` | Base64 bytes/string → bytes |
| `bytes_to_long(data)` | Bytes → big-endian integer |
| `long_to_bytes(n)` | Big-endian integer → bytes |

## Running the solutions

Use Python 3. The first three challenges need no third-party packages. The fourth requires `pycryptodome`.

On Windows, if `python` points to a different Python installation than the one where dependencies were installed, select the correct interpreter in VS Code or run its executable explicitly.

## Conclusion

These challenges introduce ways to represent the same information as characters, bytes, hexadecimal text, Base64 text, or large integers. Understanding these conversions is essential for interpreting cryptographic inputs and outputs and writing Python solutions for later CryptoHack challenges.
