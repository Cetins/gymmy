DROP TABLE registrations;
DROP TABLE members;
DROP TABLE courses;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    premium BOOL,
    active BOOL
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    date TIMESTAMP,
    capacity INT,
    active BOOL
);

CREATE TABLE registrations (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    course_id INT REFERENCES courses(id) ON DELETE CASCADE
);