def find_pairs(lst, target):
    pairs = []
    seen = set()

    for num in lst:
        complement = target - num
        pair = (min(num, complement), max(num, complement))

        # Check if complement exists and pair not seen already
        if complement in lst and pair not in seen:
            pairs.append((num, complement))
            seen.add(pair)

    return pairs


# Example input
numbers = [2, 4, 3, 5, 7, 8, -1]
target = 6

result = find_pairs(numbers, target)
print(result)
