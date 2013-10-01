DROP TABLE IF EXISTS assessments;
DROP TABLE IF EXISTS assessment_items;
DROP TABLE IF EXISTS assessment_responses;

CREATE TABLE assessment (
    aid INTEGER AUTOINCREMENT PRIMARY KEY,
    cid INTEGER NOT NULL,
    name STRING DEFAULT "Assessment"
);

CREATE TABLE assessment_items (
    itemid INTEGER AUTOINCREMENT PRIMARY KEY,
    aid INTEGER NOT NULL,
    qtype INTEGER DEFAULT 0,
    qtitle STRING DEFAULT "Question",
    mcanswer0 STRING DEFAULT "",
    mcanswer1 STRING DEFAULT "",
    mcanswer2 STRING DEFAULT "",
    mcanswer3 STRING DEFAULT "",
    mccorrect INTEGER DEFAULT 0
);

CREATE TABLE assessments_responses (
    rid INTEGER AUTOINCREMENT PRIMARY KEY,
    uid INTEGER NOT NULL,
    itemid INTEGER NOT NULL,
    mcanswer INTEGER DEFAULT 0,
    writinganswer STRING DEFAULT ""
);
