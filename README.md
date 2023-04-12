# GYMMY

## CRM Web Application with Python Flask

<img width="500" alt="Screenshot 2022-06-16 at 01 04 30" src="https://user-images.githubusercontent.com/69481095/173961978-edfb821f-f7c1-40dd-8d35-52c8099531d8.png">

## About

Gymmy is a booking tracking app specifically designed for gyms. You can store and manage your members, courses and bookings in one place

## Features

* Create, edit members
* Create, edit courses
* Create, cancel bookings

<img width="500" alt="Screenshot 2022-06-16 at 01 08 13" src="https://user-images.githubusercontent.com/69481095/173962294-2ac43f55-ee96-467e-ad42-d66ab6ba21a0.png">

# Members

The members page displays all saved members in card view. You can also click on the member name for more detailed view. 

### Activate/Deactivate Member

You can deactivate your members. This will help you suspend their membership without losing their data. You can still see all the members regardless in the members page but when making a booking you can only see active members under the selections.

### Premium Membership

There are two types of memberships in Gymmy, premium and standard. You can book all courses for premium members while standard members can only access off-peak hour courses. If you try to book a standard member to a peak hour course system will display an apology page.

<img width="500" alt="Screenshot 2022-06-16 at 01 16 48" src="https://user-images.githubusercontent.com/69481095/173962985-958d39d6-bf69-451f-921b-142605d265f9.png">

# Courses

The courses page displays all saved courses. You can click on the course title to see a detailed view. In details you can see the list of members who booked that course, or an informative message of you don't have any bookings in that course.

### Activate/Deactivate Course

Just like members, you can deactivate your courses. You can still see all courses but only book active ones. To activate the course simply go to course page and change the active status back again.

<img width="500" alt="Screenshot 2022-06-16 at 01 26 21" src="https://user-images.githubusercontent.com/69481095/173963927-2a28b585-0b42-4771-9596-c7c095a79411.png">

# Bookings

All the bookings will be displayed in bookings page as a table. In order to see more details simply click on the member name. You will see the details of the booking and a delete button. You can delete the booking with one click.

Also you can click on the course title in the bookings table and go to course's details page to see other members who booked that course. 

# Request Handling

Gymmy has two extensive feauture

* Course capacity tracking

Gymmy tracks the capacity you assign a course and when there isn't any available space system denies to complete your request and redirects you to an apology page.

<img width="300" alt="Screenshot 2022-06-16 at 01 30 27" src="https://user-images.githubusercontent.com/69481095/173964650-8efaa63d-3e58-40da-8d10-036fdf5212b2.png">

* Peak-hour distinction

To prevent crowds and fair usage Gyymy has to two types of membership, premium and standard. Also there is a pre-assigned peak hour, 6PM (18:00). You can not book a standard member to a course which starts after 6PM. When this happens system denies to complete your request and redirects you to an apology page.

<img width="300" alt="Screenshot 2022-06-16 at 01 30 46" src="https://user-images.githubusercontent.com/69481095/173965059-5f18aff1-30e3-4653-bacb-61818e69583e.png">

Every apology page has two parts. First part explains the why your request denied, and the second part explains how you can fix it.

## Pre-filled Forms

While editing your member or your course, all existing details came as pre-filled with your form. So if you need to edit only one detail you don't need to fill all the details all over again. 

<img width="300" alt="Screenshot 2022-06-16 at 01 42 50" src="https://user-images.githubusercontent.com/69481095/173965407-a8ee3995-6859-474c-aafa-bcb04a3b80be.png">

Make your changes and click update.

<img width="300" alt="Screenshot 2022-06-16 at 01 43 25" src="https://user-images.githubusercontent.com/69481095/173965473-d70582c3-cc4c-4341-8e5f-845d085f3a45.png">

# Easy Navigation

Most of the names and titles are linking nicely in order to create easy access and smooth navigation through pages. When you click on a course you can see all the members who booked that course and if you click any of the member names you can navigate through that members single page.

<img width="300" alt="Screenshot 2022-06-16 at 01 48 37" src="https://user-images.githubusercontent.com/69481095/173966224-1fd0a433-72cb-4554-98bc-3f8eec25029a.png">


# Developer Notes

To run this project in your machine:

* Clone the project with ```git clone <project_link>```
* Ensure you have installed:
    * Python / python.org
    * PostgreSQL /  postgresql.org
    * Flask ```pip install Flask ```
    * Psycopg2 ```pip install pycopg2 ```
* On terminal of the project main folder:
    * create database ```createdb gymmy```
    * add dummydata ```psql -d gymmy -f db/gymmy.sql```
    * run console ```python console.py```
    * to view your app on your localhost```flask --app app run``` then CTRL + click the link on the terminal.

Feel free the open issues in this repository :)
