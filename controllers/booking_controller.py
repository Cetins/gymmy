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

@bookings_blueprint.route("/bookings/<id>")
def show(id):
    booking = booking_repository.select(id)
    member = member_repository.select(booking['member_id'])
    course = course_repository.select(booking['course_id'])
    return render_template("bookings/show.html", booking=booking, member=member, course=course)

@bookings_blueprint.route("/bookings/new")
def new():
    members = member_repository.select_all()
    courses = course_repository.select_all()
    return render_template("bookings/new.html", members=members, courses=courses)

@bookings_blueprint.route("/bookings", methods=["POST"])
def add_booking():
    member_id = request.form["member_id"]
    course_id = request.form["course_id"]
    member = member_repository.select(member_id)
    course = course_repository.select(course_id)
    new_booking = Booking(member, course)
    booking_repository.save(new_booking)
    
    return redirect("/bookings")