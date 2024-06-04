from pymongo import MongoClient
from datetime import datetime
from collections import defaultdict

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["university"]

# Коллекции
students_collection = db["students"]
groups_collection = db["groups"]
courses_collection = db["courses"]
grades_collection = db["grades"]


# Вывести списки групп каждому предмету с указанием преподавателя
def get_groups_by_course():
    courses = courses_collection.find()
    for course in courses:
        print(
            f"Предмет: {course['course_name']}, Преподаватель: {course['instructor']}"
        )
        groups = groups_collection.find({"course_ids": course["_id"]})
        for group in groups:
            print(f"Группа: {group['group_name']}")


# Определить, какую дисциплину изучает максимальное количество студентов
def get_most_popular_course():
    pipeline = [
        {"$unwind": "$course_ids"},
        {"$group": {"_id": "$course_ids", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 1},
    ]
    result = groups_collection.aggregate(pipeline)
    for item in result:
        course = courses_collection.find_one({"_id": item["_id"]})
        print(
            f"Наибольшее количество студентов изучает предмет: {course['course_name']} ({item['count']} студентов)"
        )


# Определить сколько студентов обучатся у каждого их преподавателей
def get_students_by_instructor():
    instructors = courses_collection.distinct("instructor")
    for instructor in instructors:
        pipeline = [
            {"$match": {"instructor": instructor}},
            {
                "$lookup": {
                    "from": "groups",
                    "localField": "_id",
                    "foreignField": "course_ids",
                    "as": "groups",
                }
            },
            {"$unwind": "$groups"},
            {
                "$lookup": {
                    "from": "students",
                    "localField": "groups._id",
                    "foreignField": "group_id",
                    "as": "students",
                }
            },
            {"$unwind": "$students"},
            {"$group": {"_id": "$instructor", "count": {"$sum": 1}}},
        ]
        result = courses_collection.aggregate(pipeline)
        for item in result:
            print(f"Преподаватель: {instructor}, Количество студентов: {item['count']}")


# Определить долю сдавших студентов по каждой дисциплине
def get_pass_rate_by_course():
    courses = courses_collection.find()
    for course in courses:
        total_students = grades_collection.count_documents({"course_id": course["_id"]})
        passed_students = grades_collection.count_documents(
            {"course_id": course["_id"], "grade": {"$gte": 3}}
        )
        pass_rate = passed_students / total_students if total_students else 0
        print(f"Предмет: {course['course_name']}, Доля сдавших: {pass_rate:.2%}")


# Определить среднюю оценку по предметам (для сдавших студентов)
def get_average_grade_by_course():
    courses = courses_collection.find()
    for course in courses:
        pipeline = [
            {"$match": {"course_id": course["_id"], "grade": {"$gte": 3}}},
            {"$group": {"_id": "$course_id", "average_grade": {"$avg": "$grade"}}},
        ]
        result = grades_collection.aggregate(pipeline)
        for item in result:
            print(
                f"Предмет: {course['course_name']}, Средняя оценка: {item['average_grade']:.2f}"
            )


# Определить группу с максимальной средней оценкой (включая не сдавших)
def get_group_with_highest_average_grade():
    groups = groups_collection.find()
    max_avg_grade = 0
    top_group = None
    for group in groups:
        pipeline = [
            {"$match": {"group_id": group["_id"]}},
            {"$group": {"_id": "$group_id", "average_grade": {"$avg": "$grade"}}},
        ]
        result = grades_collection.aggregate(pipeline)
        for item in result:
            if item["average_grade"] > max_avg_grade:
                max_avg_grade = item["average_grade"]
                top_group = group["group_name"]
    print(
        f"Группа с наивысшей средней оценкой: {top_group}, Средняя оценка: {max_avg_grade:.2f}"
    )


# Вывести студентов со всеми оценками отлично и не имеющих несданный экзамен
def get_excellent_students():
    students = students_collection.find()
    for student in students:
        grades = grades_collection.find({"student_id": student["_id"]})
        all_excellent = all(grade["grade"] == 5 for grade in grades)
        no_fails = all(grade["grade"] >= 3 for grade in grades)
        if all_excellent and no_fails:
            print(f"{student['full_name']}")


# Вывести кандидатов на отчисление (не сдан не менее двух предметов)
def get_candidates_for_expulsion():
    students = students_collection.find()
    for student in students:
        grades = grades_collection.find({"student_id": student["_id"]})
        fail_count = sum(1 for grade in grades if grade["grade"] < 3)
        if fail_count >= 2:
            print(f"{student['full_name']}")


# Примеры вызова функций
get_groups_by_course()
get_most_popular_course()
get_students_by_instructor()
get_pass_rate_by_course()
get_average_grade_by_course()
get_group_with_highest_average_grade()
get_excellent_students()
get_candidates_for_expulsion()
