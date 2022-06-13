from flask import Flask, render_template, request, redirect
from flask import Blueprint
from datetime import *
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
    
    bookings = booking_repository.list_bookings_for_course(course.id)
    booked_members = []
    for row in bookings:
        member = member_repository.select(row["member_id"])
        booked_members.append(member)
        
    return render_template("bookings/show.html", booking=booking, member=member, course=course, booked_members=booked_members)

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
    
    if not member.premium:
        time = str(course.date)
        peak_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        if peak_time.hour > 17:
            apology = [
                f"{member.name} does not have a premium membership.",
                f"In order to book a peak-hour course {member.name} need to have premium membership." 
                ]
            return render_template("/bookings/apology.html", apology=apology)
    if course.capacity < 1:
        apology = [
            f"{course.title} is full.",
            f"You can increase the capacity by editing course or pick another course/slot with availability" 
            ]
        return render_template("/bookings/apology.html", apology=apology)
    
    booking_repository.save(new_booking)
    
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/delete/<id>")
def delete(id):
    booking_repository.delete(id)
    return redirect("/bookings")