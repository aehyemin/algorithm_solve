select i.ITEM_ID, i.ITEM_NAME
from item_info as i
join item_tree as t
on t.item_id = i.item_id
where parent_item_id is null
