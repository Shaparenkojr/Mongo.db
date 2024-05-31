for (gr of db.groups.find()) {
    print(gr.name)
    print(gr.direction)
    print("budget students: " + db.students.find({ group_id: gr._id, budget: "true" }).count())
    print("non budget students: " + db.students.find({ group_id: gr._id, budget: "false" }).count())
    print("")
}