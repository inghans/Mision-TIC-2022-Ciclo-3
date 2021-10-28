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

#CRUD Persona Programado por: Lerkis
def DatosUsuarios(rol):    
    conn= Conectar()    
    cursor= conn.execute("select `user`.id, `user`.nombre_usuario,`user`.telefono, `user`.correo from `user` inner join roles on (`user`.id_rol=roles.id) where `roles`.nombre='"+rol+"';")
    #for item in cursor:
    return cursor.fetchall() #item
    conn.close()

def PersonaGuardar(Nombre, Telefono, Correo, Direccion, Roles):
    conn= Conectar()    
    cursor= conn.execute("INSERT INTO user VALUES(NULL,?,?,?,?,?);",(Nombre,Telefono,Correo,Direccion,int(Roles)))
    #for item in cursor:  
    conn.commit()  
    conn.close()

def PersonaListar(rol):
    conn= Conectar()    
    cursor= conn.execute("select `user`.id, `user`.nombre_usuario from `user` inner join roles on (`user`.id_rol=roles.id) where roles.nombre='"+rol+"';")
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

# CRUD Cursos Programado por: HANS
def CursosGuardar(val):
    conn= Conectar()    
    cursor= conn.execute("INSERT INTO cursos VALUES(NULL,'"+val+"');")
    #for item in cursor:  
    conn.commit()  
    conn.close()
def CursosListar():
    conn= Conectar()    
    cursor= conn.execute("SELECT * FROM CURSOS")
    #for item in cursor:
    return cursor.fetchall() #item
    conn.close()

#CRUD roles Programado por:Lerkis
def RolesListar():
    conn= Conectar()    
    cursor= conn.execute("SELECT * FROM ROLES")
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

#CRUD Matriculas Programado por: Lerkis
def MatriculaGuardar(idCurso,idMatricula):
    conn= Conectar()    
    cursor= conn.execute("INSERT INTO matriculas VALUES(NULL,'"+idCurso+"','"+idMatricula+"');")
    #for item in cursor:  
    conn.commit()  
    conn.close()

def MatriculaListar():
    conn= Conectar()    
    cursor= conn.execute("select matriculas.id, cursos.nombre_curso,`user`.nombre_usuario from matriculas inner join cursos on (matriculas.id_curso=cursos.id) inner join `user` on (matriculas.id_estudiante=`user`.id)")
    #for item in cursor:
    return cursor.fetchall() #item
    conn.close()


        
    
   

