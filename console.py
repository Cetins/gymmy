import pdb
import datetime
from controllers.bookings_controller import bookings
from models.booking import Booking
from models.member import Member
from models.course import Course
import repositories.member_repository as member_repository
import repositories.course_repository as course_repository
import repositories.booking_repository as booking_repository

member_1 = Member("Leonard Hofstadter", 34, "leonard@mail.com", False, True)
member_repository.save(member_1)
member_2 = Member("Sheldon Cooper", 25, "sheldor@mail.com", True, True)
member_repository.save(member_2)
member_3 = Member("Penny Hofstadter", 21, "penny@mail.com", False, True)
member_repository.save(member_3)
member_4 = Member("Howard Wolowitz", 39, "howard@mail.com", False, True)
member_repository.save(member_4)
member_5 = Member("Raj Koothrappali", 42, "raj@mail.com", True, False)
member_repository.save(member_5)
member_6 = Member("Amy Farrah Fowler", 32, "amy@mail.com", True, True)
member_repository.save(member_6)
member_7 = Member("Bernadette Wolowitz", 32, "bernadette@mail.com", True, True)
member_repository.save(member_7)
member_8 = Member("Stuart Bloom", 51, "stuart@mail.com", False, False)
member_repository.save(member_8)
member_9 = Member("Wil Wheaton", 43, "wil@mail.com", False, True)
member_repository.save(member_9)


course_1 = Course("Spin Class", "Intermediate", datetime.datetime(2022, 7, 17, 18, 30, 0), 15, True)
course_repository.save(course_1)
course_2 = Course("Morning Yoga", "Beginner", datetime.datetime(2022, 12, 20, 6, 0, 0), 10, True)
course_repository.save(course_2)
course_3 = Course("Kick Box", "Advanced", datetime.datetime(2022, 8, 5, 15, 00, 0), 5, True)
course_repository.save(course_3)
course_4 = Course("Cardio", "Advanced", datetime.datetime(2022, 8, 7, 14, 30, 0), 5, True)
course_repository.save(course_4)
course_5 = Course("Intense Core", "Advanced", datetime.datetime(2022, 7, 5, 15, 00, 0), 5, True)
course_repository.save(course_5)
course_6 = Course("Cardio WW", "Advanced", datetime.datetime(2022, 9, 9, 18, 30, 0), 5, True)
course_repository.save(course_6)
course_7 = Course("Zumba", "Intermediate", datetime.datetime(2022, 8, 22, 18, 00, 0), 5, True)
course_repository.save(course_7)
course_8 = Course("Pilates", "Beginner", datetime.datetime(2022, 7, 15, 9, 00, 0), 5, True)
course_repository.save(course_8)
course_9 = Course("Xcore Beginner", "Beginner", datetime.datetime(2022, 8, 21, 15, 00, 0), 5, True)
course_repository.save(course_9)

booking_1 = Booking(member_1, course_2)
booking_2 = Booking(member_1, course_4)

booking_repository.save(booking_1)
booking_repository.save(booking_2)

pdb.set_trace()