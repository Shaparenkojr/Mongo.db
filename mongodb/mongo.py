from pymongo import MongoClient
from bson.objectid import ObjectId

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Создание базы данных
db = client["university"]

# Создание коллекций
students_collection = db["students"]
groups_collection = db["groups"]
directions_collection = db["directions"]
teachers_collection = db["teachers"]
subjects_collection = db["subjects"]
grades_collection = db["grades"]
schedule_collection = db["schedule"]
attendance_collection = db["attendance"]

# Удаление старых данных (если нужно)
students_collection.delete_many({})
groups_collection.delete_many({})
directions_collection.delete_many({})
teachers_collection.delete_many({})
subjects_collection.delete_many({})
grades_collection.delete_many({})
schedule_collection.delete_many({})
attendance_collection.delete_many({})

# Направления обучения
directions = ["Информатика", "Математика", "Физика"]

# Преподаватели
teachers = [
    {"full_name": "Иванов Петр Сергеевич"},
    {"full_name": "Петрова Анна Васильевна"},
    {"full_name": "Сидоров Алексей Николаевич"},
    {"full_name": "Смирнова Мария Александровна"},
    {"full_name": "Кузнецов Виктор Владимирович"},
]

# Вставка преподавателей
teacher_ids = [
    teachers_collection.insert_one(teacher).inserted_id for teacher in teachers
]

# Предметы и соответствие преподавателям
subjects = [
    {"name": "Алгоритмы и структуры данных", "teacher_id": teacher_ids[0]},
    {"name": "Математический анализ", "teacher_id": teacher_ids[1]},
    {"name": "Физика", "teacher_id": teacher_ids[2]},
    {"name": "Программирование", "teacher_id": teacher_ids[0]},
    {"name": "Линейная алгебра", "teacher_id": teacher_ids[1]},
    {"name": "Теоретическая механика", "teacher_id": teacher_ids[3]},
    {"name": "Базы данных", "teacher_id": teacher_ids[4]},
]

# Вставка предметов
subject_ids = [
    subjects_collection.insert_one(subject).inserted_id for subject in subjects
]

# Времена пар
schedule = [
    {"pair_number": 1, "start_time": "08:00", "end_time": "09:30"},
    {"pair_number": 2, "start_time": "09:40", "end_time": "11:10"},
    {"pair_number": 3, "start_time": "11:20", "end_time": "12:50"},
    {"pair_number": 4, "start_time": "13:00", "end_time": "14:30"},
    {"pair_number": 5, "start_time": "14:40", "end_time": "16:10"},
    {"pair_number": 6, "start_time": "16:20", "end_time": "17:50"},
]

# Вставка расписания
schedule_ids = [schedule_collection.insert_one(s).inserted_id for s in schedule]

# Создание групп для направлений и вставка студентов
direction_groups = {
    "Информатика": ["Группа И-1", "Группа И-2", "Группа И-3"],
    "Математика": ["Группа М-1", "Группа М-2", "Группа М-3"],
    "Физика": ["Группа Ф-1", "Группа Ф-2", "Группа Ф-3"],
}

# Вставка направлений, групп и студентов
for direction, groups in direction_groups.items():
    direction_id = directions_collection.insert_one({"name": direction}).inserted_id
    for group_name in groups:
        group_id = groups_collection.insert_one(
            {"group_name": group_name, "study_direction_id": direction_id}
        ).inserted_id

        # Примеры студентов
students = [
    {
        "full_name": "Иван Иванов",
        "birth_date": "2001-01-01",
        "address": {"city": "Москва", "street": "Тверская улица", "house_number": "10"},
        "phones": ["+7-495-123-4567"],
        "email": "ivan.ivanov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Мария Смирнова",
        "birth_date": "2002-02-02",
        "address": {"city": "Москва", "street": "Арбат", "house_number": "15"},
        "phones": ["+7-495-234-5678"],
        "email": "maria.smirnova@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Алексей Петров",
        "birth_date": "2003-03-03",
        "address": {
            "city": "Москва",
            "street": "Ленинградский проспект",
            "house_number": "20",
        },
        "phones": ["+7-495-345-6789"],
        "email": "alexey.petrov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Елена Кузнецова",
        "birth_date": "2004-04-04",
        "address": {"city": "Москва", "street": "Проспект Мира", "house_number": "25"},
        "phones": ["+7-495-456-7890"],
        "email": "elena.kuznetsova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Дмитрий Соколов",
        "birth_date": "2005-05-05",
        "address": {
            "city": "Москва",
            "street": "Никольская улица",
            "house_number": "30",
        },
        "phones": ["+7-495-567-8901"],
        "email": "dmitry.sokolov@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Иван Иванов",
        "birth_date": "2001-01-01",
        "address": {"city": "Москва", "street": "Тверская улица", "house_number": "10"},
        "phones": ["+7-495-123-4567"],
        "email": "ivan.ivanov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Мария Смирнова",
        "birth_date": "2002-02-02",
        "address": {"city": "Москва", "street": "Арбат", "house_number": "15"},
        "phones": ["+7-495-234-5678"],
        "email": "maria.smirnova@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Алексей Петров",
        "birth_date": "2003-03-03",
        "address": {
            "city": "Москва",
            "street": "Ленинградский проспект",
            "house_number": "20",
        },
        "phones": ["+7-495-345-6789"],
        "email": "alexey.petrov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Елена Кузнецова",
        "birth_date": "2004-04-04",
        "address": {"city": "Москва", "street": "Проспект Мира", "house_number": "25"},
        "phones": ["+7-495-456-7890"],
        "email": "elena.kuznetsova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Дмитрий Соколов",
        "birth_date": "2005-05-05",
        "address": {
            "city": "Москва",
            "street": "Никольская улица",
            "house_number": "30",
        },
        "phones": ["+7-495-567-8901"],
        "email": "dmitry.sokolov@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Ольга Новикова",
        "birth_date": "2001-06-06",
        "address": {
            "city": "Санкт-Петербург",
            "street": "Невский проспект",
            "house_number": "35",
        },
        "phones": ["+7-812-123-4567"],
        "email": "olga.novikova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Андрей Морозов",
        "birth_date": "2002-07-07",
        "address": {"city": "Казань", "street": "Улица Баумана", "house_number": "40"},
        "phones": ["+7-843-234-5678"],
        "email": "andrey.morozov@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Анна Васильева",
        "birth_date": "2003-08-08",
        "address": {
            "city": "Новосибирск",
            "street": "Красный проспект",
            "house_number": "45",
        },
        "phones": ["+7-383-345-6789"],
        "email": "anna.vasileva@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Михаил Козлов",
        "birth_date": "2004-09-09",
        "address": {
            "city": "Екатеринбург",
            "street": "Ленина проспект",
            "house_number": "50",
        },
        "phones": ["+7-343-456-7890"],
        "email": "mikhail.kozlov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Татьяна Павлова",
        "birth_date": "2005-10-10",
        "address": {
            "city": "Нижний Новгород",
            "street": "Большая Покровская улица",
            "house_number": "55",
        },
        "phones": ["+7-831-567-8901"],
        "email": "tatiana.pavlova@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Иван Иванов",
        "birth_date": "2001-01-01",
        "address": {"city": "Москва", "street": "Тверская улица", "house_number": "10"},
        "phones": ["+7-495-123-4567"],
        "email": "ivan.ivanov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Мария Смирнова",
        "birth_date": "2002-02-02",
        "address": {"city": "Москва", "street": "Арбат", "house_number": "15"},
        "phones": ["+7-495-234-5678"],
        "email": "maria.smirnova@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Алексей Петров",
        "birth_date": "2003-03-03",
        "address": {
            "city": "Москва",
            "street": "Ленинградский проспект",
            "house_number": "20",
        },
        "phones": ["+7-495-345-6789"],
        "email": "alexey.petrov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Елена Кузнецова",
        "birth_date": "2004-04-04",
        "address": {"city": "Москва", "street": "Проспект Мира", "house_number": "25"},
        "phones": ["+7-495-456-7890"],
        "email": "elena.kuznetsova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Дмитрий Соколов",
        "birth_date": "2005-05-05",
        "address": {
            "city": "Москва",
            "street": "Никольская улица",
            "house_number": "30",
        },
        "phones": ["+7-495-567-8901"],
        "email": "dmitry.sokolov@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Ольга Новикова",
        "birth_date": "2001-06-06",
        "address": {
            "city": "Санкт-Петербург",
            "street": "Невский проспект",
            "house_number": "35",
        },
        "phones": ["+7-812-123-4567"],
        "email": "olga.novikova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Андрей Морозов",
        "birth_date": "2002-07-07",
        "address": {"city": "Казань", "street": "Улица Баумана", "house_number": "40"},
        "phones": ["+7-843-234-5678"],
        "email": "andrey.morozov@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Анна Васильева",
        "birth_date": "2003-08-08",
        "address": {
            "city": "Новосибирск",
            "street": "Красный проспект",
            "house_number": "45",
        },
        "phones": ["+7-383-345-6789"],
        "email": "anna.vasileva@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Михаил Козлов",
        "birth_date": "2004-09-09",
        "address": {
            "city": "Екатеринбург",
            "street": "Ленина проспект",
            "house_number": "50",
        },
        "phones": ["+7-343-456-7890"],
        "email": "mikhail.kozlov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Татьяна Павлова",
        "birth_date": "2005-10-10",
        "address": {
            "city": "Нижний Новгород",
            "street": "Большая Покровская улица",
            "house_number": "55",
        },
        "phones": ["+7-831-567-8901"],
        "email": "tatiana.pavlova@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Сергей Волков",
        "birth_date": "2001-11-11",
        "address": {"city": "Воронеж", "street": "Ленина улица", "house_number": "60"},
        "phones": ["+7-473-123-4567"],
        "email": "sergey.volkov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Наталья Белова",
        "birth_date": "2002-12-12",
        "address": {
            "city": "Ростов-на-Дону",
            "street": "Большая Садовая улица",
            "house_number": "65",
        },
        "phones": ["+7-863-234-5678"],
        "email": "natalia.belova@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Павел Романов",
        "birth_date": "2003-01-13",
        "address": {
            "city": "Самара",
            "street": "Московское шоссе",
            "house_number": "70",
        },
        "phones": ["+7-846-345-6789"],
        "email": "pavel.romanov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Ирина Сидорова",
        "birth_date": "2004-02-14",
        "address": {
            "city": "Челябинск",
            "street": "Кирова улица",
            "house_number": "75",
        },
        "phones": ["+7-351-456-7890"],
        "email": "irina.sidorova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Владимир Федоров",
        "birth_date": "2005-03-15",
        "address": {"city": "Омск", "street": "Ленина проспект", "house_number": "80"},
        "phones": ["+7-381-567-8901"],
        "email": "vladimir.fedorov@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Светлана Иванова",
        "birth_date": "2000-11-11",
        "address": {
            "city": "Ростов-на-Дону",
            "street": "Большая Садовая улица",
            "house_number": "60",
        },
        "phones": ["+7-863-678-9012"],
        "email": "svetlana.ivanova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Павел Смирнов",
        "birth_date": "2001-12-12",
        "address": {
            "city": "Волгоград",
            "street": "Профсоюзная улица",
            "house_number": "65",
        },
        "phones": ["+7-844-789-0123"],
        "email": "pavel.smirnov@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Евгений Петров",
        "birth_date": "2002-01-13",
        "address": {
            "city": "Уфа",
            "street": "Ленинградская улица",
            "house_number": "70",
        },
        "phones": ["+7-347-890-1234"],
        "email": "evgeny.petrov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Артем Беляев",
        "birth_date": "2000-03-15",
        "address": {
            "city": "Челябинск",
            "street": "Пролетарская улица",
            "house_number": "70",
        },
        "phones": ["+7-351-123-4567"],
        "email": "artem.belyaev@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Ксения Семенова",
        "birth_date": "2000-05-25",
        "address": {"city": "Омск", "street": "Мира проспект", "house_number": "80"},
        "phones": ["+7-381-234-5678"],
        "email": "ksenia.semenova@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Дарья Мельникова",
        "birth_date": "2001-07-10",
        "address": {
            "city": "Самара",
            "street": "Кировская улица",
            "house_number": "90",
        },
        "phones": ["+7-846-345-6789"],
        "email": "darya.melnikova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Елена Сергеева",
        "birth_date": "1998-05-15",
        "address": {
            "city": "Владивосток",
            "street": "Улица Светланская",
            "house_number": "123",
        },
        "phones": ["+7-902-123-4567"],
        "email": "elena.sergeeva@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Антонина Николаева",
        "birth_date": "1997-08-20",
        "address": {
            "city": "Краснодар",
            "street": "Улица Красная",
            "house_number": "456",
        },
        "phones": ["+7-918-234-5678"],
        "email": "antonina.nikolaeva@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Денис Волков",
        "birth_date": "2000-12-03",
        "address": {
            "city": "Тюмень",
            "street": "Улица Солнечная",
            "house_number": "789",
        },
        "phones": ["+7-345-345-6789"],
        "email": "denis.volkov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Ольга Павлова",
        "birth_date": "1999-04-25",
        "address": {"city": "Сочи", "street": "Улица Морская", "house_number": "111"},
        "phones": ["+7-918-111-2222"],
        "email": "olga.pavlova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Игорь Кузнецов",
        "birth_date": "1998-07-30",
        "address": {
            "city": "Красноярск",
            "street": "Улица Лесная",
            "house_number": "222",
        },
        "phones": ["+7-913-222-3333"],
        "email": "igor.kuznetsov@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Анна Смирнова",
        "birth_date": "2000-09-14",
        "address": {
            "city": "Ульяновск",
            "street": "Улица Советская",
            "house_number": "333",
        },
        "phones": ["+7-842-333-4444"],
        "email": "anna.smirnova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Максим Петров",
        "birth_date": "1997-11-03",
        "address": {
            "city": "Воронеж",
            "street": "Улица Пушкина",
            "house_number": "444",
        },
        "phones": ["+7-920-444-5555"],
        "email": "maxim.petrov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Татьяна Иванова",
        "birth_date": "1999-01-28",
        "address": {
            "city": "Иркутск",
            "street": "Улица Байкальская",
            "house_number": "555",
        },
        "phones": ["+7-395-555-6666"],
        "email": "tatiana.ivanova@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Павел Васильев",
        "birth_date": "1998-03-17",
        "address": {"city": "Томск", "street": "Улица Гагарина", "house_number": "666"},
        "phones": ["+7-382-666-7777"],
        "email": "pavel.vasilyev@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Екатерина Новикова",
        "birth_date": "1997-06-10",
        "address": {
            "city": "Ярославль",
            "street": "Улица Ленина",
            "house_number": "777",
        },
        "phones": ["+7-485-777-8888"],
        "email": "ekaterina.novikova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Никита Морозов",
        "birth_date": "2000-08-05",
        "address": {
            "city": "Кемерово",
            "street": "Улица Сибирская",
            "house_number": "888",
        },
        "phones": ["+7-384-888-9999"],
        "email": "nikita.morozov@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Александра Попова",
        "birth_date": "1999-10-20",
        "address": {"city": "Барнаул", "street": "Улица Кирова", "house_number": "999"},
        "phones": ["+7-385-999-0000"],
        "email": "alexandra.popova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Дмитрий Соколов",
        "birth_date": "1998-12-15",
        "address": {
            "city": "Оренбург",
            "street": "Улица Гагарина",
            "house_number": "1111",
        },
        "phones": ["+7-353-111-2222"],
        "email": "dmitry.sokolov@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Владислава Ковалева",
        "birth_date": "1997-02-18",
        "address": {"city": "Пермь", "street": "Улица Ленина", "house_number": "112"},
        "phones": ["+7-342-112-2233"],
        "email": "vladislava.kovaleva@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Иван Григорьев",
        "birth_date": "1996-05-22",
        "address": {
            "city": "Владимир",
            "street": "Улица Горького",
            "house_number": "223",
        },
        "phones": ["+7-492-223-3344"],
        "email": "ivan.grigoryev@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Екатерина Степанова",
        "birth_date": "1997-08-26",
        "address": {"city": "Курск", "street": "Улица Пушкина", "house_number": "334"},
        "phones": ["+7-471-334-4455"],
        "email": "ekaterina.stepanova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Артем Жуков",
        "birth_date": "1996-11-30",
        "address": {
            "city": "Рязань",
            "street": "Улица Советская",
            "house_number": "445",
        },
        "phones": ["+7-491-445-5566"],
        "email": "artem.zhukov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Анастасия Тимофеева",
        "birth_date": "1998-03-04",
        "address": {"city": "Тверь", "street": "Улица Кирова", "house_number": "556"},
        "phones": ["+7-482-556-6677"],
        "email": "anastasia.timofeeva@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Григорий Козлов",
        "birth_date": "1999-06-08",
        "address": {"city": "Тула", "street": "Улица Гагарина", "house_number": "667"},
        "phones": ["+7-487-667-7788"],
        "email": "grigory.kozlov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Валентина Исаева",
        "birth_date": "1996-09-12",
        "address": {
            "city": "Улан-Удэ",
            "street": "Улица Ленина",
            "house_number": "778",
        },
        "phones": ["+7-301-778-8899"],
        "email": "valentina.isaeva@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Ирина Макарова",
        "birth_date": "1997-12-16",
        "address": {
            "city": "Белгород",
            "street": "Улица Строителей",
            "house_number": "889",
        },
        "phones": ["+7-472-889-9900"],
        "email": "irina.makarova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Михаил Павлов",
        "birth_date": "1998-02-20",
        "address": {
            "city": "Ижевск",
            "street": "Улица Комсомольская",
            "house_number": "990",
        },
        "phones": ["+7-341-990-0011"],
        "email": "mikhail.pavlov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "София Калинина",
        "birth_date": "1999-05-24",
        "address": {"city": "Тамбов", "street": "Улица Ленина", "house_number": "1001"},
        "phones": ["+7-475-1001-1122"],
        "email": "sofia.kalinina@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Ирина Калинина",
        "birth_date": "1999-05-24",
        "address": {
            "city": "Тамбов",
            "street": "Улица Павлова",
            "house_number": "1001",
        },
        "phones": ["+7-495-1001-1122"],
        "email": "uru.terg@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Ирина Козлова",
        "birth_date": "1997-03-25",
        "address": {
            "city": "Ижевск",
            "street": "Улица Гагарина",
            "house_number": "1112",
        },
        "phones": ["+7-341-112-2233"],
        "email": "irina.kozlova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Андрей Николаев",
        "birth_date": "2000-05-16",
        "address": {
            "city": "Ульяновск",
            "street": "Улица Ленина",
            "house_number": "1113",
        },
        "phones": ["+7-842-113-2244"],
        "email": "andrey.nikolaev@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Елена Петрова",
        "birth_date": "1998-07-17",
        "address": {
            "city": "Тамбов",
            "street": "Улица Советская",
            "house_number": "1114",
        },
        "phones": ["+7-475-114-2355"],
        "email": "elena.petrova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Михаил Смирнов",
        "birth_date": "1999-09-18",
        "address": {"city": "Курск", "street": "Улица Пушкина", "house_number": "1115"},
        "phones": ["+7-471-115-2466"],
        "email": "mikhail.smirnov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Анна Иванова",
        "birth_date": "1997-11-19",
        "address": {"city": "Уфа", "street": "Улица Ленина", "house_number": "1116"},
        "phones": ["+7-347-116-2577"],
        "email": "anna.ivanova@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Иван Кузнецов",
        "birth_date": "1998-01-20",
        "address": {
            "city": "Киров",
            "street": "Улица Сибирская",
            "house_number": "1117",
        },
        "phones": ["+7-833-117-2688"],
        "email": "ivan.kuznetsov@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Александра Васильева",
        "birth_date": "1999-03-21",
        "address": {"city": "Калуга", "street": "Улица Ленина", "house_number": "1118"},
        "phones": ["+7-484-118-2799"],
        "email": "alexandra.vasilyeva@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Сергей Новиков",
        "birth_date": "2000-05-22",
        "address": {
            "city": "Владимир",
            "street": "Улица Гагарина",
            "house_number": "1119",
        },
        "phones": ["+7-492-119-2900"],
        "email": "sergey.novikov@example.com",
        "group_id": group_id,
        "budget": False,
    },
    {
        "full_name": "Дарья Морозова",
        "birth_date": "1998-07-23",
        "address": {
            "city": "Саратов",
            "street": "Улица Красная",
            "house_number": "1120",
        },
        "phones": ["+7-845-120-3011"],
        "email": "darya.morozova@example.com",
        "group_id": group_id,
        "budget": True,
    },
    {
        "full_name": "Павел Попов",
        "birth_date": "1997-09-24",
        "address": {"city": "Орел", "street": "Улица Пушкина", "house_number": "1121"},
        "phones": ["+7-486-121-3122"],
        "email": "pavel.popov@example.com",
        "group_id": group_id,
        "budget": False,
    },
]


# Вставка студентов
student_ids = [
    students_collection.insert_one(student).inserted_id for student in students
]

# Проверка вставленных данных
print("Направления обучения:")
for direction in directions_collection.find():
    print(direction)

print("Группы:")
for group in groups_collection.find():
    print(group)

print("Студенты:")
for student in students_collection.find():
    print(student)

print("Преподаватели:")
for teacher in teachers_collection.find():
    print(teacher)

print("Предметы:")
for subject in subjects_collection.find():
    print(subject)

print("Оценки:")
for grade in grades_collection.find():
    print(grade)

print("Расписание:")
for schedule in schedule_collection.find():
    print(schedule)

print("Посещения:")
for attendance in attendance_collection.find():
    print(attendance)
