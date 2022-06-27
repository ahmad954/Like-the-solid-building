# demonstrate hashtable usage


# TODO: create a hashtable all at once

hash1=dict({"A":1,"B":2,"C":3,"D":"KEY4"})
print(hash1)
# TODO: create a hashtable progressively
hash2 = {}

hash2["a"] = 1
hash2["b"] = 2
hash2["c"] = 3
hash2["d"] = "key4"


# TODO: try to access a nonexistent key
#print(hash2["g"])


# TODO: replace an item
hash2["a"]= 5

print(hash2["a"])

# TODO: iterate the keys and values in the dictionary

for key,value in hash2.items():
    print("key:",key,"val:",value)
