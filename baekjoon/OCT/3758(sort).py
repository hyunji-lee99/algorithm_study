import sys

t=int(sys.stdin.readline())
for _ in range(t):
    n,k,t,m=map(int, sys.stdin.readline().split(' '))
    # n개의 팀에 대한 정보 배열
    # 총 점수, 제출횟수, 제출시간, 문제번호별 점수
    team_info=[[0,0,0,[0]*(k),t_id] for t_id in range(n)]
    for time in range(m):
        team, pnum, score = map(int, sys.stdin.readline().split(' '))
        # 제출 횟수, 제출 시간 갱신
        team_info[team - 1][1] += 1
        team_info[team-1][2] = time
        # 해당 문제의 현재 점수보다 새로운 점수가 더 높다면, 점수 갱신
        if team_info[team-1][3][pnum-1]<score:
            team_info[team-1][0]-=team_info[team-1][3][pnum-1]
            team_info[team-1][0]+=score
            team_info[team-1][3][pnum-1]=score

    team_info.sort(key=lambda x:(-x[0], x[1], x[2]))
    for rank in range(n):
        if team_info[rank][4]==t-1:
            print(rank+1)
            break
    # 직접 구현
    # mscore,mnum,mtime,mpros =team_info[t-1]
    # ans=1
    # for idx in range(n):
    #     if idx==t-1:
    #         continue
    #     ts, tm, tt, tp=team_info[idx]
    #     # 우리팀 점수보다 높은 점수일 경우
    #     if ts>mscore:
    #         ans+=1
    #     # 우리팀 점수와 동일하다면, 제출 횟수가 더 적은지 확인
    #     elif ts==mscore:
    #         if tm<mnum:
    #             ans+=1
    #         elif tm==mnum:
    #             # 제출 횟수가 동일하다면, 최종 제출 시간이 더 빠른지 확인
    #             if tt<mtime:
    #                 ans+=1
    # print(ans)
