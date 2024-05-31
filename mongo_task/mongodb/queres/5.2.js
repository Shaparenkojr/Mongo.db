print(db.schedule.aggregate(
    [
        {
            $group:
            {
                _id:{group: "$group", subject: "$subject"},
                subjectCount: {$count: {}},
            }
        }, 
        {
            $sort: {
                "subjectCount": -1
            }
        }, 
        {
            $limit: 1
        }
    ]
))