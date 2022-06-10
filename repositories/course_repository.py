from controllers.course_controller import courses
from db.run_sql import run_sql

from models.course import Course

def save(course):
    sql = "INSERT INTO courses (title, date, capacity, active) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [course.title, course.date, course.capacity, course.active]
    results = run_sql(sql, values)
    course.id = results[0]['id']
    return course  

def select_all():
    sql = "SELECT * FROM courses"
    courses = run_sql(sql)
    return courses