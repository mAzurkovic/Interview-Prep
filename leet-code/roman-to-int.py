roman_mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def romanToInt(s: str) -> int:
    # s is Roman string     
    sum = 0   
    i = 0
    while (i < len(s)):
        current_char = s[i]
        # Check if out of bounds 
        if ( i < len(s) - 1 ): 
            next_char = s[i + 1]
            # Check if next number is smaller
            if (roman_mapping[current_char] < roman_mapping[next_char]):
                sum = sum + (roman_mapping[next_char] - roman_mapping[current_char])
                i = i + 1
            else:
                sum = sum + roman_mapping[current_char]
        else:
            sum = sum + roman_mapping[current_char]

        i = i + 1

    return (sum)

print(romanToInt("MCMXCIV"))