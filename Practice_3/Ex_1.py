s = input()

txt = s[::-1]
output_str = txt[0].upper()

for i in range(2, len(txt), 2):
    output_str += txt[i].lower()

print(output_str)