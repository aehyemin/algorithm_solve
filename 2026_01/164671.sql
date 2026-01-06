select concat("/home/grep/src/", f.board_id,"/", f.file_id, f.file_name, f.file_ext) as FILE_PATH
from used_goods_file as f
where f.board_id = (
    select board_id
    from used_goods_board
    order by views desc
    limit 1
)
order by f.file_id desc
