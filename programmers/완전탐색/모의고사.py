def solution(answers):
    answer = []
    
    num_1 = [1, 2, 3, 4, 5]
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == num_1[i % len(num_1)]:
            correct[0] += 1
        if answers[i] == num_2[i % len(num_2)]:
            correct[1] += 1
        if answers[i] == num_3[i % len(num_3)]:
            correct[2] += 1
    
    max_score = max(correct)
    
    for idx, score in enumerate(correct):
        if score == max_score:
            answer.append(idx + 1)
    
    return answer