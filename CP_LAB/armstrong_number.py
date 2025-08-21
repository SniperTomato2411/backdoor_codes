def isArmstrong(num: int) -> bool:
    order = len(str(num))
    temp, res = num, 0
    while temp > 0:
        digit = temp % 10
        res += digit ** order
        temp //= 10
    return res == num

def allArmstrong(lower: int, upper: int) -> list[int]:
    res = []
    for i in range(lower, upper + 1):
        if isArmstrong(i):
            res.append(i)
    if len(res) == 0:
        res.append(-1)
    return res

lower = int(input())
upper = int(input())
print(*allArmstrong(lower, upper))
