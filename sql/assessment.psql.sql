DROP TABLE IF EXISTS assessments;
DROP TABLE IF EXISTS assessment_items;
DROP TABLE IF EXISTS assessment_responses;

CREATE TABLE assessment (
    aid serial,
    cid INTEGER NOT NULL,
    name VARCHAR(1024) DEFAULT "Assessment"
);

CREATE TABLE assessment_items (
    itemid serial,
    aid INTEGER NOT NULL,
    qtype INTEGER DEFAULT 0,
    qtitle VARCHAR(2048) DEFAULT "Question",
    mcanswer0 VARCHAR(512) DEFAULT "",
    mcanswer1 VARCHAR(512) DEFAULT "",
    mcanswer2 VARCHAR(512) DEFAULT "",
    mcanswer3 VARCHAR(512) DEFAULT "",
    mccorrect INTEGER DEFAULT 0
);

CREATE TABLE assessment_responses (
    rid serial,
    uid INTEGER NOT NULL,
    itemid INTEGER NOT NULL,
    mcanswer INTEGER DEFAULT 0,
    writinganswer VARCHAR(8192) DEFAULT ""
);
