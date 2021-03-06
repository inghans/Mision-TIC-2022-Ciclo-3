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
    cursor= conn.execute("select `user`.id, `user`.nombre_usuario,`user`.telefono, `user`.correo, `user`.direccion from `user` inner join roles on (`user`.id_rol=roles.id) where `roles`.nombre='"+rol+"';")
    #for item in cursor:
    return cursor.fetchall() #item
    conn.close()

def PersonaGuardar(Nombre, Telefono, Correo, Direccion, Roles):
    conn= Conectar()    
    cursor= conn.execute("INSERT INTO user VALUES(NULL,?,?,?,?,?);",(Nombre,Telefono,Correo,Direccion,int(Roles)))
    #for item in cursor:  
    conn.commit()  
    conn.close()

def PersonaActualizar(Nombre, Telefono, Correo, Direccion,id):
    conn= Conectar()    
    cursor= conn.execute("update `user` set nombre_usuario='"+Nombre+"', telefono='"+Telefono+"', correo='"+Correo+"', direccion='"+Direccion+"' where id='"+id+"'")
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

def MateriaActualizar(Nombre,id):
    conn= Conectar()    
    cursor= conn.execute("update `materias` set nombre_materia='"+Nombre+"' where id='"+id+"'")
    #for item in cursor:  
    conn.commit()  
    conn.close()

# CRUD Cursos Programado por: HANS
def CursosGuardar(val):
    conn= Conectar()    
    cursor= conn.execute("INSERT INTO cursos VALUES(NULL,'"+val+"');")
    #for item in cursor:  
    conn.commit()  
    conn.close()

def CursosGuardarDetalle(idCurso,idMateria,IdDocente):
    conn= Conectar()    
    cursor= conn.execute("INSERT INTO curso_detalle VALUES(NULL,'"+idCurso+"','"+idMateria+"','"+IdDocente+"');")
    #for item in cursor:  
    conn.commit()  
    conn.close()

def CursoActualizar(Nombre,id):
    conn= Conectar()    
    cursor= conn.execute("update cursos set nombre_curso='"+Nombre+"' where id='"+id+"'")
    #for item in cursor:  
    conn.commit()  
    conn.close()

def CursosListar():
    conn= Conectar()    
    cursor= conn.execute("SELECT * FROM CURSOS")
    #for item in cursor:
    return cursor.fetchall() #item
    conn.close()

def CursosListarDetalle(val):
    conn= Conectar()    
    cursor= conn.execute("select materias.nombre_materia, `user`.nombre_usuario from curso_detalle inner join materias on (curso_detalle.id_materia=materias.id) inner join `user` on (curso_detalle.id_user=`user`.id) where curso_detalle.id_curso='"+val+"'")
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
def ActividadesListar(val):
    conn= Conectar()    
    cursor= conn.execute("select cursos.id as IdCurso, cursos.nombre_curso,`user`.nombre_usuario, materias.id as IdMateria, materias.nombre_materia from curso_detalle inner join cursos on (curso_detalle.id_curso=cursos.id)    inner join matriculas on (cursos.id=matriculas.id_curso) inner join `user` on (curso_detalle.id_user=`user`.id)    inner join materias on (curso_detalle.id_materia=materias.id) where curso_detalle.id_user='"+val+"'")
    #for item in cursor:
    return cursor.fetchall() #item
    conn.close()

def ActividadesListarMateria(IdCurso,IdMateria,IdDocente):
    conn= Conectar()    
    cursor= conn.execute("select actividades.id, actividades.nombre, actividades.nota from actividades inner join cursos on (actividades.id_curso=cursos.id) inner join materias on (actividades.id_materia=materias.id) where cursos.id='"+IdCurso+"' and materias.id='"+IdMateria+"' and actividades.id_docente='"+IdDocente+"'")
    #for item in cursor:
    return cursor.fetchall() #item
    conn.close()

def ActividadesGuardar(idCurso,idMateria,IdDocente,Nombre,Nota):
    conn= Conectar()    
    cursor= conn.execute("INSERT INTO actividades VALUES(NULL,'"+idCurso+"','"+idMateria+"','"+IdDocente+"','"+Nombre+"','"+Nota+"');")
    #for item in cursor:  
    conn.commit()  
    conn.close()

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


        
    
   

