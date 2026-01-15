#2022-04-13 취소되지 않은 흉부외과 진료내역
#진료예약번호 a.apnt_no, 환자이름 p.pt_name, 환자번호 a.pt_no,
# 진료과코드a.mcdp_cd, 의사이름 d.dr_name, 진료예약일시 a.apnt_ymd 출력출력
#patient 환자 정보 p
#doctor 의사정보 d
#appointment 진료예약목록 a
#mddr_id 의사id a.mddr_id = d.dr_id, p.pt_no=a.pt_no

select a.APNT_NO, p.PT_NAME, a.PT_NO, a.MCDP_CD, d.DR_NAME, a.APNT_YMD
from appointment as a
join doctor as d
on a.mddr_id = d.dr_id
join patient as p
on p.pt_no = a.pt_no
where a.mcdp_cd = 'CS' and a.apnt_cncl_yn = 'N' and date(a.apnt_ymd) = '2022-04-13'
order by a.apnt_ymd
[출처] [프로그래머스] 취소되지 않은 진료 예약 조회하기|작성자 aehyemin
