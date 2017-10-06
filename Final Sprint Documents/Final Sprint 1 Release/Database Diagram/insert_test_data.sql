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
