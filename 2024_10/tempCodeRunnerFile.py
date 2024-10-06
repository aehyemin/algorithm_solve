    sosu.append(i)
        N = N / i
        for i in range(i, N):
            if N % i == 0:
                N = N / i
        
print(sosu)