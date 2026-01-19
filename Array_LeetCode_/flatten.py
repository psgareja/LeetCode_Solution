"""
Flatten Array 
"""
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result += flatten(item)
        else:
            result.append(item)
    return result

nested = [1, [2, [3, 4]], 5]
print(flatten(nested))
