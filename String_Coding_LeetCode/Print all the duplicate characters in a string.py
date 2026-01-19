"""
Print all the duplicate characters in a string
Last Updated : 12 Jun, 2025
Given a string s, the task is to identify all characters that appear more than once and print each as a list containing the character and its count.

Examples:

Input: s = "geeksforgeeks"
Output: ['e', 4], ['g', 2], ['k', 2], ['s', 2]
Explanation: Characters e, g, k, and s appear more than once. Their counts are shown in order of first occurrence.

Input: s = "programming"
Output: ['r', 2], ['g', 2], ['m', 2]
Explanation: Only r, g, and m are duplicates. Output lists them with their counts.

Input: s = "mississippi"
Output: ['i', 4], ['s', 4], ['p', 2]
Explanation: Characters i, s, and p have multiple occurrences. The output reflects that with count and order preserved.
"""


def print_duplicates(s):
    freq = {}
    result = []

    # Count frequency
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Preserve order of first occurrence
    seen = set()
    for ch in s:
        if freq[ch] > 1 and ch not in seen:
            result.append([ch, freq[ch]])
            seen.add(ch)

    return result
