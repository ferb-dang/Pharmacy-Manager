INSERT INTO tbl_permissions (id, title, description)
VALUES 
('1','read','read staff'),
('2','create','create staff'),
('3','update','update staff'),
('4','delete','delete staff'),
('5','read','read medicine'),
('6','create','create medicine'),
('7','update','update medicine'),
('8','delete','delete medicine'),
('9','assign role','admin can assign role');

INSERT INTO tbl_roles (id, title, description, slug)
VALUES 
('1','admin','full roles, can do any thing',''),
('2','manager','can manage staff and medicines',''),
('3','staff','can manage medicines',''),
('4','user','can CRUD medicines in order','');

INSERT INTO tbl_role_permissions (roles_id,permissions_id)
VALUES 
('1','1'),
('1','2'),
('1','3'),
('1','4'),
('1','5'),
('1','6'),
('1','7'),
('1','8'),
('1','9'),
('2','1'),
('2','2'),
('2','3'),
('2','4'),
('2','5'),
('2','6'),
('2','7'),
('2','8'),
('3','5'),
('3','6'),
('3','7'),
('3','8'),
('4','5'),
('4','6'),
('4','7'),
('4','8');

INSERT INTO tbl_users (role_id, user_name,password,name,gender,date_of_birth,email,address,phone_numbers)
VALUES
('1','admin','$2b$12$VoTmnFohfkzGnnFscDpM1uF5ALMlRcA4mcoUl7xsAM3Ppxhcrr9K.','Thắng','1','1999-06-07','thangdv@vmodev.com','Việt Nam','0936163984'),
('1','admin1','$2b$12$VoTmnFohfkzGnnFscDpM1uJpSyAB9jVx4xUrfeEKWcyGBrWY/WCjC','Nam','1','1999-06-07','example@vmodev.com','Việt Nam','012345678');

INSERT INTO tbl_medicines (name, slug,medical_function,quantity,price,manufacture_date,expire_date,status)
VALUES
('vitamin A','','bo sung vitamin D','2000','1','2030-05-02','2022-04-03','out of stock'),
('vitamin C','','bo sung vitamin C','656','876321','2022-07-07','2022-04-03','available');

INSERT INTO tbl_orders (user_id, status,shipping_address,shipping_fee)
VALUES
('1','Dang Van Chuyen','Viet nam','1.000.000')