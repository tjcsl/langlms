DROP TABLE IF EXISTS assessments;
DROP TABLE IF EXISTS assessment_items;
DROP TABLE IF EXISTS assessment_responses;

CREATE TABLE assessment (
    aid INTEGER PRIMARY KEY AUTOINCREMENT,
    cid INTEGER NOT NULL,
    name STRING DEFAULT "Assessment"
);

CREATE TABLE assessment_items (
    itemid INTEGER PRIMARY KEY AUTOINCREMENT,
    aid INTEGER NOT NULL,
    qtype INTEGER DEFAULT 0,
    qtitle STRING DEFAULT "Question",
    mcanswer0 STRING DEFAULT "",
    mcanswer1 STRING DEFAULT "",
    mcanswer2 STRING DEFAULT "",
    mcanswer3 STRING DEFAULT "",
    mccorrect INTEGER DEFAULT 0
);

CREATE TABLE assessment_responses (
    rid INTEGER PRIMARY KEY AUTOINCREMENT,
    uid INTEGER NOT NULL,
    itemid INTEGER NOT NULL,
    mcanswer INTEGER DEFAULT 0,
    writinganswer STRING DEFAULT ""
);
