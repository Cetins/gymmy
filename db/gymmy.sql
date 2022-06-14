DROP TABLE bookings;
DROP TABLE members;
DROP TABLE courses;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    email VARCHAR(255),
    premium BOOL,
    active BOOL
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    level VARCHAR(255),
    title VARCHAR(255),
    date TIMESTAMP,
    capacity INT,
    active BOOL
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    course_id INT REFERENCES courses(id) ON DELETE CASCADE
);