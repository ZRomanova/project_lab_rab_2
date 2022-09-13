A = [1, 2, 3, 12, 123, 1234, 16666]
N = A[6]

def point(pMin, pMax): 
    return (pMax - pMin) // 2

def halfdiv(a, n):
    pointMin = 0
    pointMax = len(a)
    pointN = point(pointMin, pointMax)
    while a[pointN] != n:
        if a[pointN] > n:
            pointMax, pointN = pointN, point(pointMin, pointN)
        else:
            pointMin, pointN = pointN, pointN + point(pointN, pointMax)
    return pointN

print(halfdiv(A, N))