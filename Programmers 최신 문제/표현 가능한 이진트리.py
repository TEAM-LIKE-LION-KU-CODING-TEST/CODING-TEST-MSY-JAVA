def solution(numbers):
    answer = []
    
    # 중위순회 방식
    def in_order(st, ed, binary):
        if st >= ed:
            return True
        
        # 부모 노드 위치인 mid
        mid = (st + ed) // 2
        parent = binary[mid]
        
        left = binary[(st + (mid - 1)) // 2]
        right = binary[((mid + 1) + ed) // 2]
        
        # 루트 노드가 더미 노드이면 자식 노드도 더미 노드여야 한다
        if parent == 0 and (left == 1 or right == 1):
            return False
        
        # 왼쪽, 오른쪽 서브트리 순회
        if in_order(st, mid - 1, binary) and in_order(mid + 1, ed, binary):
            return True
        return False
    
    for n in numbers:
        num = n
        binary = []
        if num == 0:
            binary = [0]
        else:
            while num > 0:
                binary.append(num % 2)
                num = num // 2
            binary.reverse()
        
        # 포화이 이진트리 만들기
        target = 1
        while target < len(binary):
            target = target * 2 + 1
        binary = [0] * (target - len(binary)) + binary
        
        # 0부터 시작하는 리스트의 최상단 부모 노드는 len(binary) // 2
        if in_order(0, len(binary) - 1, binary):
            answer.append(1)
            continue
        answer.append(0)
        
    return answer