import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
    conn = mysql.connector.connect(
            host='Benjamin718.mysql.pythonanywhere-services.com',
            user='Benjamin718',
            password='r00t'
        )

except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print ('Existe un error en el nombre de usuario o la clave')
        else
            print(err)


cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `Benjamin718$flotaeldorado`;")

cursor.execute("CREATE DATABASE `Benjamin718$flotaeldorado`;")

cursor.execute("USE `Benjamin718$flotaeldorado`;")

#creando las tablas

TABLES = {}

#TABLES['productos'] = ('''
 #   CREATE TABLE `productos` (
  #  `id` int (11) NOT NULL AUTO_INCREMENT,
