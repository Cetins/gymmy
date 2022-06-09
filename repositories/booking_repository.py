from db.run_sql import run_sql

from models.booking import Booking
from models.member import Member
from models.course import Course

def save(member, course):
    sql = "INSERT INTO bookings (member_id, course_id) VALUES (%s, %s) RETURNING id"
    values = [member.id, course.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking = Booking(member.id, course.id, id)
    return booking