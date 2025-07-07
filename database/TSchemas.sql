-- Used to create the tables in database (In supabase-SQL Editor)
-- students table
CREATE TABLE students (
    register_number VARCHAR(20) PRIMARY KEY,
    name TEXT NOT NULL
);

-- subjects table
CREATE TABLE subjects (
    subject_code VARCHAR(10) PRIMARY KEY,
    subject_name TEXT NOT NULL,
    semester INTEGER NOT NULL CHECK (semester >= 1 AND semester <= 8)
);

-- exams table
CREATE TABLE exams (
    exam_id SERIAL PRIMARY KEY,
    semester INTEGER NOT NULL CHECK (semester >= 1 AND semester <= 8),
    exam_type VARCHAR(10) NOT NULL CHECK (exam_type IN ('Internal 1', 'Internal 2', 'Model')),
    exam_date DATE
);

-- marks table
CREATE TABLE marks (
    id SERIAL PRIMARY KEY,
    register_number VARCHAR(20) REFERENCES students(register_number),
    subject_code VARCHAR(10) REFERENCES subjects(subject_code),
    exam_id INTEGER REFERENCES exams(exam_id),
    mark INTEGER CHECK (mark >= 0 AND mark <= 100),
    UNIQUE (register_number, subject_code, exam_id)
);
