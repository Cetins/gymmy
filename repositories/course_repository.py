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

def select(id):
    sql = "SELECT * FROM courses WHERE id=%s"
    values = [id]
    result = run_sql(sql,values)[0]
    course = Course(result["title"], result["date"], result["capacity"], result["active"], result["id"])
    return course

def update(course):
    sql = "UPDATE courses SET title=%s, date=%s, capacity=%s, active=%s WHERE id=%s"
    values = [course.title, course.date, course.capacity, course.active, course.id]
    run_sql(sql, values)  
    
def delete(id):
    sql = "DELETE FROM courses WHERE id=%s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE FROM courses"
    run_sql(sql)
