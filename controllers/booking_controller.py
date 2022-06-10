from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.course_repository as course_repository
import repositories.member_repository as member_repository



bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    results = booking_repository.select_all()
    bookings = []
    
    for result in results:
        member = member_repository.select(result['member_id'])
        course = course_repository.select(result['course_id'])
        booking = Booking(member, course, result["id"])
        bookings.append(booking)
    
    return render_template("bookings/index.html", bookings=bookings)