delete from users where uid not in (select uid from class_roles) and acl!=2;
delete from class_roles where uid not in (select uid from users);
delete from classes where cid not in (select cid from class_roles);
delete from news_posts where cid not in (select cid from classes);
