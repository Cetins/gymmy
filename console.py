import pdb
import datetime
from controllers.booking_controller import bookings
from models.booking import Booking
from models.member import Member
from models.course import Course
import repositories.member_repository as member_repository
import repositories.course_repository as course_repository
import repositories.booking_repository as booking_repository

member_1 = Member("Charlie", False, True)
member_repository.save(member_1)

member_2 = Member("Sushi", True, True)
member_repository.save(member_2)

member_3 = Member("Olive", False, False)
member_repository.save(member_3)


course_1 = Course("Spin Class", datetime.datetime(2022, 7, 17, 18, 30, 0), 15, True)
course_repository.save(course_1)

course_2 = Course("Morning Yoga", datetime.datetime(2022, 7, 20, 6, 0, 0), 10, True)
course_repository.save(course_2)

course_3 = Course("Kick Box", datetime.datetime(2022, 8, 7, 15, 00, 0), 5, True)
course_repository.save(course_3)

booking_1 = Booking(member_2, course_3)
booking_2 = Booking(member_1, course_2)

booking_repository.save(booking_1)
booking_repository.save(booking_2)


pdb.set_trace()