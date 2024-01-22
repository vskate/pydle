def bubble_sort_dicts(lst, key):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j][key] > lst[j+1][key]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst