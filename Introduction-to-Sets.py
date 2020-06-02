def average(array):
    array1 = set(array)
    return sum(array1)/len(array1)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
