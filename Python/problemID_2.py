# https://projecteuler.net/archives
# Problem 2 

def fibonacci():
    arr = [1,1]
    sum = 0
    n = 2

    while (sum < 4000000):
        arr.append(arr[n-1] + arr[n-2])
        if arr[n] % 2 == 0:
            sum += arr[n]      
        n += 1
    print(sum)


if __name__ == "__main__":
    fibonacci()