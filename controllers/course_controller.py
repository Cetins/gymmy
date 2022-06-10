from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.course import Course
import repositories.course_repository as course_repository

courses_blueprint = Blueprint("courses", __name__)

@courses_blueprint.route("/courses")
def courses():
    courses = course_repository.select_all()
    return render_template("courses/index.html", courses=courses)

@courses_blueprint.route("/courses/<id>")
def show(id):
    course = course_repository.select(id)
    return render_template("courses/show.html", course=course)

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