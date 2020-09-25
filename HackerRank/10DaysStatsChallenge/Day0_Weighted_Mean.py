# Problem Link - 

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input().strip())
NUMBERS = [int(i) for i in input().strip().split(' ')]
WEIGHTS = [int(i) for i in input().strip().split(' ')]

def calculate_weighted_mean(n, numbers, weights):
    product_num_weight = []
    for num, weight in zip(numbers, weights):
        product_num_weight.append(num * weight)
    return sum(product_num_weight)/sum(weights)

print('{0:.1f}'.format(calculate_weighted_mean(N, NUMBERS, WEIGHTS)))
