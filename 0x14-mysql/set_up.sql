-- Script that sets up 0x14-mysql tasks
-- Query that creates the MySQL server user holberton_user. Reminder: cat script.sql | mysql -hlocalhost -uroot -p
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost';
-- Query that sets password for. (Identify by fails with if not exists)
SET PASSWORD FOR 'holberton_user'@'localhost' = 'projectcorrection280hbtn';
-- Query that grants privilages to the user.
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
-- Shows grants for the user
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'holberton_user'@'localhost';
-- Query that creates the MySQL server user replica_user.
CREATE USER IF NOT EXISTS 'replica_user'@'%';
-- Query that sets password for. (Identify by fails with if not exists)
SET PASSWORD FOR 'replica_user'@'%' = 'replica';
-- Query that grants privilages to the user.
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- Shows grants for the user
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'replica_user'@'%';
-- Checks for correct permissions
SELECT user, Repl_slave_priv FROM mysql.user;
-- Querry to create the database tyrell_corp in your MySQL server if it does not exist.
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
-- Querry to create a table called "nexus6" in the current database in your MySQL server.
CREATE TABLE IF NOT EXISTS nexus6 (id INT,
name VARCHAR(256)
);
-- Querry to inserts a new row in the table "nexus6" of database provided.
INSERT INTO nexus6 (id, name) VALUES (1, "Leon");


-- mysql> SHOW MASTER STATUS;
-- +------------------+----------+--------------+------------------+-------------------+
-- | File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
-- +------------------+----------+--------------+------------------+-------------------+
-- | mysql-bin.000080 |     3327 | tyrell_corp  |                  |                   |
-- +------------------+----------+--------------+------------------+-------------------+
-- 1 row in set (0.00 sec)