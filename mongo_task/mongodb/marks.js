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

function randomIntFromInterval(min, max) { // min and max included 
    return Math.floor(Math.random() * (max - min + 1) + min);
}

for (st of db.students.find()) {
    for (let sem = 1; sem <= 4; sem++) {
        for (s_t of subject_teacher) {
            db.marks.insertOne({
                student: st._id,
                semestr: sem,
                subject: s_t[0],
                teacher: s_t[1],
                mark: randomIntFromInterval(2, 5)
            })
        }
    }
}