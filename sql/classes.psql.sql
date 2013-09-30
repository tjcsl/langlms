DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS class_roles;

CREATE TABLE classes(
    cid serial,
    name varchar(512) not null,
    school varchar(512) not null
);

CREATE TABLE class_roles(
    roleid serial,
    cid integer,
    uid integer,
    role integer 
);
