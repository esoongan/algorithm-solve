def solution(n, times):
    times = sorted(times)
    end = times[-1] * (n//2)
    start = 0

    while start <= end:
        count = 0
        mid = (start + end) // 2

        for i in times:
            count += mid // i

        if count < n:
            start = mid+1
        else:
            result = mid
            end = mid-1
    print(result)
    return result


solution(6, [7,10])