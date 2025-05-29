# def digital_root(n):
#     n=str(n)
#     sum=0
#     for i in n:
#         sum+=int(i)
#         if len(str(sum))>1:
#             sum=int(str(sum)[0]) + int(str(sum)[-1])
#     return sum


# def solution(full_text: str, search_text: str) -> int:
#     count = 0
#     start = 0
#     while True:
#         pos = full_text.find(search_text, start)
#         if pos == -1:
#             break
#         count += 1
#         start = pos + len(search_text)
#     return count

# ver gavige



# def replace_vowel_codes(arr):
#     vowels = {97: 'a', 101: 'e', 105: 'i', 111: 'o', 117: 'u'}
#     for i in range(len(arr)):
#         if arr[i] in vowels:
#             arr[i] = vowels[arr[i]]
#     return arr


# def most_frequent_count(arr):
#     if not arr:
#         return 0
#     counts = []
#     for num in arr:
#         counts[num] = counts.get(num, 0) + 1
#     return max(counts.values())


def delete_nth(lst, n):
    counts = {}
    result = []
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] <= n:
            result.append(num)
    return result
