def solution(fees, records):
    answer = []
    cars = {}
    for r in records:
        time, num, route = r.split(" ")
        h, m = map(int, time.split(":"))
        std_m = h * 60 + m
        if num not in cars:
            cars[num] = []
        cars[num].append([std_m, route])
    
    for k in sorted(cars.keys()):
        t_sum = 0
        st = []
        for r in cars[k]:
            if not st:
                st.append(r)
            else:
                t_sum += r[0] - st[0][0]
                st.pop()
        if st:
            t_sum += (23 * 60 + 59) - st[0][0]
        
        if t_sum <= fees[0]:
            answer.append(fees[1])
        else:
            unit = 0
            unit = (t_sum - fees[0]) // fees[2]
            if ((t_sum - fees[0]) % fees[2]) != 0:
                unit += 1
            answer.append(fees[1] + (unit * fees[3]))
    return answers