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


### ACTIVITY3_INTRO.PY

# CryptoHack – Network Attacks (JSON Communication)

## Challenge Information

- **Platform:** CryptoHack
- **Challenge:** Network Attacks
- **Category:** Introduction
- **Concepts:** TCP Sockets, JSON, Client–Server Communication, Python Pwntools
- **Server:** `socket.cryptohack.org`
- **Port:** `11112`

## Challenge Objective

The objective is to establish a TCP connection with the CryptoHack challenge server and retrieve the flag by sending a valid JSON request.

The server communicates using JSON objects and expects a request containing the key `buy` with the value `flag`.

## Initial Approach

We used the Python `pwntools` library to connect to the server.

Initially, the request was:

```python
request = {
    "buy": "clothes"
}
```

The server returned:

```text
{'error': 'Sorry! All we have to sell are flags.'}
```

### Observation

The TCP connection was established successfully, and the server correctly processed our JSON request.

However, the requested item, `clothes`, was invalid because the server only provides flags.

## Modification Made

Based on the server response and challenge instructions, we modified the JSON request.

**Before:**

```python
request = {
    "buy": "clothes"
}
```

**After:**

```python
request = {
    "buy": "flag"
}
```

This change allows us to request the intended item from the server.

## Final Python Code

```python
#!/usr/bin/env python3

from pwn import *
import json

HOST = "socket.cryptohack.org"
PORT = 11112

r = remote(HOST, PORT)

def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

# Read welcome messages
print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())

# Send the modified JSON request
request = {
    "buy": "flag"
}

json_send(request)

# Receive server response
response = json_recv()

print(response)

r.close()
```

## Code Explanation

| Function / Statement | Description |
|---|---|
| `from pwn import *` | Imports the pwntools library for network communication |
| `import json` | Imports Python's JSON handling module |
| `remote(HOST, PORT)` | Establishes a TCP connection with the server |
| `r.readline()` | Reads a line of data received from the server |
| `json.dumps()` | Converts a Python dictionary into a JSON string |
| `.encode()` | Converts the JSON string into bytes |
| `r.sendline()` | Sends data to the server followed by a newline |
| `.decode()` | Converts received bytes into a string |
| `json.loads()` | Converts received JSON into a Python dictionary |
| `r.close()` | Closes the TCP connection |

## Result

**Initial response:**

```text
{'error': 'Sorry! All we have to sell are flags.'}
```

**Corrected request:**

```json
{"buy": "flag"}
```

After submitting the corrected request, the server is expected to return the flag in its JSON response.

**Flag:** To be recorded after verifying the final server response.

## Conclusion

This challenge introduces network communication using Python and the `pwntools` library.

We successfully established a TCP connection with the CryptoHack server and learned how to exchange JSON messages.

The initial request failed because an incorrect value was supplied. By analyzing the server's error response and modifying the request from `clothes` to `flag`, we corrected the communication.

### Key Learnings

1. Establishing TCP connections using Python.
2. Sending and receiving JSON objects.
3. Understanding client–server communication.
4. Analyzing server error responses.
5. Modifying requests based on the server's expected input.