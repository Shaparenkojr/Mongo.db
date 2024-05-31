let passet_students = new Set()

for (m of db.marks.find()) {
    if (m.mark > 2) {
        student = db.students.find({_id: m.student}, {name: 1, _id: 0}).toArray()[0].name
        passet_students.add(student)
    }
}
print(passet_students)