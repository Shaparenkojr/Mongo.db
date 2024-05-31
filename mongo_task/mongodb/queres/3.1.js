students = db.students.find()
groups = db.groups.find()
for (gr of groups) {
    students_by_group = db.students.find({group_id:{_id:gr._id}}, {name:1, budget:1, _id:0}).sort({name: 1})
    print("Group:" + gr.name)
    print(students_by_group)
}