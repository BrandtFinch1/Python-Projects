sentence=input("Input a sentence: ")
print(f"Original sentence: {sentence}")

sliced_string= sentence[0:5]
print (f"First 5 characters: {sliced_string}")

lowercase= sentence.lower()
print(f"Sentence in lowercase: {lowercase}")

underscore= sentence.replace(" ", "_")
print(f"Spaces replaced with underscores: {underscore}")

list=sentence.split()
print(f"List of words: {list}")

hyphenated = "-".join(list)
print(f"Hyphen-joined string: {hyphenated}")

