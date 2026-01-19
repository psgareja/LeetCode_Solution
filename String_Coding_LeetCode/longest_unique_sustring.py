def longest_unique_substring(s: str) -> str:
    char_set = set()
    left = 0
    max_len = 0
    result = ""

    for right, char in enumerate(s):
        while char in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(char)

        if right - left + 1 > max_len:
            max_len = right - left + 1
            result = s[left:right + 1]

    return result


print(longest_unique_substring("abdbabceddbbd"))
