s = input()
words = s.split("_")
output_str = words[0].capitalize() + "".join(word.capitalize() for word in words[1:])

print(output_str)