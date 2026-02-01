piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ["do", "re", "mi", "fa", "so", "la", "ti"]

print(piano_keys[2:5]) # prints ['c', 'd', 'e'] which is from index 2 to index 4 ( stop at index = 5 which means 5 is not with us )
print(piano_keys[:5])
print(piano_keys[2:])
print(piano_keys[2:5:2]) # list[start:stop:step]
print(piano_keys[::2])
print(piano_keys[::-1]) # This line reverses the entire list
print(piano_tuple[2:5])
print(piano_tuple[1::]) # Start at index 1 (the second item). Go to the end.
