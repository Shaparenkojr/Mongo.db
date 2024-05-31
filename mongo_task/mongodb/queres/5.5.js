let subject_marks = {}

for (m of db.marks.find()) {
    if (m.mark > 2) {
        if (m.subject in subject_marks) {
            subject_marks[m.subject].push(m.mark)
        } else {
            subject_marks[m.subject] = [m.mark]
        }
    }
}

let sub_avg = {}

for(sb of Object.keys(subject_marks)){
    sub_avg[sb] = subject_marks[sb].reduce((a, b) => a + b, 0) / subject_marks[sb].length
}

print(sub_avg)