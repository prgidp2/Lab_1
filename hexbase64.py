import base64

hexadecimal = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
end_length = len(hexadecimal) * 4

hex_as_int = int(hexadecimal, 16)
hex_as_binary = bin(hex_as_int)
padded_binary = hex_as_binary[2:].zfill(end_length)

data_b2a = binascii.b2a_uu(padded_binary)

print data_b2a

base64_encoded_data = base64.b64encode(data_b2a)

print(base64_encoded_data)
