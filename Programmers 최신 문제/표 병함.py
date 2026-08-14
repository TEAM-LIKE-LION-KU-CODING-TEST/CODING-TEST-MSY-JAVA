def return_not_empty(val1, val2):
    if val1 != "EMPTY":
        return val1
    return val2

def solution(commands):
    answer = []
    # cells[r][c] = [val, is_merged, merge_group_index]
    cells = [[["EMPTY", False, -1] for _ in range(51)] for _ in range(51)]
    merge_group = []
    
    for command in commands:
        c_list = command.split()
        
        if c_list[0] == "UPDATE":
            if len(c_list) == 4:
                r = int(c_list[1])
                c = int(c_list[2])
                val = c_list[3]
                if not cells[r][c][1]:
                    cells[r][c][0] = val
                else:
                    merge_group[cells[r][c][2]][0] = val
            elif len(c_list) == 3:
                val1 = c_list[1]
                val2 = c_list[2]
                for r in range(1, 51):
                    for c in range(1, 51):
                        if not cells[r][c][1]:
                            if cells[r][c][0] == val1:
                                cells[r][c][0] = val2
                for mg in merge_group:
                    if mg[0] == val1:
                        mg[0] = val2
                        
        elif c_list[0] == "MERGE":
            r1 = int(c_list[1])
            c1 = int(c_list[2])
            r2 = int(c_list[3])
            c2 = int(c_list[4])
            
            # 같은 위치인 경우 무시
            if r1 == r2 and c1 == c2:
                continue
            
            # 이미 같은 그룹에 속해있는 경우 무시
            if cells[r1][c1][1] and cells[r2][c2][1] and cells[r1][c1][2] == cells[r2][c2][2]:
                continue
                
            # 단일 셀 왼쪽 단일 셀 오른쪽
            if not cells[r1][c1][1] and not cells[r2][c2][1]:
                val = return_not_empty(cells[r1][c1][0], cells[r2][c2][0])
                mg_index = len(merge_group)
                merge_group.append([val, [[r1, c1], [r2, c2]]])
                cells[r1][c1] = ["EMPTY", True, mg_index]
                cells[r2][c2] = ["EMPTY", True, mg_index]
            # 단일 셀 왼쪽 머지 그룹 셀 오른쪽
            elif not cells[r1][c1][1] and cells[r2][c2][1]:
                mg_index = cells[r2][c2][2]
                merge_group[mg_index][0] = return_not_empty(cells[r1][c1][0], merge_group[mg_index][0])
                merge_group[mg_index][1].append([r1, c1])
                cells[r1][c1][1] = True
                cells[r1][c1][2] = mg_index
            # 머지 그룹 셀 왼쪽 단일 셀 오른쪽
            elif cells[r1][c1][1] and not cells[r2][c2][1]:
                mg_index = cells[r1][c1][2]
                merge_group[mg_index][0] = return_not_empty(merge_group[mg_index][0], cells[r2][c2][0])
                merge_group[mg_index][1].append([r2, c2])
                cells[r2][c2][1] = True
                cells[r2][c2][2] = mg_index
            # 머지 그룹 셀 왼쪽 머지 그룹 셀 오른쪽
            elif cells[r1][c1][1] and cells[r2][c2][1]:
                mg_index = cells[r1][c1][2]
                target_index = cells[r2][c2][2]
                merge_group[mg_index][0] = return_not_empty(merge_group[mg_index][0], merge_group[target_index][0])
                merge_group[mg_index][1].extend(merge_group[target_index][1])
                for tr, tc in merge_group[target_index][1]:
                    cells[tr][tc][2] = mg_index
                merge_group[target_index] = ["EMPTY", []]
                
        elif c_list[0] == "UNMERGE":
            r = int(c_list[1])
            c = int(c_list[2])
            
            if not cells[r][c][1]:
                continue
                
            mg_index = cells[r][c][2]
            prev_val = merge_group[mg_index][0]
            
            for tr, tc in merge_group[mg_index][1]:
                cells[tr][tc] = ["EMPTY", False, -1]
            merge_group[mg_index] = ["EMPTY", []]
            cells[r][c][0] = prev_val
            
        elif c_list[0] == "PRINT":
            r = int(c_list[1])
            c = int(c_list[2])
            # 머지되지 않은 셀인 경우
            if not cells[r][c][1]:
                answer.append(cells[r][c][0])
            # 머지된 셀인 경우
            else:
                answer.append(merge_group[cells[r][c][2]][0])
                
    return answer