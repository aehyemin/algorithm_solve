#parent_item_id에 없는 item_id -> 업그레이드불가능한 아이템
select ITEM_ID,	ITEM_NAME,	RARITY
from item_info
where item_id not in ( #[0, 1, null]
    select parent_item_id
    from item_tree
    where parent_item_id is not null 
)
order by item_id desc
