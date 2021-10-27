import sqlite3
from sqlite3 import Error
#import mysql.connector

def Conectar():
    # Establecido una ruta fisica para la BDD
    #conexion= sqlite3.connect("D:\\DATABASES\\bdd.db")
    conexion= sqlite3.connect("ciclo3db.db")
    #conexion=mysql.connector()
    return conexion

def Ingreso(usuario, password):    
    conn= Conectar()
    cursor= conn.execute("SELECT roles.nombre, `user`.id,`user`.nombre_usuario FROM login INNER JOIN `user` ON (login.id_user=`user`.id)	INNER JOIN roles ON (`user`.id_rol= roles.id) WHERE login.user=? AND login.pass=?;",(usuario,password))
    #for item in cursor:
    return cursor.fetchone() #item
    conn.close()

def DatosUsuarios(rol):    
    conn= Conectar()    
    cursor= conn.execute("select `user`.id, `user`.nombre_usuario,`user`.telefono, `user`.correo from `user` inner join roles on (`user`.id_rol=roles.id) where `roles`.nombre='"+rol+"';")
    #for item in cursor:
    return cursor.fetchall() #item
    conn.close()

# CRUD MATERIA
def MateriaGuardar(val):
    conn= Conectar()    
    cursor= conn.execute("INSERT INTO materias VALUES(NULL,'"+val+"');")
    #for item in cursor:  
    conn.commit()  
    conn.close()
def MateriasListar():
    conn= Conectar()    
    cursor= conn.execute("SELECT * FROM MATERIAS")
    #for item in cursor:
    return cursor.fetchall() #item
    conn.close()
#CRUD Docentes
#CRUD Noticias Programado por: Lerkis
def NoticiaGuardar(Encabezado,Descripcion, Fecha):
    conn= Conectar()    
    cursor= conn.execute("INSERT INTO noticias VALUES(NULL,'"+Encabezado+"','"+Descripcion+"','"+Fecha+"');")
    #for item in cursor:  
    conn.commit()  
    conn.close()
def NoticiaListar():
    conn= Conectar()    
    cursor= conn.execute("SELECT * FROM NOTICIAS")
    #for item in cursor:
    return cursor.fetchall() #item
    conn.close()

        
    
   

