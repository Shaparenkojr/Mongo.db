from pymongo import MongoClient
from datetime import datetime

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["university"]

# Коллекции
students_collection = db["students"]
groups_collection = db["groups"]
directions_collection = db["directions"]


# Задание 1: Вывести списки групп по заданному направлению с указанием номера группы
def get_groups_by_direction(direction_name):
    direction = directions_collection.find_one({"name": direction_name})
    if direction:
        groups = groups_collection.find({"study_direction_id": direction["_id"]})
        for group in groups:
            print(f"Группа: {group['group_name']}")
            students = students_collection.find({"group_id": group["_id"]}).sort(
                "full_name", 1
            )
            for student in students:
                status = "бюджет" if student["budget"] else "внебюджет"
                print(f"{student['full_name']}, {status}")


# Задание 2: Вывести студентов с фамилией, начинающейся с первой буквы вашей фамилии
def get_students_by_initial(initial):
    students = students_collection.find({"full_name": {"$regex": f"^{initial}"}}).sort(
        "full_name", 1
    )
    for student in students:
        group = groups_collection.find_one({"_id": student["group_id"]})
        direction = directions_collection.find_one({"_id": group["study_direction_id"]})
        print(f"{student['full_name']}, {group['group_name']}, {direction['name']}")


# # Задание 3: Вывести список студентов для поздравления по месяцам
# def get_birthdays_by_month():
#     students = students_collection.find()
#     months = {
#         1: "января",
#         2: "февраля",
#         3: "марта",
#         4: "апреля",
#         5: "мая",
#         6: "июня",
#         7: "июля",
#         8: "августа",
#         9: "сентября",
#         10: "октября",
#         11: "ноября",
#         12: "декабря",
#     }
#     for student in students:
#         birth_date = datetime.strptime(student["birth_date"], "%Y-%m-%d")
#         month_name = months[birth_date.month]
#         print(
#             f"{student['full_name'].split()[0]} {student['full_name'].split()[1][0]}.{student['full_name'].split()[2][0]}., {birth_date.day} {month_name}, {group['group_name']}, {direction['name']}"
#         )


# Задание 4: Вывести студентов с указанием возраста в годах
def get_students_with_age():
    current_year = datetime.now().year
    students = students_collection.find()
    for student in students:
        birth_year = datetime.strptime(student["birth_date"], "%Y-%m-%d").year
        age = current_year - birth_year
        print(f"{student['full_name']}, {age} лет")


# Задание 5: Вывести студентов, у которых день рождения в текущем месяце
def get_birthdays_current_month():
    current_month = datetime.now().month
    students = students_collection.find()
    for student in students:
        birth_month = datetime.strptime(student["birth_date"], "%Y-%m-%d").month
        if birth_month == current_month:
            print(f"{student['full_name']}")


# Задание 6: Вывести количество студентов по каждому направлению
def get_student_count_by_direction():
    directions = directions_collection.find()
    for direction in directions:
        groups = groups_collection.find({"study_direction_id": direction["_id"]})
        total_students = 0
        for group in groups:
            total_students += students_collection.count_documents(
                {"group_id": group["_id"]}
            )
        print(f"{direction['name']}: {total_students} студентов")


# Задание 7: Вывести количество бюджетных и внебюджетных мест по группам
def get_budget_and_non_budget_by_group():
    groups = groups_collection.find()
    for group in groups:
        budget_count = students_collection.count_documents(
            {"group_id": group["_id"], "budget": True}
        )
        non_budget_count = students_collection.count_documents(
            {"group_id": group["_id"], "budget": False}
        )
        direction = directions_collection.find_one({"_id": group["study_direction_id"]})
        print(
            f"Группа: {group['group_name']}, Направление: {direction['name']}, Бюджет: {budget_count}, Внебюджет: {non_budget_count}"
        )


# Примеры вызова функций
get_groups_by_direction("Информатика")
get_students_by_initial("Ш")
# get_birthdays_by_month()
get_students_with_age()
get_birthdays_current_month()
get_student_count_by_direction()
get_budget_and_non_budget_by_group()
