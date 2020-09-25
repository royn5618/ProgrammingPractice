## Solution 1
## Link to Challenge - https://app.codility.com/programmers/custom_challenge/palladium2020/
## Link to my performance - https://app.codility.com/cert/view/certYKS4R6-HGWTTU3HGXM4KFJ9/

def solution(H):
    # write your code in Python 3.6
    max_width = len(H)
    try: 
        if len(H) == 1:
            return H[0]
        elif len(H) > 1:
            prob_area_list = []
            for i in range(1, max_width):
                area = (max(H[:i]) * len(H[:i])) + (max(H[i:]) * len(H[i:]))
                prob_area_list.append(area)
            return min(prob_area_list)
    except Exception as e:
        print(e)
        return None
