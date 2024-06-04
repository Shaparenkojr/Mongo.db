-- 3.1 запрос
SELECT
    s.name AS 'ФИО',
    CASE
        WHEN s.budget = 1 THEN 'Бюджет'
        ELSE 'Внебюджет'
    END AS 'Бюджет/Внебюджет',
    g.group_name AS 'Название группы',
    g.id AS 'Номер группы'
FROM
    students s
    JOIN groups g ON s.group_id = g.id
    JOIN directions_of_study d ON g.direction_id = d.id
WHERE
    d.direction_name = 'FI'
ORDER BY
    s.name;

--3.2 запрос
SELECT
    s.name AS 'ФИО',
    CASE
        WHEN s.budget = 1 THEN 'Бюджет'
        ELSE 'Внебюджет'
    END AS 'Бюджет/Внебюджет',
    g.group_name AS 'Название группы',
    g.id AS 'Номер группы'
FROM
    students s
    JOIN groups g ON s.group_id = g.id
    JOIN directions_of_study d ON g.direction_id = d.id
WHERE
    d.direction_name = 'FI'
ORDER BY
    s.name;

-- 3.3 запрос
SELECT
    s.name AS 'ФИО',
    g.group_name AS 'Название группы',
    g.id AS 'Номер группы',
    d.direction_name AS 'Направление обучения'
FROM
    students s
    JOIN groups g ON s.group_id = g.id
    JOIN directions_of_study d ON g.direction_id = d.id
WHERE
    SUBSTRING(s.name, 1, 1) = 'Ш' -- Замените 'В' на первую букву вашей фамилии
ORDER BY
    s.name;

-- 3.4 запрос 
SELECT
    s.name AS 'ФИО',
    DATEDIFF(year, s.date_of_birth, GETDATE()) AS 'Возраст (лет)'
FROM
    students s;

-- 3.5 запрос
SELECT
    s.name AS 'ФИО',
    s.date_of_birth AS 'Дата рождения'
FROM
    students s
WHERE
    MONTH(s.date_of_birth) = MONTH(GETDATE());

--3.6 запрос
SELECT
    d.direction_name AS 'Название направления',
    COUNT(s.id) AS 'Количество студентов'
FROM
    students s
    JOIN groups g ON s.group_id = g.id
    JOIN directions_of_study d ON g.direction_id = d.id
GROUP BY
    d.direction_name
ORDER BY
    d.direction_name;

--3.7 запрос
SELECT
    g.id AS 'Номер группы',
    g.group_name AS 'Название группы',
    d.direction_name AS 'Название направления',
    SUM(
        CASE
            WHEN s.budget = 1 THEN 1
            ELSE 0
        END
    ) AS 'Количество бюджетных мест',
    SUM(
        CASE
            WHEN s.budget = 0 THEN 1
            ELSE 0
        END
    ) AS 'Количество внебюджетных мест'
FROM
    students s
    JOIN groups g ON s.group_id = g.id
    JOIN directions_of_study d ON g.direction_id = d.id
GROUP BY
    g.id,
    g.group_name,
    d.direction_name
ORDER BY
    g.id;

--5.1 запрос
SELECT
    d.direction_name AS 'Название направления',
    g.group_name AS 'Название группы',
    g.id AS 'Номер группы',
    dis.name AS 'Название предмета',
    t.name AS 'Преподаватель'
FROM
    groups g
    JOIN directions_of_study d ON g.direction_id = d.id
    JOIN DirectionDisciplineTeacher ddt ON d.id = ddt.direction_id
    JOIN disciplines dis ON ddt.discipline_id = dis.id
    JOIN teachers t ON ddt.teacher_id = t.id
ORDER BY
    d.direction_name,
    g.group_name,
    dis.name;

--5.2 запрос
SELECT
    TOP 1 dis.name AS 'Название дисциплины',
    COUNT(DISTINCT s.id) AS 'Количество студентов'
FROM
    students s
    JOIN groups g ON s.group_id = g.id
    JOIN DirectionDisciplineTeacher ddt ON g.direction_id = ddt.direction_id
    JOIN disciplines dis ON ddt.discipline_id = dis.id
GROUP BY
    dis.name
ORDER BY
    COUNT(DISTINCT s.id) DESC;

-- 5.3 запрос
SELECT
    t.name AS 'Преподаватель',
    COUNT(DISTINCT s.id) AS 'Количество студентов'
FROM
    teachers t
    JOIN DirectionDisciplineTeacher ddt ON t.id = ddt.teacher_id
    JOIN groups g ON ddt.direction_id = g.direction_id
    JOIN students s ON g.id = s.group_id
GROUP BY
    t.name
ORDER BY
    t.name;

-- 5.4 запрос
SELECT
    d.name AS 'Дисциплина',
    SUM(
        CASE
            WHEN m.mark >= 3 THEN 1
            ELSE 0
        END
    ) AS 'Количество сдавших',
    SUM(
        CASE
            WHEN m.mark >= 2
            AND m.mark <= 3 THEN 1
            ELSE 0
        END
    ) AS 'Количество не сдавших',
    SUM(
        CASE
            WHEN m.mark IS NULL THEN 1
            ELSE 0
        END
    ) AS 'Количество не допущенных',
    (
        SUM(
            CASE
                WHEN m.mark >= 3 THEN 1
                ELSE 0
            END
        ) * 1.0 / (
            SUM(
                CASE
                    WHEN m.mark >= 3 THEN 1
                    ELSE 0
                END
            ) + SUM(
                CASE
                    WHEN m.mark >= 2
                    AND m.mark <= 3 THEN 1
                    ELSE 0
                END
            ) + SUM(
                CASE
                    WHEN m.mark IS NULL THEN 1
                    ELSE 0
                END
            )
        )
    ) * 100 AS 'Доля сдавших (в %)'
FROM
    disciplines d
    LEFT JOIN DirectionDisciplineTeacher ddt ON d.id = ddt.discipline_id
    LEFT JOIN marks m ON ddt.id = m.sub_disc_teach_id
GROUP BY
    d.name
ORDER BY
    d.name;

-- 5.5 запрос
SELECT
    d.name AS 'Дисциплина',
    AVG(
        CASE
            WHEN m.mark >= 3 THEN m.mark
            ELSE NULL
        END
    ) AS 'Средняя оценка'
FROM
    disciplines d
    LEFT JOIN DirectionDisciplineTeacher ddt ON d.id = ddt.discipline_id
    LEFT JOIN marks m ON ddt.id = m.sub_disc_teach_id
GROUP BY
    d.name
ORDER BY
    d.name;

-- 5.6 запрос
SELECT
    TOP 1 g.group_name AS 'Группа',
    AVG(m.mark) AS 'Средняя оценка'
FROM
    groups g
    JOIN students s ON g.id = s.group_id
    LEFT JOIN marks m ON s.id = m.student_id
GROUP BY
    g.group_name
ORDER BY
    AVG(m.mark) DESC;

-- 5.7 запрос
SELECT
    s.name AS 'ФИО студента',
    COUNT(DISTINCT m.sub_disc_teach_id) AS 'Количество не сданных предметов'
FROM
    students s
    LEFT JOIN marks m ON s.id = m.student_id
WHERE
    m.mark IS NULL
    OR m.mark < 3
GROUP BY
    s.name
HAVING
    COUNT(DISTINCT m.sub_disc_teach_id) >= 2
ORDER BY
    s.name;

-- 7.1 запрос
SELECT
    d.name AS 'Дисциплина',
    SUM(
        CASE
            WHEN la.status = 1 THEN 1
            ELSE 0
        END
    ) AS 'Количество посещенных занятий'
FROM
    disciplines d
    JOIN DirectionDisciplineTeacher ddt ON d.id = ddt.discipline_id
    JOIN LessonAttendance la ON ddt.id = la.sub_disc_teach_id
WHERE
    d.name = 'название_предмета'
GROUP BY
    d.name;

-- 7.2 запрос 
SELECT
    d.name AS 'Дисциплина',
    SUM(
        CASE
            WHEN la.status = 0 THEN 1
            ELSE 0
        END
    ) AS 'Количество пропущенных занятий'
FROM
    disciplines d
    JOIN DirectionDisciplineTeacher ddt ON d.id = ddt.discipline_id
    JOIN LessonAttendance la ON ddt.id = la.sub_disc_teach_id
WHERE
    d.name = 'название_предмета'
GROUP BY
    d.name;

-- 7.3 запрос
SELECT
    t.name AS 'Преподаватель',
    l.date AS 'Дата занятия',
    COUNT(DISTINCT la.student_id) AS 'Количество студентов'
FROM
    teachers t
    JOIN DirectionDisciplineTeacher ddt ON t.id = ddt.teacher_id
    JOIN lessons l ON ddt.id = l.sub_disc_teach_id
    JOIN LessonAttendance la ON l.id = la.lesson_id
WHERE
    t.name = 'имя_преподавателя'
GROUP BY
    t.name,
    l.date
ORDER BY
    l.date;

-- 7.4 запрос 
SELECT
    s.name AS 'ФИО студента',
    d.name AS 'Дисциплина',
    SUM(l.duration) AS 'Общее время (в минутах)'
FROM
    students s
    JOIN groups g ON s.group_id = g.id
    JOIN DirectionDisciplineTeacher ddt ON g.direction_id = ddt.direction_id
    JOIN disciplines d ON ddt.discipline_id = d.id
    JOIN lessons l ON ddt.id = l.sub_disc_teach_id
GROUP BY
    s.name,
    d.name
ORDER BY
    s.name,
    d.name;