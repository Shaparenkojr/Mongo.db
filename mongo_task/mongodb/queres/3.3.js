for (i = 1; i <= 12; i++) {
        print("Month " + i + ":")
    for (st of db.students.find()) {
        if (st.date_of_birth.split("-")[1] == "0" + i) {
            print(st.name)
        } else if (st.date_of_birth.split("-")[1] == i) {
            print(st.name)
        }
    }
}