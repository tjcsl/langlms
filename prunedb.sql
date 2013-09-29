delete from class_roles where uid not in (select uid from users);
delete from classes where cid not in (select cid from class_roles);
