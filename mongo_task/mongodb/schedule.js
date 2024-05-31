subject_teacher = [
    ["экономика", "Филатов Дмитрий Александрович"],
    ["кибербезопасность", " Манагаров Иван Александрович"],
    ["программирование", "Пестунов Андоей Игоревич"],
    ["философия", "Морозова Окксана Викторовна"],
    ["компьютерные сети", "Бабешко Владимир Николаевич"],
    ["геоинформтика", " Павлова Анна Илларионовна"],
    ["менджмент", "Тодеушовна Мария Барселоновна"],
    ["математика", "Чанышев Анвар Исмагилович"]
]
let sc_date = new Date('2023-09-4')
for (gr of db.groups.find()) {
    sc_date.setDate(sc_date.getDate() + 1)
    for (let pair_num = 1; pair_num < 4; pair_num++) {
        random = Math.floor(Math.random() * subject_teacher.length)
        db.schedule.insertOne({
            group: gr._id,
            number_pair: pair_num,
            subject: subject_teacher[random][0],
            teacher: subject_teacher[random][1],
            date: sc_date
        })
    }
}