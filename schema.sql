CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_number INTEGER UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_number INTEGER,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL CHECK (grade >= 0 AND grade <= 100),
    FOREIGN KEY (roll_number) REFERENCES students(roll_number)
);
