-- db tables creation --

CREATE TABLE goals (
    goalID INTEGER PRIMARY KEY AUTOINCREMENT,
    goalDescription TEXT NOT NULL,
    completed BOOL NOT NULL);

CREATE TABLE history (
    sessionID INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    time_minutes INTEGER NOT NULL,
    date TEXT NOT NULL DEFAULT (DATE('now'))
    );