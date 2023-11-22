import math

def calculate_time(intime, outtime):
    inhour, inminute = map(int, intime.split(':'))
    outhour, outminute = map(int, outtime.split(':'))

    diffminute = outminute - inminute
    if diffminute < 0:
        outhour -= 1
        diffminute += 60
    diffhour = outhour - inhour

    return diffhour * 60 + diffminute


def solution(fees, records):
    answer = []
    # fees[0]분까지 fees[1]원, 이후 fees[2]분마다 fees[3]원 추가
    records_by_car = {}
    for record in records:
        time, number, what = record.split(' ')
        try:
            records_by_car[number].append(time)
        except:
            records_by_car[number] = [time]

    ans = []
    for number, time in records_by_car.items():
        difftime = 0
        while len(time) >= 2:
            intime = time.pop(0)
            outtime = time.pop(0)
            difftime += calculate_time(intime, outtime)
        if time:
            difftime += calculate_time(time[0], '23:59')
        # 비용 계산
        if difftime<=fees[0]:
            cost=fees[1]
        else:
            cost = fees[1] + math.ceil((difftime - fees[0]) / fees[2]) * fees[3]
        ans.append([number, cost])

    ans.sort()
    answer = [x[1] for x in ans]
    return answer

fees=list(map(int, input().split(' ')))
records=[input().strip() for _ in range(9)]

solution(fees, records)
