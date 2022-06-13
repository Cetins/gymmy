from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.course import Course
import repositories.course_repository as course_repository
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository

courses_blueprint = Blueprint("courses", __name__)

@courses_blueprint.route("/courses")
def courses():
    courses = course_repository.select_all()
    return render_template("courses/index.html", courses=courses)

@courses_blueprint.route("/courses/<id>")
def show(id):
    course = course_repository.select(id)
    bookings = booking_repository.list_bookings_for_course(course.id)
    booked_members = []
    for booking in bookings:
        member = member_repository.select(booking["member_id"])
        booked_members.append(member)
    return render_template("courses/show.html", course=course, booked_members=booked_members)

@courses_blueprint.route("/courses/new")
def new():
    return render_template("courses/new.html")

@courses_blueprint.route("/courses", methods=["POST"])
def add_course():
    title = request.form['title']
    date = request.form['date']
    capacity = request.form['capacity']
    active = request.form['active']
    new_course = Course(title, date, capacity, active)
    course_repository.save(new_course)
    
    return redirect("/courses")

@courses_blueprint.route("/courses/edit/<id>")
def edit_course(id):
    course = course_repository.select(id)
    return render_template("/courses/edit.html", course=course)
    
@courses_blueprint.route("/courses/<id>", methods=["POST"])
def update_course(id):
    title = request.form['title']
    date = request.form['date']
    capacity = request.form['capacity']
    active = request.form['active']
    updated_course = Course(title, date, capacity, active, id)
    course_repository.update(updated_course)
    
    return redirect("/courses")

@courses_blueprint.route("/courses/delete/<id>")
def delete(id):
    course_repository.delete(id)
    return redirect("/courses")