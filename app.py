from flask import Flask, render_template

from controllers.member_controller import members_blueprint
from controllers.course_controller import courses_blueprint
from controllers.booking_controller import bookings_blueprint
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.course_repository as course_repository

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(courses_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route("/")
def home():
    bookings = booking_repository.select_all()
    member_id = bookings[-1]['member_id']
    course_id = bookings[-1]['course_id']
    member = member_repository.select(member_id)
    course = course_repository.select(course_id)
    return render_template("index.html", member=member, course=course)

if __name__ == "__main__":
    app.run(debug=True)