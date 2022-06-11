from db.run_sql import run_sql

from models.booking import Booking
from models.member import Member
from models.course import Course

def save(booking):
    sql = "INSERT INTO bookings (member_id, course_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.course.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id

def select_all():
    sql = "SELECT * FROM bookings"
    bookings = run_sql(sql)
    return bookings

def list_bookings_for_course(course_id):
    sql = "SELECT * FROM bookings WHERE course_id=%s"
    values = [course_id]
    bookings = run_sql(sql, values)
    return bookings

def select(id):
    sql = "SELECT * FROM bookings WHERE id=%s"
    values = [id]
    booking = run_sql(sql, values)[0]
    return booking

def update(booking):
    sql = "UPDATE bookings SET member_id=%s, course_id=%s WHERE id=%s"
    values = [booking.member_id, booking.course_id]
    run_sql(sql, values)
    
def delete(id):
    sql = "DELETE FROM bookings WHERE id=%s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)
    