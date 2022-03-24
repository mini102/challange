def solution(numbers):
    answer = []
    for num in numbers:
        diff = 0
        tmp = num+1 
        while True:
            bin1 = bin(tmp) 
            bin2 = bin(num)
            res = num ^ tmp
            diff = bin(res).count('1') 
            if diff<=2:
                break
            tmp+=1
        answer.append(tmp)
        
    return answer
