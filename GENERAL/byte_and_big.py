from Crypto.Util.number import long_to_bytes

number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert integer to bytes
decoded_bytes = long_to_bytes(number)

# Convert bytes to readable text
flag = decoded_bytes.decode("utf-8")

print("Flag:", flag)
