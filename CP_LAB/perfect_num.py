def checkPerfect(num: int) -> None:
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    if sum_div == num:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

X = int(input())
checkPerfect(X)
