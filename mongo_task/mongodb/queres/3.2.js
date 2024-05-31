students = db.students.find()
for (st of students) {
    last_name = st.name.split(" ")[0]
    if (last_name.slice(0, 1) == "Ш") {
        print(st.name)
        print(db.groups.find({ _id: st.group_id }, { name: 1, _id: 0, direction: 1 }))
        print("")
    }
}