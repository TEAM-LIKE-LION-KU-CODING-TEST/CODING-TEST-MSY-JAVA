def solution(record):
    answer = []
    message = ["님이 들어왔습니다.", "님이 나갔습니다."]
    # [메시지, uid], 메시지 0 : 들어왔습니다, 1 : 나갔습니다
    record_data = []
    uid_name = {}
    
    for r in record:
        input_r = list(r.split(" "))
        if input_r[0] == "Enter":
            record_data.append([0, input_r[1]])
            uid_name[input_r[1]] = input_r[2]
        if input_r[0] == "Leave":
            record_data.append([1, input_r[1]])
        if input_r[0] == "Change":
            uid_name[input_r[1]] = input_r[2]
    
    for rd in record_data:
        answer.append("" + uid_name[rd[1]] + message[rd[0]])
    
    return answer