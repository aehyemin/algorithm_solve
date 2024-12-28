def solution(id_list, report, k):
    #동일 유저 신고는 1번으로 처리, 다른유저 계속 신고가능, K번이상 정지와 메일발송
    #dict 사용?
    id = { id:0 for id in id_list} #메일 몇번 받는지
    report_cnt = {id: set() for id in id_list} #신고한 목록
    for j in report:
        ToReport, reported = j.split() #신고자, 신고당한사람
        report_cnt[reported].add(ToReport) #reported 가 key , reporter 가 value
        
    for reported in report_cnt:
        if len(report_cnt[reported]) >= k:
            for reporter in report_cnt[reported]:
                id[reporter] += 1
    
    answer = list(id.values())
    return answer


