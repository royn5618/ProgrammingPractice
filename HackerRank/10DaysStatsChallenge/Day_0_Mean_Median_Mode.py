# Problem Link - https://www.hackerrank.com/challenges/s10-basic-statistics/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read length of numbers
N = int(input())
# print(N)

# Read numbers
arr = [int(i) for i in input().strip().split(' ')]

def get_mean(N, arr):
    return sum(arr)/N

def get_median(N, arr):
    sorted_arr = sorted(arr)
    # print(sorted_array)
    if N%2 == 1:
        # Floor division plus 1
        return sorted_arr[(N//2)]
    else:
        # Floor division and plus 1 divided by 2
        return (sorted_arr[N//2] + sorted_arr[(N//2) - 1]) / 2

def get_mode(arr):
    sorted_arr = sorted(arr)
    dict_count = {}
    for each_num in arr:
        if each_num not in dict_count.keys():
            dict_count[each_num] = arr.count(each_num)
    if max(list(dict_count.values())) > 1:
        return min([k for k,v in dict_count.items() if v == max(list(dict_count.values()))])
    else:
        return min(arr)

print('{0:.1f}'.format(get_mean(N, arr)))
print('{0:.1f}'.format(get_median(N, arr)))
print(get_mode(arr))
