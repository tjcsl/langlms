DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS user_settings;

CREATE TABLE users(
    uid serial,
    username varchar(512) not null,
    passwd_hash varchar(512) not null,
    acl int default 0
);

CREATE TABLE user_settings(
    sid serial,
    uid integer not null,
    key varchar(512) default "",
    value varchar(512) default ""
);
