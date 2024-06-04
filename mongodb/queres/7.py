from pymongo import MongoClient
from datetime import datetime

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["university"]

# Коллекции
students_collection = db["students"]
courses_collection = db["courses"]
attendance_collection = db["attendance"]
lessons_collection = db["lessons"]


# Вывести по заданному предмету количество посещенных занятий
def get_attended_classes_count(course_name):
    course = courses_collection.find_one({"course_name": course_name})
    if course:
        attended_count = attendance_collection.count_documents(
            {"course_id": course["_id"], "status": "attended"}
        )
        print(
            f"Количество посещенных занятий по предмету '{course_name}': {attended_count}"
        )


# Вывести по заданному предмету количество пропущенных занятий
def get_missed_classes_count(course_name):
    course = courses_collection.find_one({"course_name": course_name})
    if course:
        missed_count = attendance_collection.count_documents(
            {"course_id": course["_id"], "status": "missed"}
        )
        print(
            f"Количество пропущенных занятий по предмету '{course_name}': {missed_count}"
        )


# Вывести по заданному преподавателю количество студентов на каждом занятии
def get_students_count_by_instructor(instructor_name):
    lessons = lessons_collection.find({"instructor": instructor_name})
    for lesson in lessons:
        student_count = attendance_collection.count_documents(
            {"lesson_id": lesson["_id"], "status": "attended"}
        )
        print(
            f"Занятие по предмету '{lesson['course_name']}' (дата: {lesson['date']}): {student_count} студентов"
        )


# Для каждого студента вывести общее время, потраченное на изучение каждого предмета
def get_total_study_time_per_course():
    students = students_collection.find()
    for student in students:
        study_time = {}
        attendances = attendance_collection.find(
            {"student_id": student["_id"], "status": "attended"}
        )
        for attendance in attendances:
            lesson = lessons_collection.find_one({"_id": attendance["lesson_id"]})
            course_name = lesson["course_name"]
            lesson_duration = (
                datetime.strptime(lesson["end_time"], "%H:%M")
                - datetime.strptime(lesson["start_time"], "%H:%M")
            ).total_seconds() / 3600
            if course_name not in study_time:
                study_time[course_name] = 0
            study_time[course_name] += lesson_duration
        for course, time in study_time.items():
            print(
                f"Студент {student['full_name']} потратил {time:.2f} часов на изучение предмета '{course}'"
            )


# Примеры вызова функций
get_attended_classes_count("Математика")
get_missed_classes_count("Математика")
get_students_count_by_instructor("Иванов И.И.")
get_total_study_time_per_course()
