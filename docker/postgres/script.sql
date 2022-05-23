

insert into staff values(1001,'Andrew Ng',1000);
insert into staff values(1002,'Alan Pi',800);
insert into staff values(1003,'Nick Berger',700);
insert into staff values(1004,'Alan Pi',800);
insert into staff values(1005,'Andrew Pi',800);
insert into staff values(1006,'Vasya Pupkin',900);
insert into staff values(1007,'Mark Mark',850);
insert into staff values(1008,'Kim Jong-Un',800);


insert into class (id, id_staff, class_name) values (3001, 1001 ,'Biology');
insert into class (id, id_staff, class_name) values (3002, 1002,'Math');
insert into class (id, id_staff, class_name) values (3003, 1003,'Physics');
insert into class (id, id_staff, class_name) values (3004, 1004,'Literature');
insert into class (id, id_staff, class_name) values (3005, 1005,'English');


insert into weekday1 values (5001,'Monday');
insert into weekday1 values (5002,'Tuesday');
insert into weekday1 values (5003,'Wednesday');
insert into weekday1 values (5004,'Thursday');
insert into weekday1 values (5005,'Friday');



insert into lesson values (6001,'09:00','09:45');
insert into lesson values (6002,'09:50','10:35');
insert into lesson values (6003,'10:45','11:30');
insert into lesson values (6004,'11:45','12:30');
insert into lesson values (6005,'12:40','13:25');
insert into lesson values (6006,'14:00','14:45');


insert into section (id, id_staff, advisor) values (100, 1006, 'Vasya Pupkin');
insert into section (id, id_staff, advisor) values (200, 1007, 'Mark Mark');
insert into section (id, id_staff, advisor) values (300, 1008, 'Kim Jong-Un');



insert into student (id, id_section, name_student, roll_no, amount_fee, fee_date) values (01,100, 'Ola Kim', 1, 300, '20.01.21');
insert into student (id, id_section, name_student, roll_no, amount_fee, fee_date) values (02,100,'Misha Son', 2, 300,'21.01.21');
insert into student (id, id_section, name_student, roll_no, amount_fee, fee_date) values (03,100,'Bobby Wax', 3, 300, '21.01.21');
insert into student (id, id_section, name_student, roll_no, amount_fee, fee_date) values (04,200,'Harvey Specter', 4, 300,'20.01.21');
insert into student (id, id_section, name_student, roll_no, amount_fee, fee_date) values (05,200,'Donna Paulsen', 5, 300,'22.01.21');
insert into student (id, id_section, name_student, roll_no, amount_fee, fee_date) values (06,200,'Louis Litt', 5, 300,'20.01.21');
insert into student (id, id_section, name_student, roll_no, amount_fee, fee_date) values (07,300,'Mike Ross', 6, 300,'23.01.21');
insert into student (id, id_section, name_student, roll_no, amount_fee, fee_date) values (08,300,'Rachel Zane', 7, 300,'24.01.21');
insert into student (id, id_section, name_student, roll_no, amount_fee, fee_date) values (09,300,'Robert Zane', 8, 300,'25.01.21');


insert into role1 values (1, 'teacher');
insert into role1 values (2, 'adviser');


insert into staff_roles (role1_id, staff_id) values (2, 1001);
insert into staff_roles (role1_id, staff_id) values (2, 1002);
insert into staff_roles (role1_id, staff_id) values (2, 1003);
insert into staff_roles (role1_id, staff_id) values (2, 1004);
insert into staff_roles (role1_id, staff_id) values (2, 1005);
insert into staff_roles (role1_id, staff_id) values (1, 1006);
insert into staff_roles (role1_id, staff_id) values (1, 1007);
insert into staff_roles (role1_id, staff_id) values (1, 1008);

insert into schedule (id, id_wk, id_lesson, id_class, id_section, id_staff, room_number) values (7001,5001,6001,3001,100,1001,250);
insert into schedule (id, id_wk, id_lesson, id_class, id_section, id_staff, room_number) values (7002,5002,6002,3001,100,1001,251);
insert into schedule (id, id_wk, id_lesson, id_class, id_section, id_staff, room_number) values (7003,5003,6003,3002,100,1001,252);
insert into schedule (id, id_wk, id_lesson, id_class, id_section, id_staff, room_number) values (7004,5004,6004,3003,100,1001,253);
insert into schedule (id, id_wk, id_lesson, id_class, id_section, id_staff, room_number) values (7005,5004,6002,3001,200,1002,254);
insert into schedule (id, id_wk, id_lesson, id_class, id_section, id_staff, room_number) values (7006,5005,6003,3003,200,1003,255);
insert into schedule (id, id_wk, id_lesson, id_class, id_section, id_staff, room_number) values (7007,5005,6004,3002,200,1001,256);
