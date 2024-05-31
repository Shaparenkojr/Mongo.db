hours_count = {}

function get_subj_from_sched(schedule_id) {
    subject = db.schedule.find({_id: schedule_id}, {subject: 1, _id:0}).toArray()[0].subject
    return(subject)
}

for (st of db.students.find().toArray()) {
    for (at of db.attendence.find().toArray()) {
        if (at.attendence == true) {
            subject = get_subj_from_sched(at.schedule)
            if (subject in hours_count) {
                hours_count[subject] += 1.5
            } else {
                hours_count[subject] = 0
            }
        }
    }
    print(st.name)
    print(hours_count)
    hours_count = {}
}

print(hours_count)

