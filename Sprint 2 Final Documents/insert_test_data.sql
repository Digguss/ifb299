# The password for all of the accounts is 'test001'.
INSERT INTO smartcitydatabase.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) 
	VALUES ('1', 'pbkdf2_sha256$30000$F2b8rCeq0HNm$EJMT8DhnFaoXhreDtiiaDmhQj33siSnWRpJpRUjCpGM=', '2017-10-06 06:45:40.474000', '0', 'teststudent1', 'Student', 'Tester', 'student@student.com', '0', '1', '2017-10-06 06:44:16.238000'),
		   ('2', 'pbkdf2_sha256$30000$F2b8rCeq0HNm$EJMT8DhnFaoXhreDtiiaDmhQj33siSnWRpJpRUjCpGM=', '2017-10-06 06:45:47.127000', '0', 'testtourist1', 'Tourist', 'Tester', 'tourist@tourist.com', '0', '1', '2017-10-06 06:44:48.565000'),
		   ('3', 'pbkdf2_sha256$30000$F2b8rCeq0HNm$EJMT8DhnFaoXhreDtiiaDmhQj33siSnWRpJpRUjCpGM=', '2017-10-06 06:46:16.463000', '0', 'testbusiness1', 'Business', 'Tester', 'businessman@business.com', '0', '1', '2017-10-06 06:45:28.121000');

INSERT INTO smartcitydatabase.auth_group (id, name)
	VALUES ('1', 'aBusiness'), 
		   ('2', 'aTourist'),
		   ('3', 'aStudent');

INSERT INTO smartcitydatabase.regpage_webuser (id, phonenumber, address, user_id)
	VALUES ('1', '0411111111', '1 Student St, Studenttown', '1'),
		   ('2', '0422222222', '2 Tourist St, Touristville', '2'),
		   ('3', '0433333333', '3 Business Rd, Businesscity', '3');

INSERT INTO smartcitydatabase.auth_user_groups (id, user_id, group_id)
	VALUES ('1', '1', '3'),
		   ('2', '2', '2'),
		   ('3', '3', '1');


INSERT INTO smartcitydatabase.informationpage_college (id, name, description, phonenumber, address, email, image)
	VALUES ('1', 'Brisbane College', 'A college', '0756472655', '101 College Way, Brisbane', 'briscollege@learning.edu.au', 'storage/Cafes_on_campus.jpg'),
		   ('2', 'QUT', 'A university for the real world.', '0798765432', '5 QUT St, Brisbane', 'admin@qut.edu.au', 'storage/QUT-Picture-Insert-1_1.png');

INSERT INTO smartcitydatabase.informationpage_city_park (id, name, description, phonenumber, address, email, image)
	VALUES ('1', 'Brisbane Park', 'A park', '0712317678', '5 Park Lane, Brisbane', 'parks@brisbanecitycouncil.com.au', 'storage/910x380_city_botanic_gardens_master_plan.jpg'),
		   ('2', 'Botaincal Gardens', 'Another Park', '0787926457', '9 Gardens Pde, Brisbane', 'botgardens@bris.com.au', 'storage/RSPSpectacleGarden_wide.jpg');

INSERT INTO smartcitydatabase.hotel (id, name, description, phonenumber, address, email, image)
	VALUES ('1', 'Grand Central', 'Is a hotel', '0761621928', '1 Central St, Brisbane', 'bookings@grandcentral.com', 'storage/bnedt_main01.jpg'),
		   ('2', 'Amber Inn', 'Another Hotel', '0731211111', '8 Duck St, Brisbane', 'amber@inn.com', 'storage/novotel-brisbane-airport.jpg');
           
INSERT INTO smartcitydatabase.informationpage_industrie (id, name, description, phonenumber, address, email, image)
	VALUES ('1', 'Big Industry Co.', 'An Industry', '0744444456', '1 Money Rd, Brisbane', 'sales@money.com.au', 'storage/Brisbane_Square_July_06.jpg'),
		   ('2', 'Fun Co.', 'Another industry', '0789783412', '22 Industry Ct, Brisbane', 'sales@fun.com.au', 'storage/westpac.jpg');

INSERT INTO smartcitydatabase.informationpage_library (id, name, description, phonenumber, address, email, image)
	VALUES ('1', 'Brisbane Library', 'A library', '0745671234', '1 Learning Way', 'libraries@brisbanecitycouncil.com.au', 'storage/021.jpg'),
		   ('2', 'Bookworm Library', 'Another Library', '0774839265', '55 Reading St, Brisbane', 'books@worm.com', 'storage/Millennium_Library_1.jpg');

INSERT INTO smartcitydatabase.informationpage_museum (id, name, description, phonenumber, address, email, image)
	VALUES ('1', 'Natural History Museum', 'A museum', '0711222999', '2 Kings Pde', 'enquiries@natmuseum.com', 'storage/Museum_of_Brisbane_57ff1cc377af1f7520ac1445_16X9.jpeg'),
		   ('2', 'Brisbane Museum', 'Another museum', '0782736599', '12 History Lane, Brisbane', 'museums@brisbanecitycouncil.com.au', 'storage/brisbane-museum.jpg');

INSERT INTO smartcitydatabase.informationpage_restaurant (id, name, description, phonenumber, address, email, image)
	VALUES ('1', 'Eat Here!', 'A restaurant', '0799988877', '1 Eat St, Brisbane', 'eat@here.com.au', 'storage/JV-4297-770x514.jpg'),
		   ('2', 'Yum', 'Another restaurant', '0738276453', '68 Food Pde, Brisbane', 'yum@restaurants.com', 'storage/Sake_Restaurant_Brisbane_PI.jpg');