subject = "философия"
count = 0
for (sc of db.schedule.find({subject: subject}).toArray()) {
    for (at of db.attendence.find({schedule: sc._id}).toArray()) {
        if (at.attendence == false) {
            count++
        }
    }
}
print(count)