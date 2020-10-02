y = 13
thestring = ["l","a","b","e","l"]

print("Here is your flag:")
print("".join(chr(ord(z) ^ y) for z in thestring))
