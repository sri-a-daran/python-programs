ind = 2
cnt = 1
N = int(input("Enter a number: "))
while ind <= N:
    if N % ind == 0:
        cnt += 1
    ind += 1
if cnt == 2:
    print("Prime Number")
else:
    print("Not a prime number")
