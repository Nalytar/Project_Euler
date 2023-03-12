# https://projecteuler.net/archives
# Problem 1

def multiples():
    sum = 0
    for n in range(1,1000):
        if(n % 3 == 0 or n % 5 == 0):
            sum += n
    print(sum)
    
if __name__ == "__main__":
    multiples()