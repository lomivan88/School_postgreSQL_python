DROP TABLE IF EXISTS students, items, items_student, teachers, grades;
CREATE TABLE students (
	student_id SERIAL NOT NULL,
	first_name VARCHAR (64) NOT NULL,
	second_name VARCHAR (64) NOT NULL,
	date_of_birth TIMESTAMP NOT NULL,
	gender CHAR,
	CONSTRAINT "PK_student_id" PRIMARY KEY (student_id)
);
CREATE TABLE teachers (
	teacher_id SERIAL NOT NULL,
	first_name VARCHAR (64) NOT NULL,
	second_name VARCHAR (64) NOT NULL,
	title VARCHAR(8),
	CONSTRAINT "PK_teacher_id" PRIMARY KEY (teacher_id)
);

CREATE TABLE items (
	item_id SERIAL NOT NULL,
	item_name VARCHAR (64) NOT NULL,
	teacher_id int NOT NULL,
	description VARCHAR (128),
	CONSTRAINT "PK_items_id" PRIMARY KEY (item_id),
	CONSTRAINT "FK_teacher_id" FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE SET NULL ON UPDATE CASCADE
	);

CREATE TABLE items_student (
	student_id int NOT NULL,
	item_id int NOT NULL,
	CONSTRAINT "PK_student_item" PRIMARY KEY (student_id, item_id)
);
CREATE TABLE grades(
	grade_id SERIAL NOT NULL,
	student_id INT NOT NULL,
	item_id INT NOT NULL,
	description VARCHAR (128),
	grade INT NOT NULL,
	CONSTRAINT "PK_grade_id" PRIMARY KEY (grade_id),
	CONSTRAINT "FK_student_id_grade" FOREIGN KEY (student_id) REFERENCES students(student_id) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT "FK_item_id_grade" FOREIGN KEY (item_id) REFERENCES items(item_id) ON UPDATE CASCADE ON DELETE CASCADE
);

--Data k testování
INSERT INTO students (first_name, second_name, date_of_birth, gender) VALUES ('Michal', 'Vancura', '1988-05-12', 'M');
INSERT INTO students (first_name, second_name, date_of_birth, gender) VALUES ('Emma', 'Vancurova', '2017-05-27', 'F');
INSERT INTO students (first_name, second_name, date_of_birth, gender) VALUES ('Katerina', 'Vancurova', '1991-05-27', 'F');
INSERT INTO students (first_name, second_name, date_of_birth, gender) VALUES ('Karel', 'Novak', '1995-03-25', 'M');
INSERT INTO teachers (first_name, second_name, title) VALUES ('Kryšpín', 'Malý', 'Ing.');
INSERT INTO teachers (first_name, second_name, title) VALUES ('Franta', 'Velký', 'Mgr.');
INSERT INTO teachers (first_name, second_name, title) VALUES ('Anežka', 'Obecná', 'Bc.');
INSERT INTO items (item_name, teacher_id, description) VALUES ('English', 1, 'English language for czech students.');
INSERT INTO items (item_name, teacher_id, description) VALUES ('Math-I', 1, 'First level of math.');
INSERT INTO items (item_name, teacher_id, description) VALUES ('History', 2,'History of europe.');
INSERT INTO items_student (student_id, item_id) VALUES (1, 2);
INSERT INTO items_student (student_id, item_id) VALUES (1, 1);
INSERT INTO items_student (student_id, item_id) VALUES (2, 1);
INSERT INTO items_student (student_id, item_id) VALUES (3, 1);
INSERT INTO items_student (student_id, item_id) VALUES (3, 2);
INSERT INTO items_student (student_id, item_id) VALUES (3, 3);
INSERT INTO items_student (student_id, item_id) VALUES (4, 2);
INSERT INTO items_student (student_id, item_id) VALUES (4, 3);
INSERT INTO grades (student_id, item_id, description, grade) VALUES (1, 2, 'Násobilka', 2);
INSERT INTO grades (student_id, item_id, description, grade) VALUES (2, 1, 'Slovíčka', 3);
INSERT INTO grades (student_id, item_id, description, grade) VALUES (3, 3, 'Dějiny 15. století', 1);
INSERT INTO grades (student_id, item_id, description, grade) VALUES (4, 2, 'Zlomky', 5);

SELECT students.first_name, students.second_name, items.item_name ,grades.grade FROM students
JOIN grades ON students.student_id = grades.student_id
JOIN items ON items.item_id = grades.item_id;



	