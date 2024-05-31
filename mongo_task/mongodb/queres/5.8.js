let students_marks = {}

for (m of db.marks.find()) {
    //students.add(db.students.find({_id: m.student}, {name:1, _id:0}).toArray()[0].name)
    student = db.students.find({ _id: m.student }, { name: 1, _id: 0 }).toArray()[0].name
    if (student in students_marks) {
        students_marks[student].add(m.mark)
    } else {
        students_marks[student] = new Set()
        students_marks[student].add(m.mark)
    }
}

great_student_counter = 0
for (st of Object.keys(students_marks)) {
    if (students_marks[st].size == 1 && students_marks[st].has(2)) {
        great_student_counter++
        print(st)
    }
}
if (great_student_counter == 0) {
    print("no such student")
}