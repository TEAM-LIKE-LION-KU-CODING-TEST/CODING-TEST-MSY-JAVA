def solution(participant, completion):
    dictionary = {}
    
    for i in participant:
        # i가 처음 등장하면 0 + 1 = 1이 저장되고, 
        # 이미 있으면 기존 값 + 1 이 저장
        dictionary[i] = dictionary.get(i, 0) + 1
        
        # O(1)로 확인 가능
        # if i not in dictionary:
        #     dictionary[i] = 1
        # else :
        #     dictionary[i] += 1
    
    for i in completion:
        dictionary[i] -= 1
        
    for i in dictionary.keys():
        if dictionary[i] != 0:
            answer = i
            break
    
    return answer