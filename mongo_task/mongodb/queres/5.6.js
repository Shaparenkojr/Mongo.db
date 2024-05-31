let groups_marks = {}

function get_group(student_id) {
    group_id = db.students.find({_id:student_id}, {group_id:1, _id: 0}).toArray()[0].group_id
    group = db.groups.find({_id: group_id}, {name: 1, _id:0}).toArray()[0].name
    return group
}

for(m of db.marks.find()) {
    student_group = get_group(m.student)
    if (student_group in groups_marks) {
        groups_marks[student_group].push(m.mark)
    } else {
        groups_marks[student_group] = [m.mark]
    }
}


for(gr of Object.keys(groups_marks)){
    groups_avg[gr] = groups_marks[gr].reduce((a, b) => a + b, 0) / groups_marks[gr].length
}

let sortable = []
for (gr of Object.keys(groups_avg)) {
    sortable.push([gr, groups_avg[gr]])
}

sortable.sort(function(a, b) {
    return b[1] - a[1]
})

print(sortable[0])