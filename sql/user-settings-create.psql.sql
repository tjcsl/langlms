DROP TABLE IF EXISTS user_settings;

CREATE TABLE user_settings(
    sid serial,
    uid integer not null,
    key varchar(512) default "",
    value varchar(512) default""
);
