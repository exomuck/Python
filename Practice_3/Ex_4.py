def mirror(s):
    mirror_chars = {
        'a': 'NOT POSSIBLE', 'A': 'NOT POSSIBLE',
        'b': 'd', 'B': 'NOT POSSIBLE',
        'c': 'NOT POSSIBLE', 'C': 'NOT POSSIBLE',
        'd': 'b', 'D': 'NOT POSSIBLE',
        'e': 'NOT POSSIBLE', 'E': 'NOT POSSIBLE',
        'f': 'NOT POSSIBLE', 'F': 'NOT POSSIBLE',
        'g': 'NOT POSSIBLE', 'G': 'NOT POSSIBLE',
        'h': 'NOT POSSIBLE', 'H': 'NOT POSSIBLE',
        'i': 'i', 'I': 'NOT POSSIBLE',
        'j': 'NOT POSSIBLE', 'J': 'NOT POSSIBLE',
        'k': 'NOT POSSIBLE', 'K': 'NOT POSSIBLE',
        'l': 'NOT POSSIBLE', 'L': 'NOT POSSIBLE',
        'm': 'NOT POSSIBLE', 'M': 'NOT POSSIBLE',
        'n': 'NOT POSSIBLE', 'N': 'NOT POSSIBLE',
        'o': 'o', 'O': 'NOT POSSIBLE',
        'p': 'q', 'P': 'NOT POSSIBLE',
        'q': 'p', 'Q': 'NOT POSSIBLE',
        'r': 'NOT POSSIBLE', 'R': 'NOT POSSIBLE',
        's': 'NOT POSSIBLE', 'S': 'NOT POSSIBLE',
        't': 'NOT POSSIBLE', 'T': 'NOT POSSIBLE',
        'u': 'NOT POSSIBLE', 'U': 'NOT POSSIBLE',
        'v': 'v', 'V': 'NOT POSSIBLE',
        'w': 'w', 'W': 'NOT POSSIBLE',
        'x': 'x', 'X': 'NOT POSSIBLE',
        'y': 'NOT POSSIBLE', 'Y': 'NOT POSSIBLE',
        'z': 'NOT POSSIBLE', 'Z': 'NOT POSSIBLE'
    }

    # Handle empty strings
    if not s:
        return ''

        # Handle one-character strings
    if len(s) == 1:
        return mirror_chars.get(s, 'NOT POSSIBLE')

        # Create a list of mirror characters for each non-space character in the input string
    mirror_chars_list = [mirror_chars.get(c, 'NOT POSSIBLE') for c in s if c != ' ']

    # Check if the mirror image is valid
    if 'NOT POSSIBLE' in mirror_chars_list:
        return 'NOT POSSIBLE'

    # Create a list of characters for the mirror image with spaces preserved
    s_chars = list(s)
    for i in range(len(s_chars)):
        if s_chars[i] == ' ':
            continue
        s_chars[i] = mirror_chars_list.pop()
    return ''.join(s_chars)

print(mirror("vOid void"))