DROP TABLE IF EXISTS news_posts;

CREATE TABLE news_posts(
    postid serial,
    cid integer,
    title varchar(512) not null,
    content varchar(4096) not null
);
