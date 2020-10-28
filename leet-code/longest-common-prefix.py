def longestCommonPrefix(strs) -> str:
    shortest_length = 0
    if (len(strs) > 0):
        shortest_length = len(strs[0]) 
    else:
        return ""

    shortest_index = 0
    prefix = ""
    letters = {}

    # Get shortest string and its index...
    for i in strs:
        if len(i) < shortest_length:
            shortest_index = strs.index(i)
            shortest_length = len(i)

    # Initialize hash map with 0 counters
    i = 0
    while i < shortest_length:
        letters[strs[0][i]] = 0
        i = i + 1  

    # Loop through all letters and add cadence to hashmap...
    for word in strs:
        for current_char in word:
            if (current_char not in letters):
                letters[current_char] = 1
            else:
                letters[current_char] = letters[current_char] + 1

    print(letters)

    # Loop and check hashmap cadences...
    for letter in strs[shortest_index]:
        if letters[letter] == len(strs):
            prefix = prefix + letter
        else:
            break

    print(prefix)


longestCommonPrefix(["cir","car"])