# SDP-18: Student Learning Management System

The SDP-18 Student Learning Management System is a powerful web-based application crafted to streamline the management and delivery of educational content and resources to students. Serving as a centralized platform, it empowers educators to create, organize, and efficiently administer courses, while granting students access to a wealth of learning materials, assignments, and assessments. Our system is dedicated to fostering effective teaching and learning, facilitating collaboration, and ultimately elevating the overall educational experience for students.

Built using the Django framework, the system offers a suite of robust features tailored to cater to diverse educational needs:


## CONTRIBUTORS

- [Tadikonda Sai Manikanta](https://github.com/saitadikonda99)



# Project Directory Structure

```
Django-LMS/
├── ...
└── src/
    ├── client
    ├── CoreApp/            
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── manager.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── db.sqlite3
    └── manage.py

```

# Learning Management System (LMS) App Structure

In this Learning Management System (LMS) project, we've organized the functionality into separate apps to keep the codebase modular and maintainable. Each app focuses on specific aspects of the LMS. Below is an overview of the app structure:

## Core App

This app handles the basic functionalities and configurations of the LMS. It includes user authentication, registration, user profiles, and general site settings.

## Courses App

The Courses app manages all aspects related to courses. It includes creating, updating, and deleting courses. Additionally, it provides features for adding lessons, assignments, quizzes, and resources to courses.

## Enrollment App

The Enrollment app handles the process of enrolling students into courses. It includes views and models for managing enrollments, tracking progress, and recording completion status.

## Discussions App

The Discussions app provides a platform for students and instructors to discuss course-related topics. It includes features for creating discussion threads, posting replies, and categorizing discussions by course.

## Assignments App

The Assignments app manages the creation, submission, and grading of assignments. It supports instructors in setting assignment due dates, students in submitting solutions, and instructors in providing feedback.

## Quizzes App

The Quizzes app handles the creation and management of quizzes and assessments. It includes features for creating various types of questions, setting time limits, and calculating scores.

## Notifications App

The Notifications app manages sending notifications to users. This includes notifications about course updates, assignment due dates, new discussions, and more.

## User Progress App

The User Progress app tracks and displays user progress in courses. It showcases completed lessons, quizzes, assignments, and overall course completion percentage.

## Admin Dashboard App

The Admin Dashboard app is dedicated to administrators, providing features to manage users, courses, content, and analytics within the LMS.

## Static Pages App

The Static Pages app is responsible for managing static content such as the home page, about page, contact page, and other informational pages.

## Payments App

If the LMS offers paid courses, the Payments app handles payment processing, subscription management, and invoices.

Feel free to explore each app's directory to find more detailed information about its structure and functionality.

## Getting Started

To set up the LMS project, follow these steps:

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install project dependencies using `pip install -r requirements.txt`.
4. Configure the database settings in `settings.py`.
5. Run migrations using `python manage.py migrate`.
6. Create a superuser account using `python manage.py createsuperuser`.
7. Start the development server with `python manage.py runserver`.

Happy coding and building your own LMS!




## Features

- **Educator-Centric:** Empower educators to effortlessly design courses, arrange materials, and manage assignments within an intuitive interface.

- **Comprehensive Student Portal:** Grant students a unified space to enroll in courses, access study materials, and submit assignments seamlessly.

- **Enhanced Learning:** Foster interactive and effective teaching techniques by enabling collaborative learning experiences between educators and students.

- **Easy Integration:** Seamlessly integrate multimedia resources, ensuring diverse learning materials such as videos, documents, and quizzes can be presented.

- **Scalable and Customizable:** Designed with scalability in mind, the system's modular architecture allows for easy expansion and customization.

## Installation

Get started with the SDP-18 Student Learning Management System by following these simple steps:

1. . **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/SDP-18.git
2. Navigate to the project directory:
   ```sh
     cd Django-LMS
3. Create a virtual environment using Python 3:
   ```sh
     virtualenv -p python3 .
4. Activate the virtual environment:
   ```sh
     source ./bin/activate
5. Install Django within the virtual environment:
   ```sh
     python manage.py runserver
6. Navigate into the "src" folder:
   ```sh
     cd src
7. Start the development server:
   ```sh
     python manage.py runserver
## Usage

1. Register a new account as an educator or student.
2. Log in to access your personalized dashboard.
3. Educators can create captivating courses, curate materials, and effortlessly manage assignments.
4. Students can conveniently enroll in courses, gain access to learning resources, and submit assignments with ease.

## Contribution

We welcome contributions from the community! If you're interested in enhancing the SDP-18 project, follow these steps:

1. Fork this repository.
2. Create a dedicated branch for your feature or improvement.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork and create a pull request.
5. Our team will review your contribution, provide feedback, and merge it once ready.

Let's collaborate to create an exceptional learning management solution!

## License

This project operates under the [MIT License](LICENSE), allowing you to modify and distribute the software while retaining credit to the original authors.

---

Transforming education with technology – SDP-18 Student Learning Management System
