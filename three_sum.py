def three_sum(arr):
    n = len(arr)
    left = i + 1
    right = n - 1
    for i in range(n):
        if arr[i] + arr[left] + arr[right] > 0:
            right -= 1
        elif arr[i] + arr[left] + arr[right] < 0:
            left += 1
        else:
            return [arr[i], arr[left], arr[right]]







arr = [-1, -2, 2, 3, 5, 8]
result = three_sum(arr)
print(result)

