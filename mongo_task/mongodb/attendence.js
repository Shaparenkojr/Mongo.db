for (s of db.schedule.find()) {
    for (st of db.students.find({group_id: s.group}).toArray()) {
        db.attendence.insertOne({
            schedule: s._id,
            student: st._id,
            attendence: Math.random() < 0.5
        })
    }
}