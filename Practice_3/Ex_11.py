n = int(input())
s = input()
# YOUR CODE HERE
def caesar_cipher(s, n):
    s = s.lower()
    shift = [chr((ord(char) - 97 + n) % 26 + 97) if char.isalpha() else char for char in s]
    return ''.join(shift)
print(caesar_cipher(s, n))