for (st of db.students.find()) {
    print(db.students.aggregate(
        {
            $project: {
                dateDiff: {
                    $dateDiff: {
                        startDate: {$toDate: st.date_of_birth},
                        endDate: "$$NOW", 
                        unit: "year"
                    }
                    
                },
                name: st.name
            }
        }
    ))
}