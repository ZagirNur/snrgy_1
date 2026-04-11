def solve(arr):
    imax = 0
    imin = 0
    for i in range(len(arr)):
        if arr[i] > arr[imax]:
            imax = i
        if arr[i] < arr[imin]:
            imin = i
    if imax < imin:
        lo = imax + 1
        hi = imin
    else:
        lo = imin + 1
        hi = imax
    s = 0
    for i in range(lo, hi):
        if arr[i] < 0:
            s += arr[i]
    return s


a = list(map(int, input("Введите массив через пробел: ").split()))
print("Массив:", a)
print("Сумма отрицательных между max и min:", solve(a))
