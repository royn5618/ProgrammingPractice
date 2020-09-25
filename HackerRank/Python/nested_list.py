# problem link - https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    all_input = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        all_input.append([name, score])
    # print(all_input)
    second_min_score = sorted(set([each_element[1] for each_element in all_input]))[1]
    names = [each_element[0] for each_element in all_input if each_element[1] == second_min_score]
    for each_name in sorted(names):
        print(each_name)
