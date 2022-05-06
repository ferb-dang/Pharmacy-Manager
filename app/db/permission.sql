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

