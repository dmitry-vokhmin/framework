--
-- ���� ������������ � ������� SQLiteStudio v3.1.1 � �� ��� 26 15:03:59 2018
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: person
DROP TABLE IF EXISTS person;
CREATE TABLE person (idperson INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, lastname VARCHAR (32), firstname VARCHAR (32));
INSERT INTO person (idperson, lastname, firstname) VALUES (1, 'Ivanov', 'Ivan');
INSERT INTO person (idperson, lastname, firstname) VALUES (2, 'Borisov', 'Boris');
INSERT INTO person (idperson, lastname, firstname) VALUES (3, 'Romanov', 'Roman');
INSERT INTO person (idperson, lastname, firstname) VALUES (4, 'Igorev', 'Igor');
INSERT INTO person (idperson, lastname, firstname) VALUES (5, 'Fedorov', 'Fedor');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
