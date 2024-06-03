-- Creates a MySQL server:
--database HBNB_MYSQL_DB
--HBNB_ENV:
--HBNB_MYSQL_USER: the username of your MySQL
--HBNB_MYSQL_PWD: the password of your MySQL
--HBNB_MYSQL_HOST: the hostname of your MySQL
--HBNB_MYSQL_DB: the database name of your MySQL
--HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)
-- Connect to the MySQL
database = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='your_root_password'
)
-- Create cursor to execute queries
cursor = database.cursor()
-- Create the database not exist
cursor.execute("CREATE DATABASE IF NOT EXISTS hbnb_dev_db")
-- add the user if not exist and add the password
cursor.execute("CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'")
-- Grant all PRIVILEGES
cursor.execute("GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'")
-- Grant SELECT privilege
cursor.execute("GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'")
-- Flush privileges to apply the changes
cursor.execute("FLUSH PRIVILEGES")
-- Close the cursor and db connection
cursor.close()
database.close()

