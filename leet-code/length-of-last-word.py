def lengthOfLastWord(s) -> int:
    space_position = 0
    if (" " not in s):
        return len(s)

    if ( len(s.replace(" ", "")) == 0 ):
        return 0

    i = 0
    while i < len(s) - 1:
        if (s[i] == " " and s[i + 1] != " "):
            space_position = i
        i += 1

    return len( s[space_position:].strip() )

print(lengthOfLastWord("hello world"))