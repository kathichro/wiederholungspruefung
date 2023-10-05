BEGIN TRANSACTION;
DELETE from todo;
DELETE from list;
DELETE from sqlite_sequence;
INSERT INTO todo (complete, description) VALUES (TRUE, "Get some food");
INSERT INTO todo (description) VALUES ("Drive the bike more often");
INSERT INTO todo (description) VALUES ("Implement web app");
INSERT INTO todo (complete, description) VALUES (TRUE, "Call mom");
INSERT INTO todo (complete, description) VALUES (TRUE, "Clean up");
INSERT INTO list (name) VALUES ("Life");
INSERT INTO list (name) VALUES ("Work");
INSERT INTO list (name) VALUES ("Family");
INSERT INTO todo_list (todo_id, list_id) VALUES (1, 1);
INSERT INTO todo_list (todo_id, list_id) VALUES (2, 1);
INSERT INTO todo_list (todo_id, list_id) VALUES (2, 2);
INSERT INTO todo_list (todo_id, list_id) VALUES (3, 2);
INSERT INTO todo_list (todo_id, list_id) VALUES (4, 3);
INSERT INTO todo_list (todo_id, list_id) VALUES (5, 3);
COMMIT;