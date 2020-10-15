def sec_max_finder(n,arr):
    zes = max(arr)
    i=0
    while(i<n):
        if zes ==max(arr):
            arr.remove(max(arr))
        i+=1
    return max(arr)
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(sec_max_finder(n,arr))
