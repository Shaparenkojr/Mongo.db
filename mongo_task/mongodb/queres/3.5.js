for (st of db.students.find()) {
    if (st.date_of_birth.split("-")[1] == new Date().getMonth() + 1) {
        print(st.name)
    }
}