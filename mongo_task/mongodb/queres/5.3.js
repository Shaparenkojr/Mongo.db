teacher_students = {}
for(m of db.marks.find()) {
    if (m.teacher in teacher_students && !(m.student in teacher_students[m.teacher])) {
        teacher_students[m.teacher].add(m.student.toString())
    } else if (!(m.teacher in teacher_students)) {
        teacher_students[m.teacher] = new Set()
        teacher_students[m.teacher].add(m.student.toString())
    }
}

for (key of Object.keys(teacher_students)) {
    print(key + ": " + teacher_students[key].size)
}