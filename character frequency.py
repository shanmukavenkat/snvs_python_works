def print_char_count(line):
    line = line.lower()
    unique_chars = set(line)
    unique_chars.discard(" ")
    for char in sorted(unique_chars):
        msg = "{char}: {count}"
        line.count(char)
        print(msg.format(char=char,count=line.count(char)))

line_ = input()
print_char_count(line_)
