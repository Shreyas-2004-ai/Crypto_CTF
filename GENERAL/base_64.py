import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

#  Convert hexadecimal to bytes
decoded_bytes = bytes.fromhex(hex_string)

#  Encode bytes into Base64
base64_bytes = base64.b64encode(decoded_bytes)

# Convert Base64 bytes to a string
flag = base64_bytes.decode("utf-8")

print("Flag:", flag)