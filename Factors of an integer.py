Factor = [0] * 50
ind = 2
cnt = 1
Factor[0] = 1  
N = int(input("Enter a number :  "))
while ind <= N:
    if N % ind == 0:
        Factor[cnt] = ind
        cnt += 1
    ind += 1
print("Factors of", N, "are:")
for ind in range(cnt):
    print(Factor[ind])
