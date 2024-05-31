db.students.insertMany([
    {
        "name": "Иванов Иван Иванович",
        "date_of_birth": "1999-12-15",
        "addres": "Москва, ул. Пушкина, д. 1",
        "email": "ivanov.ivan@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000001"
    },
    {
        "name": "Петров Петр Петрович",
        "date_of_birth": "2000-11-20",
        "addres": "Санкт-Петербург, Невский проспект, д. 2",
        "email": "petrov.petr@example.com",
        "group_id": db.groups.findOne({ "name": "РСО101" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000002"
    },
    {
        "name": "Сидорова Мария Ивановна",
        "date_of_birth": "2001-10-30",
        "addres": "Екатеринбург, ул. Ленина, д. 3",
        "email": "sidorova.maria@example.com",
        "group_id": db.groups.findOne({ "name": "РСО102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000003"
    },
    {
        "name": "Кузнецов Алексей Петрович",
        "date_of_birth": "2002-09-25",
        "addres": "Новосибирск, ул. Советская, д. 4",
        "email": "kuznetsov.alexey@example.com",
        "group_id": db.groups.findOne({ "name": "РСО102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000004"
    },
    {
        "name": "Васильева Анна Сергеевна",
        "date_of_birth": "2003-08-14",
        "addres": "Казань, ул. Баумана, д. 5",
        "email": "vasilieva.anna@example.com",
        "group_id": db.groups.findOne({ "name": "РСО103" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000005"
    },
    {
        "name": "Смирнов Дмитрий Алексеевич",
        "date_of_birth": "2004-07-10",
        "addres": "Красноярск, ул. Ломоносова, д. 6",
        "email": "smirnov.dmitry@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ103" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000006"
    },
    {
        "name": "Морозова Ольга Викторовна",
        "date_of_birth": "2000-06-05",
        "addres": "Тюмень, ул. Профсоюзная, д. 7",
        "email": "morozova.olga@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000007"
    },
    {
        "name": "Попов Сергей Владимирович",
        "date_of_birth": "1999-04-20",
        "addres": "Челябинск, ул. Комсомольская, д. 8",
        "email": "popov.sergey@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000008"
    },
    {
        "name": "Соколов Артем Андреевич",
        "date_of_birth": "2001-12-11",
        "addres": "Воронеж, ул. Мира, д. 9",
        "email": "sokolov.artem@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ103" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000009"
    },
    {
        "name": "Михайлова Наталья Петровна",
        "date_of_birth": "2002-11-22",
        "addres": "Самара, ул. Лесная, д. 10",
        "email": "mihaylova.natalya@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000010"
    },
    {
        "name": "Романов Никита Алексеевич",
        "date_of_birth": "2003-03-15",
        "addres": "Иркутск, ул. Октябрьская, д. 11",
        "email": "romanov.nikita@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000011"
    },
    {
        "name": "Григорьева Мария Сергеевна",
        "date_of_birth": "2004-02-10",
        "addres": "Уфа, ул. Молодежная, д. 12",
        "email": "grigorieva.maria@example.com",
        "group_id": db.groups.findOne({ "name": "РСО102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000012"
    },
    {
        "name": "Яковлев Андрей Дмитриевич",
        "date_of_birth": "1999-01-25",
        "addres": "Пермь, ул. Северная, д. 13",
        "email": "yakovlev.andrey@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000013"
    },
    {
        "name": "Зайцева Екатерина Владимировна",
        "date_of_birth": "2000-10-16",
        "addres": "Владивосток, ул. Восточная, д. 14",
        "email": "zaitseva.ekaterina@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000014"
    },
    {
        "name": "Федоров Денис Викторович",
        "date_of_birth": "2001-09-04",
        "addres": "Томск, ул. Западная, д. 15",
        "email": "fedorov.denis@example.com",
        "group_id": db.groups.findOne({ "name": "ИС102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000015"
    },
    {
        "name": "Алексеева Марина Павловна",
        "date_of_birth": "2002-08-19",
        "addres": "Омск, ул. Южная, д. 16",
        "email": "alekseeva.marina@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000016"
    },
    {
        "name": "Николаев Артем Сергеевич",
        "date_of_birth": "2003-07-14",
        "addres": "Волгоград, ул. Центральная, д. 17",
        "email": "nikolaev.artem@example.com",
        "group_id": db.groups.findOne({ "name": "ИС101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000017"
    },
    {
        "name": "Крылова Татьяна Алексеевна",
        "date_of_birth": "2004-06-12",
        "addres": "Саратов, ул. Крайняя, д. 18",
        "email": "krylova.tatyana@example.com",
        "group_id": db.groups.findOne({ "name": "ИС101" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000018"
    },
    {
        "name": "Медведев Михаил Иванович",
        "date_of_birth": "1999-05-11",
        "addres": "Тула, ул. Рубиновая, д. 19",
        "email": "medvedev.mikhail@example.com",
        "group_id": db.groups.findOne({ "name": "ИС102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000019"
    },
    {
        "name": "Орлова Елена Викторовна",
        "date_of_birth": "2000-04-18",
        "addres": "Рязань, ул. Гоголя, д. 20",
        "email": "orlova.elena@example.com",
        "group_id": db.groups.findOne({ "name": "Э101" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000020"
    },
    {
        "name": "Волков Андрей Сергеевич",
        "date_of_birth": "2001-03-07",
        "addres": "Пенза, ул. Лесная, д. 21",
        "email": "volkov.andrey@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000021"
    },
    {
        "name": "Тимофеева Анна Алексеевна",
        "date_of_birth": "2002-02-05",
        "addres": "Тверь, ул. Лермонтова, д. 22",
        "email": "timofeeva.anna@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ103" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000022"
    },
    {
        "name": "Ефимов Игорь Викторович",
        "date_of_birth": "2003-01-15",
        "addres": "Кострома, ул. Трудовая, д. 23",
        "email": "efimov.igor@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000023"
    },
    {
        "name": "Лебедева Наталья Сергеевна",
        "date_of_birth": "2004-12-21",
        "addres": "Архангельск, ул. Вокзальная, д. 24",
        "email": "lebedeva.natalya@example.com",
        "group_id": db.groups.findOne({ "name": "Э101" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000024"
    },
    {
        "name": "Миронов Алексей Андреевич",
        "date_of_birth": "1999-11-09",
        "addres": "Калуга, ул. Гагарина, д. 25",
        "email": "mironov.alexey@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000025"
    },
    {
        "name": "Савельева Марина Викторовна",
        "date_of_birth": "2000-10-30",
        "addres": "Смоленск, ул. Советская, д. 26",
        "email": "savelieva.marina@example.com",
        "group_id": db.groups.findOne({ "name": "Э102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000026"
    },
    {
        "name": "Семенов Артем Петрович",
        "date_of_birth": "2001-09-18",
        "addres": "Владимир, ул. Ленина, д. 27",
        "email": "semenov.artem@example.com",
        "group_id": db.groups.findOne({ "name": "Э102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000027"
    },
    {
        "name": "Захарова Елена Николаевна",
        "date_of_birth": "2002-08-07",
        "addres": "Ярославль, ул. Кольцевая, д. 28",
        "email": "zaharova.elena@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000028"
    },
    {
        "name": "Павлов Алексей Сергеевич",
        "date_of_birth": "2003-07-25",
        "addres": "Чита, ул. Вишневая, д. 29",
        "email": "pavlov.alexey@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000029"
    },
    {
        "name": "Гусева Ольга Владимировна",
        "date_of_birth": "2004-06-16",
        "addres": "Якутск, ул. Дружбы, д. 30",
        "email": "guseva.olga@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000030"
    },
    {
        "name": "Прохоров Илья Дмитриевич",
        "date_of_birth": "1999-05-23",
        "addres": "Киров, ул. Комсомольская, д. 31",
        "email": "prokhorov.ilya@example.com",
        "group_id": db.groups.findOne({ "name": "Э101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000031"
    },
    {
        "name": "Анисимова Татьяна Павловна",
        "date_of_birth": "2000-04-15",
        "addres": "Астрахань, ул. Набережная, д. 32",
        "email": "anisimova.tatyana@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000032"
    },
    {
        "name": "Григорьев Максим Сергеевич",
        "date_of_birth": "2001-03-12",
        "addres": "Белгород, ул. Пушкина, д. 33",
        "email": "grigoriev.maxim@example.com",
        "group_id": db.groups.findOne({ "name": "РСО101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000033"
    },
    {
        "name": "Ермакова Анастасия Викторовна",
        "date_of_birth": "2002-02-18",
        "addres": "Биробиджан, ул. Ленина, д. 34",
        "email": "ermakova.anastasia@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000034"
    },
    {
        "name": "Макаров Андрей Николаевич",
        "date_of_birth": "2003-01-20",
        "addres": "Владикавказ, ул. Гагарина, д. 35",
        "email": "makarov.andrey@example.com",
        "group_id": db.groups.findOne({ "name": "Э101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000035"
    },
    {
        "name": "Гусарова Елена Владимировна",
        "date_of_birth": "2004-12-15",
        "addres": "Грозный, ул. Школьная, д. 36",
        "email": "gusarova.elena@example.com",
        "group_id": db.groups.findOne({ "name": "Э102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000036"
    },
    {
        "name": "Воронцов Дмитрий Иванович",
        "date_of_birth": "1999-11-23",
        "addres": "Йошкар-Ола, ул. Молодежная, д. 37",
        "email": "vorontsov.dmitry@example.com",
        "group_id": db.groups.findOne({ "name": "РСО101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000037"
    },
    {
        "name": "Лазарева Ольга Викторовна",
        "date_of_birth": "2000-10-21",
        "addres": "Кемерово, ул. Северная, д. 38",
        "email": "lazareva.olga@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ103" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000038"
    },
    {
        "name": "Фролов Максим Петрович",
        "date_of_birth": "2001-09-17",
        "addres": "Курск, ул. Ленина, д. 39",
        "email": "frolov.maxim@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000039"
    },
    {
        "name": "Борисова Анастасия Ивановна",
        "date_of_birth": "2002-08-13",
        "addres": "Мурманск, ул. Советская, д. 40",
        "email": "borisova.anastasia@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000040"
    },
    {
        "name": "Соболев Иван Сергеевич",
        "date_of_birth": "2003-07-10",
        "addres": "Набережные Челны, ул. Комсомольская, д. 41",
        "email": "sobolev.ivan@example.com",
        "group_id": db.groups.findOne({ "name": "РСО101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000041"
    },
    {
        "name": "Терехова Мария Владимировна",
        "date_of_birth": "2004-06-14",
        "addres": "Нальчик, ул. Пушкина, д. 42",
        "email": "terehova.maria@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000042"
    },
    {
        "name": "Рябова Анна Алексеевна",
        "date_of_birth": "1999-05-21",
        "addres": "Нижний Новгород, ул. Мира, д. 43",
        "email": "ryabova.anna@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000043"
    },
    {
        "name": "Шестаков Петр Викторович",
        "date_of_birth": "2000-04-16",
        "addres": "Новокузнецк, ул. Гагарина, д. 44",
        "email": "shestakov.petr@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000044"
    },
    {
        "name": "Панова Марина Сергеевна",
        "date_of_birth": "2001-03-13",
        "addres": "Новосибирск, ул. Ленина, д. 45",
        "email": "panova.marina@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000045"
    },
    {
        "name": "Коновалов Андрей Владимирович",
        "date_of_birth": "2002-02-20",
        "addres": "Петрозаводск, ул. Комсомольская, д. 46",
        "email": "konovalov.andrey@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000046"
    },
    {
        "name": "Герасимова Татьяна Ивановна",
        "date_of_birth": "2003-01-27",
        "addres": "Ростов-на-Дону, ул. Советская, д. 47",
        "email": "gerasimova.tatyana@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000047"
    },
    {
        "name": "Голубев Сергей Викторович",
        "date_of_birth": "2004-12-30",
        "addres": "Рязань, ул. Ленина, д. 48",
        "email": "golubev.sergey@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000048"
    },
    {
        "name": "Воронина Марина Алексеевна",
        "date_of_birth": "1999-11-26",
        "addres": "Санкт-Петербург, ул. Комсомольская, д. 49",
        "email": "voronina.marina@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ103" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000049"
    },
    {
        "name": "Беляев Николай Дмитриевич",
        "date_of_birth": "2000-10-24",
        "addres": "Саратов, ул. Советская, д. 50",
        "email": "belyaev.nikolay@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000050"
    },
    {
        "name": "Руднева Анастасия Павловна",
        "date_of_birth": "2001-09-19",
        "addres": "Симферополь, ул. Ленина, д. 51",
        "email": "rudneva.anastasia@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000051"
    },
    {
        "name": "Мартынов Дмитрий Иванович",
        "date_of_birth": "2002-08-12",
        "addres": "Сочи, ул. Советская, д. 52",
        "email": "martynov.dmitry@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ103" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000052"
    },
    {
        "name": "Токарева Ольга Викторовна",
        "date_of_birth": "2003-07-11",
        "addres": "Ставрополь, ул. Гагарина, д. 53",
        "email": "tokareva.olga@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ103" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000053"
    },
    {
        "name": "Жуков Артем Сергеевич",
        "date_of_birth": "2004-06-13",
        "addres": "Сыктывкар, ул. Комсомольская, д. 54",
        "email": "zhukov.artem@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000054"
    },
    {
        "name": "Галкин Александр Андреевич",
        "date_of_birth": "1999-05-24",
        "addres": "Тамбов, ул. Ленина, д. 55",
        "email": "galkin.alexander@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000055"
    },
    {
        "name": "Михайлова Наталья Викторовна",
        "date_of_birth": "2000-04-12",
        "addres": "Тверь, ул. Гагарина, д. 56",
        "email": "mikhailova.natalya@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000056"
    },
    {
        "name": "Петров Виктор Михайлович",
        "date_of_birth": "2001-03-11",
        "addres": "Томск, ул. Пушкина, д. 57",
        "email": "petrov.viktor@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000057"
    },
    {
        "name": "Павлова Ирина Сергеевна",
        "date_of_birth": "2002-02-15",
        "addres": "Тула, ул. Ленина, д. 58",
        "email": "pavlova.irina@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000058"
    },
    {
        "name": "Федоров Михаил Андреевич",
        "date_of_birth": "2003-01-16",
        "addres": "Ульяновск, ул. Комсомольская, д. 59",
        "email": "fedorov.mikhail@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ102" }, { _id: 1 })._id,
        "budget": "false",
        "phone_number": "+79000000059"
    },
    {
        "name": "Ульянов Алексей Викторович",
        "date_of_birth": "2004-12-22",
        "addres": "Уфа, ул. Гагарина, д. 60",
        "email": "kozlov.alexey@example.com",
        "group_id": db.groups.findOne({ "name": "ФИ101" }, { _id: 1 })._id,
        "budget": "true",
        "phone_number": "+79000000060"
    }
])
