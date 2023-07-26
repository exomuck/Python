class string_utilities:
    @staticmethod
    def is_valid_parentheses(s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets:
                if not stack or stack.pop() != brackets[char]:
                    return False
        return not stack

    @staticmethod
    def reverse_words(s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)

print(string_utilities().is_valid_parentheses('{[(])]}'))
print(string_utilities().is_valid_parentheses('{[()(({}))]}'))
print(string_utilities().reverse_words('Bach khoa Ha Noi'))