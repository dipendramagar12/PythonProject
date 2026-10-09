sentence = input("Enter a sentence: ")

text = sentence.split()
print("unnecessary space: ", text)

words = len(text)
print("Numbers of word count:",words)

lower = sentence.lower()
print("lower case: ", lower)

python_count = lower.split().count("python")
print("Word 'python' appears: ", python_count, "times")


