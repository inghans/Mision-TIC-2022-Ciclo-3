import sqlite3
from sqlite3 import Error
import mysql.connector

def Conectar():
    # Establecido una ruta fisica para la BDD
    #conexion= sqlite3.connect("D:\\DATABASES\\bdd.db")
    conexion= sqlite3.connect("C:\\GIT\\Mision-TIC-2022-Ciclo-3\\ciclo3db.db")
    #conexion=mysql.connector()
    return conexion

def Ingreso(usuario, password):    
    conn= Conectar()
    cursor= conn.execute("SELECT roles.nombre FROM login INNER JOIN `user` ON (login.id_user=`user`.id)	INNER JOIN roles ON (`user`.id_rol= roles.id) WHERE login.user=? AND login.pass=?;",(usuario,password))
    #for item in cursor:
    return cursor.fetchone() #item
    conn.close()        
    
   

