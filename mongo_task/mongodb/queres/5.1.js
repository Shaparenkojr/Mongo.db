for (t of db.teachers.find()) {
    print(t.subject + " " + t.name)
    groups = db.schedule.find({subject: t.subject}, {group:1, _id: 0}).toArray()
    for (gr of groups) {
        print(db.groups.find({_id: gr.group}, {name:1, _id: 0}).toArray()[0].name)
    }
    print()
}