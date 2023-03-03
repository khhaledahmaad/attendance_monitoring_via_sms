
    (function(vegaEmbed) {
      var spec = {"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "hconcat": [{"vconcat": [{"layer": [{"mark": "rect", "encoding": {"color": {"type": "quantitative", "field": "total_attendees", "legend": {"title": "Total Attendees"}, "scale": {"scheme": "greenblue"}}, "x": {"type": "nominal", "bin": false, "field": "course_code", "title": "Course Code"}, "y": {"type": "quantitative", "bin": false, "field": "total_attendees", "title": "Total Attendance (Weekly)"}}, "height": 400, "title": "Total Attendees (Weekly) by Course", "width": 484}, {"mark": "point", "encoding": {"color": {"value": "grey"}, "size": {"type": "quantitative", "field": "total_attendees", "legend": {"title": "Total Attendees"}}, "x": {"type": "nominal", "bin": false, "field": "course_code", "title": "Course Code"}, "y": {"type": "quantitative", "bin": false, "field": "total_attendees", "title": "Total Attendance (Weekly)"}}, "height": 400, "title": "Total Attendees (Weekly) by Course", "width": 484}]}], "resolve": {"legend": {"color": "independent", "size": "independent"}}}, {"mark": {"type": "circle", "size": 200}, "encoding": {"color": {"type": "nominal", "field": "academic_semester", "title": "Semester"}, "tooltip": [{"type": "nominal", "field": "course_code"}, {"type": "nominal", "field": "course_name"}, {"type": "nominal", "field": "month"}, {"type": "quantitative", "field": "year"}, {"type": "nominal", "field": "academic_semester"}, {"type": "quantitative", "field": "academic_week"}, {"type": "quantitative", "field": "total_attendees"}], "x": {"type": "nominal", "field": "course_code", "title": "Course Code"}, "y": {"type": "quantitative", "field": "total_attendees", "title": "Total Attendance (Weekly)"}}, "height": 400, "selection": {"selector004": {"type": "interval", "bind": "scales", "encodings": ["x", "y"]}}, "title": "Total Attendees (Weekly) by Course", "width": 484}], "data": {"name": "data-b57aaa3ab7249dc63f1c82fc913b222e"}, "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json", "datasets": {"data-b57aaa3ab7249dc63f1c82fc913b222e": [{"course_name": "Engineering Mathematics and Modelling", "course_code": "101", "date": "26/09/2022", "year": 2022, "month": "September", "day": "Monday", "week": 39, "academic_semester": "1", "academic_week": 1, "total_attendees": 157}, {"course_name": "Digital Logic Design", "course_code": "102", "date": "27/09/2022", "year": 2022, "month": "September", "day": "Tuesday", "week": 39, "academic_semester": "1", "academic_week": 1, "total_attendees": 152}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "28/09/2022", "year": 2022, "month": "September", "day": "Wednesday", "week": 39, "academic_semester": "1", "academic_week": 1, "total_attendees": 157}, {"course_name": "Final Year Project", "course_code": "104", "date": "29/09/2022", "year": 2022, "month": "September", "day": "Thursday", "week": 39, "academic_semester": "1", "academic_week": 1, "total_attendees": 157}, {"course_name": "Computer Systems and Software Engineering", "course_code": "105", "date": "30/09/2022", "year": 2022, "month": "September", "day": "Friday", "week": 39, "academic_semester": "1", "academic_week": 1, "total_attendees": 151}, {"course_name": "Desging and Practice", "course_code": "106", "date": "26/09/2022", "year": 2022, "month": "September", "day": "Monday", "week": 39, "academic_semester": "1", "academic_week": 1, "total_attendees": 159}, {"course_name": "Engineering Computing", "course_code": "107", "date": "27/09/2022", "year": 2022, "month": "September", "day": "Tuesday", "week": 39, "academic_semester": "1", "academic_week": 1, "total_attendees": 157}, {"course_name": "Engineering Principles", "course_code": "108", "date": "28/09/2022", "year": 2022, "month": "September", "day": "Wednesday", "week": 39, "academic_semester": "1", "academic_week": 1, "total_attendees": 150}, {"course_name": "Innovation and Enterprise", "course_code": "109", "date": "29/09/2022", "year": 2022, "month": "September", "day": "Thursday", "week": 39, "academic_semester": "1", "academic_week": 1, "total_attendees": 154}, {"course_name": "Computer Networks", "course_code": "110", "date": "30/09/2022", "year": 2022, "month": "September", "day": "Friday", "week": 39, "academic_semester": "1", "academic_week": 1, "total_attendees": 151}, {"course_name": "Engineering Mathematics and Modelling", "course_code": "101", "date": "03/10/2022", "year": 2022, "month": "October", "day": "Monday", "week": 40, "academic_semester": "1", "academic_week": 2, "total_attendees": 156}, {"course_name": "Digital Logic Design", "course_code": "102", "date": "04/10/2022", "year": 2022, "month": "October", "day": "Tuesday", "week": 40, "academic_semester": "1", "academic_week": 2, "total_attendees": 150}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "05/10/2022", "year": 2022, "month": "October", "day": "Wednesday", "week": 40, "academic_semester": "1", "academic_week": 2, "total_attendees": 159}, {"course_name": "Final Year Project", "course_code": "104", "date": "06/10/2022", "year": 2022, "month": "October", "day": "Thursday", "week": 40, "academic_semester": "1", "academic_week": 2, "total_attendees": 155}, {"course_name": "Computer Systems and Software Engineering", "course_code": "105", "date": "07/10/2022", "year": 2022, "month": "October", "day": "Friday", "week": 40, "academic_semester": "1", "academic_week": 2, "total_attendees": 153}, {"course_name": "Desging and Practice", "course_code": "106", "date": "03/10/2022", "year": 2022, "month": "October", "day": "Monday", "week": 40, "academic_semester": "1", "academic_week": 2, "total_attendees": 150}, {"course_name": "Engineering Computing", "course_code": "107", "date": "04/10/2022", "year": 2022, "month": "October", "day": "Tuesday", "week": 40, "academic_semester": "1", "academic_week": 2, "total_attendees": 157}, {"course_name": "Engineering Principles", "course_code": "108", "date": "05/10/2022", "year": 2022, "month": "October", "day": "Wednesday", "week": 40, "academic_semester": "1", "academic_week": 2, "total_attendees": 155}, {"course_name": "Innovation and Enterprise", "course_code": "109", "date": "06/10/2022", "year": 2022, "month": "October", "day": "Thursday", "week": 40, "academic_semester": "1", "academic_week": 2, "total_attendees": 156}, {"course_name": "Computer Networks", "course_code": "110", "date": "07/10/2022", "year": 2022, "month": "October", "day": "Friday", "week": 40, "academic_semester": "1", "academic_week": 2, "total_attendees": 150}, {"course_name": "Engineering Mathematics and Modelling", "course_code": "101", "date": "10/10/2022", "year": 2022, "month": "October", "day": "Monday", "week": 41, "academic_semester": "1", "academic_week": 3, "total_attendees": 155}, {"course_name": "Digital Logic Design", "course_code": "102", "date": "11/10/2022", "year": 2022, "month": "October", "day": "Tuesday", "week": 41, "academic_semester": "1", "academic_week": 3, "total_attendees": 156}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "12/10/2022", "year": 2022, "month": "October", "day": "Wednesday", "week": 41, "academic_semester": "1", "academic_week": 3, "total_attendees": 152}, {"course_name": "Final Year Project", "course_code": "104", "date": "13/10/2022", "year": 2022, "month": "October", "day": "Thursday", "week": 41, "academic_semester": "1", "academic_week": 3, "total_attendees": 159}, {"course_name": "Computer Systems and Software Engineering", "course_code": "105", "date": "14/10/2022", "year": 2022, "month": "October", "day": "Friday", "week": 41, "academic_semester": "1", "academic_week": 3, "total_attendees": 154}, {"course_name": "Desging and Practice", "course_code": "106", "date": "10/10/2022", "year": 2022, "month": "October", "day": "Monday", "week": 41, "academic_semester": "1", "academic_week": 3, "total_attendees": 150}, {"course_name": "Engineering Computing", "course_code": "107", "date": "11/10/2022", "year": 2022, "month": "October", "day": "Tuesday", "week": 41, "academic_semester": "1", "academic_week": 3, "total_attendees": 158}, {"course_name": "Engineering Principles", "course_code": "108", "date": "12/10/2022", "year": 2022, "month": "October", "day": "Wednesday", "week": 41, "academic_semester": "1", "academic_week": 3, "total_attendees": 152}, {"course_name": "Innovation and Enterprise", "course_code": "109", "date": "13/10/2022", "year": 2022, "month": "October", "day": "Thursday", "week": 41, "academic_semester": "1", "academic_week": 3, "total_attendees": 155}, {"course_name": "Computer Networks", "course_code": "110", "date": "14/10/2022", "year": 2022, "month": "October", "day": "Friday", "week": 41, "academic_semester": "1", "academic_week": 3, "total_attendees": 153}, {"course_name": "Engineering Mathematics and Modelling", "course_code": "101", "date": "17/10/2022", "year": 2022, "month": "October", "day": "Monday", "week": 42, "academic_semester": "1", "academic_week": 4, "total_attendees": 157}, {"course_name": "Digital Logic Design", "course_code": "102", "date": "18/10/2022", "year": 2022, "month": "October", "day": "Tuesday", "week": 42, "academic_semester": "1", "academic_week": 4, "total_attendees": 153}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "19/10/2022", "year": 2022, "month": "October", "day": "Wednesday", "week": 42, "academic_semester": "1", "academic_week": 4, "total_attendees": 158}, {"course_name": "Final Year Project", "course_code": "104", "date": "20/10/2022", "year": 2022, "month": "October", "day": "Thursday", "week": 42, "academic_semester": "1", "academic_week": 4, "total_attendees": 158}, {"course_name": "Computer Systems and Software Engineering", "course_code": "105", "date": "21/10/2022", "year": 2022, "month": "October", "day": "Friday", "week": 42, "academic_semester": "1", "academic_week": 4, "total_attendees": 153}, {"course_name": "Desging and Practice", "course_code": "106", "date": "17/10/2022", "year": 2022, "month": "October", "day": "Monday", "week": 42, "academic_semester": "1", "academic_week": 4, "total_attendees": 159}, {"course_name": "Engineering Computing", "course_code": "107", "date": "18/10/2022", "year": 2022, "month": "October", "day": "Tuesday", "week": 42, "academic_semester": "1", "academic_week": 4, "total_attendees": 154}, {"course_name": "Engineering Principles", "course_code": "108", "date": "19/10/2022", "year": 2022, "month": "October", "day": "Wednesday", "week": 42, "academic_semester": "1", "academic_week": 4, "total_attendees": 158}, {"course_name": "Innovation and Enterprise", "course_code": "109", "date": "20/10/2022", "year": 2022, "month": "October", "day": "Thursday", "week": 42, "academic_semester": "1", "academic_week": 4, "total_attendees": 154}, {"course_name": "Computer Networks", "course_code": "110", "date": "21/10/2022", "year": 2022, "month": "October", "day": "Friday", "week": 42, "academic_semester": "1", "academic_week": 4, "total_attendees": 155}, {"course_name": "Engineering Mathematics and Modelling", "course_code": "101", "date": "24/10/2022", "year": 2022, "month": "October", "day": "Monday", "week": 43, "academic_semester": "1", "academic_week": 5, "total_attendees": 156}, {"course_name": "Digital Logic Design", "course_code": "102", "date": "25/10/2022", "year": 2022, "month": "October", "day": "Tuesday", "week": 43, "academic_semester": "1", "academic_week": 5, "total_attendees": 152}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "26/10/2022", "year": 2022, "month": "October", "day": "Wednesday", "week": 43, "academic_semester": "1", "academic_week": 5, "total_attendees": 155}, {"course_name": "Final Year Project", "course_code": "104", "date": "27/10/2022", "year": 2022, "month": "October", "day": "Thursday", "week": 43, "academic_semester": "1", "academic_week": 5, "total_attendees": 154}, {"course_name": "Computer Systems and Software Engineering", "course_code": "105", "date": "28/10/2022", "year": 2022, "month": "October", "day": "Friday", "week": 43, "academic_semester": "1", "academic_week": 5, "total_attendees": 155}, {"course_name": "Desging and Practice", "course_code": "106", "date": "24/10/2022", "year": 2022, "month": "October", "day": "Monday", "week": 43, "academic_semester": "1", "academic_week": 5, "total_attendees": 157}, {"course_name": "Engineering Computing", "course_code": "107", "date": "25/10/2022", "year": 2022, "month": "October", "day": "Tuesday", "week": 43, "academic_semester": "1", "academic_week": 5, "total_attendees": 151}, {"course_name": "Engineering Principles", "course_code": "108", "date": "26/10/2022", "year": 2022, "month": "October", "day": "Wednesday", "week": 43, "academic_semester": "1", "academic_week": 5, "total_attendees": 152}, {"course_name": "Innovation and Enterprise", "course_code": "109", "date": "27/10/2022", "year": 2022, "month": "October", "day": "Thursday", "week": 43, "academic_semester": "1", "academic_week": 5, "total_attendees": 152}, {"course_name": "Computer Networks", "course_code": "110", "date": "28/10/2022", "year": 2022, "month": "October", "day": "Friday", "week": 43, "academic_semester": "1", "academic_week": 5, "total_attendees": 157}, {"course_name": "Engineering Mathematics and Modelling", "course_code": "101", "date": "31/10/2022", "year": 2022, "month": "October", "day": "Monday", "week": 44, "academic_semester": "1", "academic_week": 6, "total_attendees": 153}, {"course_name": "Digital Logic Design", "course_code": "102", "date": "01/11/2022", "year": 2022, "month": "November", "day": "Tuesday", "week": 44, "academic_semester": "1", "academic_week": 6, "total_attendees": 155}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "02/11/2022", "year": 2022, "month": "November", "day": "Wednesday", "week": 44, "academic_semester": "1", "academic_week": 6, "total_attendees": 150}, {"course_name": "Final Year Project", "course_code": "104", "date": "03/11/2022", "year": 2022, "month": "November", "day": "Thursday", "week": 44, "academic_semester": "1", "academic_week": 6, "total_attendees": 159}, {"course_name": "Computer Systems and Software Engineering", "course_code": "105", "date": "04/11/2022", "year": 2022, "month": "November", "day": "Friday", "week": 44, "academic_semester": "1", "academic_week": 6, "total_attendees": 159}, {"course_name": "Desging and Practice", "course_code": "106", "date": "31/10/2022", "year": 2022, "month": "October", "day": "Monday", "week": 44, "academic_semester": "1", "academic_week": 6, "total_attendees": 151}, {"course_name": "Engineering Computing", "course_code": "107", "date": "01/11/2022", "year": 2022, "month": "November", "day": "Tuesday", "week": 44, "academic_semester": "1", "academic_week": 6, "total_attendees": 150}, {"course_name": "Engineering Principles", "course_code": "108", "date": "02/11/2022", "year": 2022, "month": "November", "day": "Wednesday", "week": 44, "academic_semester": "1", "academic_week": 6, "total_attendees": 152}, {"course_name": "Innovation and Enterprise", "course_code": "109", "date": "03/11/2022", "year": 2022, "month": "November", "day": "Thursday", "week": 44, "academic_semester": "1", "academic_week": 6, "total_attendees": 159}, {"course_name": "Computer Networks", "course_code": "110", "date": "04/11/2022", "year": 2022, "month": "November", "day": "Friday", "week": 44, "academic_semester": "1", "academic_week": 6, "total_attendees": 159}, {"course_name": "Engineering Mathematics and Modelling", "course_code": "101", "date": "07/11/2022", "year": 2022, "month": "November", "day": "Monday", "week": 45, "academic_semester": "1", "academic_week": 7, "total_attendees": 157}, {"course_name": "Digital Logic Design", "course_code": "102", "date": "08/11/2022", "year": 2022, "month": "November", "day": "Tuesday", "week": 45, "academic_semester": "1", "academic_week": 7, "total_attendees": 150}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "09/11/2022", "year": 2022, "month": "November", "day": "Wednesday", "week": 45, "academic_semester": "1", "academic_week": 7, "total_attendees": 157}, {"course_name": "Final Year Project", "course_code": "104", "date": "10/11/2022", "year": 2022, "month": "November", "day": "Thursday", "week": 45, "academic_semester": "1", "academic_week": 7, "total_attendees": 152}, {"course_name": "Computer Systems and Software Engineering", "course_code": "105", "date": "11/11/2022", "year": 2022, "month": "November", "day": "Friday", "week": 45, "academic_semester": "1", "academic_week": 7, "total_attendees": 150}, {"course_name": "Desging and Practice", "course_code": "106", "date": "07/11/2022", "year": 2022, "month": "November", "day": "Monday", "week": 45, "academic_semester": "1", "academic_week": 7, "total_attendees": 151}, {"course_name": "Engineering Computing", "course_code": "107", "date": "08/11/2022", "year": 2022, "month": "November", "day": "Tuesday", "week": 45, "academic_semester": "1", "academic_week": 7, "total_attendees": 154}, {"course_name": "Engineering Principles", "course_code": "108", "date": "09/11/2022", "year": 2022, "month": "November", "day": "Wednesday", "week": 45, "academic_semester": "1", "academic_week": 7, "total_attendees": 157}, {"course_name": "Innovation and Enterprise", "course_code": "109", "date": "10/11/2022", "year": 2022, "month": "November", "day": "Thursday", "week": 45, "academic_semester": "1", "academic_week": 7, "total_attendees": 153}, {"course_name": "Computer Networks", "course_code": "110", "date": "11/11/2022", "year": 2022, "month": "November", "day": "Friday", "week": 45, "academic_semester": "1", "academic_week": 7, "total_attendees": 153}, {"course_name": "Engineering Mathematics and Modelling", "course_code": "101", "date": "14/11/2022", "year": 2022, "month": "November", "day": "Monday", "week": 46, "academic_semester": "1", "academic_week": 8, "total_attendees": 153}, {"course_name": "Digital Logic Design", "course_code": "102", "date": "15/11/2022", "year": 2022, "month": "November", "day": "Tuesday", "week": 46, "academic_semester": "1", "academic_week": 8, "total_attendees": 158}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "16/11/2022", "year": 2022, "month": "November", "day": "Wednesday", "week": 46, "academic_semester": "1", "academic_week": 8, "total_attendees": 158}, {"course_name": "Final Year Project", "course_code": "104", "date": "17/11/2022", "year": 2022, "month": "November", "day": "Thursday", "week": 46, "academic_semester": "1", "academic_week": 8, "total_attendees": 156}, {"course_name": "Computer Systems and Software Engineering", "course_code": "105", "date": "18/11/2022", "year": 2022, "month": "November", "day": "Friday", "week": 46, "academic_semester": "1", "academic_week": 8, "total_attendees": 157}, {"course_name": "Desging and Practice", "course_code": "106", "date": "14/11/2022", "year": 2022, "month": "November", "day": "Monday", "week": 46, "academic_semester": "1", "academic_week": 8, "total_attendees": 158}, {"course_name": "Engineering Computing", "course_code": "107", "date": "15/11/2022", "year": 2022, "month": "November", "day": "Tuesday", "week": 46, "academic_semester": "1", "academic_week": 8, "total_attendees": 157}, {"course_name": "Engineering Principles", "course_code": "108", "date": "16/11/2022", "year": 2022, "month": "November", "day": "Wednesday", "week": 46, "academic_semester": "1", "academic_week": 8, "total_attendees": 158}, {"course_name": "Innovation and Enterprise", "course_code": "109", "date": "17/11/2022", "year": 2022, "month": "November", "day": "Thursday", "week": 46, "academic_semester": "1", "academic_week": 8, "total_attendees": 153}, {"course_name": "Computer Networks", "course_code": "110", "date": "18/11/2022", "year": 2022, "month": "November", "day": "Friday", "week": 46, "academic_semester": "1", "academic_week": 8, "total_attendees": 155}, {"course_name": "Engineering Mathematics and Modelling", "course_code": "101", "date": "21/11/2022", "year": 2022, "month": "November", "day": "Monday", "week": 47, "academic_semester": "1", "academic_week": 9, "total_attendees": 153}, {"course_name": "Digital Logic Design", "course_code": "102", "date": "22/11/2022", "year": 2022, "month": "November", "day": "Tuesday", "week": 47, "academic_semester": "1", "academic_week": 9, "total_attendees": 158}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "23/11/2022", "year": 2022, "month": "November", "day": "Wednesday", "week": 47, "academic_semester": "1", "academic_week": 9, "total_attendees": 159}, {"course_name": "Final Year Project", "course_code": "104", "date": "24/11/2022", "year": 2022, "month": "November", "day": "Thursday", "week": 47, "academic_semester": "1", "academic_week": 9, "total_attendees": 154}, {"course_name": "Computer Systems and Software Engineering", "course_code": "105", "date": "25/11/2022", "year": 2022, "month": "November", "day": "Friday", "week": 47, "academic_semester": "1", "academic_week": 9, "total_attendees": 157}, {"course_name": "Desging and Practice", "course_code": "106", "date": "21/11/2022", "year": 2022, "month": "November", "day": "Monday", "week": 47, "academic_semester": "1", "academic_week": 9, "total_attendees": 153}, {"course_name": "Engineering Computing", "course_code": "107", "date": "22/11/2022", "year": 2022, "month": "November", "day": "Tuesday", "week": 47, "academic_semester": "1", "academic_week": 9, "total_attendees": 152}, {"course_name": "Engineering Principles", "course_code": "108", "date": "23/11/2022", "year": 2022, "month": "November", "day": "Wednesday", "week": 47, "academic_semester": "1", "academic_week": 9, "total_attendees": 158}, {"course_name": "Innovation and Enterprise", "course_code": "109", "date": "24/11/2022", "year": 2022, "month": "November", "day": "Thursday", "week": 47, "academic_semester": "1", "academic_week": 9, "total_attendees": 157}, {"course_name": "Computer Networks", "course_code": "110", "date": "25/11/2022", "year": 2022, "month": "November", "day": "Friday", "week": 47, "academic_semester": "1", "academic_week": 9, "total_attendees": 155}, {"course_name": "Engineering Mathematics and Modelling", "course_code": "101", "date": "28/11/2022", "year": 2022, "month": "November", "day": "Monday", "week": 48, "academic_semester": "1", "academic_week": 10, "total_attendees": 151}, {"course_name": "Digital Logic Design", "course_code": "102", "date": "29/11/2022", "year": 2022, "month": "November", "day": "Tuesday", "week": 48, "academic_semester": "1", "academic_week": 10, "total_attendees": 151}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "30/11/2022", "year": 2022, "month": "November", "day": "Wednesday", "week": 48, "academic_semester": "1", "academic_week": 10, "total_attendees": 154}, {"course_name": "Final Year Project", "course_code": "104", "date": "01/12/2022", "year": 2022, "month": "December", "day": "Thursday", "week": 48, "academic_semester": "1", "academic_week": 10, "total_attendees": 155}, {"course_name": "Computer Systems and Software Engineering", "course_code": "105", "date": "02/12/2022", "year": 2022, "month": "December", "day": "Friday", "week": 48, "academic_semester": "1", "academic_week": 10, "total_attendees": 155}, {"course_name": "Desging and Practice", "course_code": "106", "date": "28/11/2022", "year": 2022, "month": "November", "day": "Monday", "week": 48, "academic_semester": "1", "academic_week": 10, "total_attendees": 150}, {"course_name": "Engineering Computing", "course_code": "107", "date": "29/11/2022", "year": 2022, "month": "November", "day": "Tuesday", "week": 48, "academic_semester": "1", "academic_week": 10, "total_attendees": 153}, {"course_name": "Engineering Principles", "course_code": "108", "date": "30/11/2022", "year": 2022, "month": "November", "day": "Wednesday", "week": 48, "academic_semester": "1", "academic_week": 10, "total_attendees": 156}, {"course_name": "Innovation and Enterprise", "course_code": "109", "date": "01/12/2022", "year": 2022, "month": "December", "day": "Thursday", "week": 48, "academic_semester": "1", "academic_week": 10, "total_attendees": 157}, {"course_name": "Computer Networks", "course_code": "110", "date": "02/12/2022", "year": 2022, "month": "December", "day": "Friday", "week": 48, "academic_semester": "1", "academic_week": 10, "total_attendees": 154}, {"course_name": "Engineering Mathematics and Modelling", "course_code": "101", "date": "05/12/2022", "year": 2022, "month": "December", "day": "Monday", "week": 49, "academic_semester": "1", "academic_week": 11, "total_attendees": 158}, {"course_name": "Digital Logic Design", "course_code": "102", "date": "06/12/2022", "year": 2022, "month": "December", "day": "Tuesday", "week": 49, "academic_semester": "1", "academic_week": 11, "total_attendees": 155}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "07/12/2022", "year": 2022, "month": "December", "day": "Wednesday", "week": 49, "academic_semester": "1", "academic_week": 11, "total_attendees": 159}, {"course_name": "Final Year Project", "course_code": "104", "date": "08/12/2022", "year": 2022, "month": "December", "day": "Thursday", "week": 49, "academic_semester": "1", "academic_week": 11, "total_attendees": 155}, {"course_name": "Computer Systems and Software Engineering", "course_code": "105", "date": "09/12/2022", "year": 2022, "month": "December", "day": "Friday", "week": 49, "academic_semester": "1", "academic_week": 11, "total_attendees": 159}, {"course_name": "Desging and Practice", "course_code": "106", "date": "05/12/2022", "year": 2022, "month": "December", "day": "Monday", "week": 49, "academic_semester": "1", "academic_week": 11, "total_attendees": 151}, {"course_name": "Engineering Computing", "course_code": "107", "date": "06/12/2022", "year": 2022, "month": "December", "day": "Tuesday", "week": 49, "academic_semester": "1", "academic_week": 11, "total_attendees": 157}, {"course_name": "Engineering Principles", "course_code": "108", "date": "07/12/2022", "year": 2022, "month": "December", "day": "Wednesday", "week": 49, "academic_semester": "1", "academic_week": 11, "total_attendees": 159}, {"course_name": "Innovation and Enterprise", "course_code": "109", "date": "08/12/2022", "year": 2022, "month": "December", "day": "Thursday", "week": 49, "academic_semester": "1", "academic_week": 11, "total_attendees": 159}, {"course_name": "Computer Networks", "course_code": "110", "date": "09/12/2022", "year": 2022, "month": "December", "day": "Friday", "week": 49, "academic_semester": "1", "academic_week": 11, "total_attendees": 155}, {"course_name": "Engineering Mathematics and Modelling", "course_code": "101", "date": "12/12/2022", "year": 2022, "month": "December", "day": "Monday", "week": 50, "academic_semester": "1", "academic_week": 12, "total_attendees": 158}, {"course_name": "Digital Logic Design", "course_code": "102", "date": "13/12/2022", "year": 2022, "month": "December", "day": "Tuesday", "week": 50, "academic_semester": "1", "academic_week": 12, "total_attendees": 150}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "14/12/2022", "year": 2022, "month": "December", "day": "Wednesday", "week": 50, "academic_semester": "1", "academic_week": 12, "total_attendees": 157}, {"course_name": "Final Year Project", "course_code": "104", "date": "15/12/2022", "year": 2022, "month": "December", "day": "Thursday", "week": 50, "academic_semester": "1", "academic_week": 12, "total_attendees": 159}, {"course_name": "Computer Systems and Software Engineering", "course_code": "105", "date": "16/12/2022", "year": 2022, "month": "December", "day": "Friday", "week": 50, "academic_semester": "1", "academic_week": 12, "total_attendees": 150}, {"course_name": "Desging and Practice", "course_code": "106", "date": "12/12/2022", "year": 2022, "month": "December", "day": "Monday", "week": 50, "academic_semester": "1", "academic_week": 12, "total_attendees": 155}, {"course_name": "Engineering Computing", "course_code": "107", "date": "13/12/2022", "year": 2022, "month": "December", "day": "Tuesday", "week": 50, "academic_semester": "1", "academic_week": 12, "total_attendees": 151}, {"course_name": "Engineering Principles", "course_code": "108", "date": "14/12/2022", "year": 2022, "month": "December", "day": "Wednesday", "week": 50, "academic_semester": "1", "academic_week": 12, "total_attendees": 158}, {"course_name": "Innovation and Enterprise", "course_code": "109", "date": "15/12/2022", "year": 2022, "month": "December", "day": "Thursday", "week": 50, "academic_semester": "1", "academic_week": 12, "total_attendees": 152}, {"course_name": "Computer Networks", "course_code": "110", "date": "16/12/2022", "year": 2022, "month": "December", "day": "Friday", "week": 50, "academic_semester": "1", "academic_week": 12, "total_attendees": 157}, {"course_name": "Cybersecurity and Cryptography", "course_code": "103", "date": "25/01/2023", "year": 2023, "month": "January", "day": "Wednesday", "week": 4, "academic_semester": "2", "academic_week": 1, "total_attendees": 1}, {"course_name": "Final Year Project", "course_code": "104", "date": "2023-02-02", "year": 2023, "month": "February", "day": "Thursday", "week": 5, "academic_semester": "2", "academic_week": 2, "total_attendees": 1}]}};
      var embedOpt = {"mode": "vega-lite"};

      function showError(el, error){
          el.innerHTML = ('<div class="error" style="color:red;">'
                          + '<p>JavaScript Error: ' + error.message + '</p>'
                          + "<p>This usually means there's a typo in your chart specification. "
                          + "See the javascript console for the full traceback.</p>"
                          + '</div>');
          throw error;
      }
      const el = document.getElementById('vis');
      vegaEmbed("#vis", spec, embedOpt)
        .catch(error => showError(el, error));
    })(vegaEmbed);

  