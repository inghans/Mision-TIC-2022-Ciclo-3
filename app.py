from re import T
from flask import Flask, render_template, request, session
import controller, os

app= Flask(__name__)
app.secret_key= os.urandom(32)

@app.route('/')
def login():
    resultado='invisible'
    return render_template('login.html',resultado=resultado)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/estudiantes')
def estudiantes():
    response=controller.DatosUsuarios('ESTUDIANTE')
    return render_template('estudiantes.html',lista=response)

@app.route('/docentes')
def docentes():
    response=controller.DatosUsuarios('DOCENTE')
    return render_template('docentes.html',lista=response)

# programacion de RUTA ESTUDIANTE por DOCENTE realizado por:Lerkis
@app.route('/docente_estudiante')
def docente_estudiante():
    response=controller.DatosUsuarios('ESTUDIANTE')
    return render_template('docente_estudiante.html',lista=response)

# programacion de RUTA MATRICULAS realizado por: LERKIS
@app.route('/matriculas',methods=('GET','POST'))
def matriculas():
    if request.method == 'POST':
        idCurso=request.form.get('cboCurso')
        idEstudiante=request.form.get('cboEstudiante')        
        r=controller.MatriculaGuardar(idCurso,idEstudiante)
    responseCurso=controller.CursosListar()        
    responseEstudiante=controller.PersonaListar('ESTUDIANTE')
    response=controller.MatriculaListar()        
    return render_template('matriculas.html',listaCurso=responseCurso, listaEstudiante=responseEstudiante,lista=response)

# programacion de RUTA NOTICIAS  realizado por: LERKIS
@app.route('/noticias',methods=('GET','POST'))
def noticias():
    if request.method == 'POST':
        Encabezado=request.form['txtEncabezado']
        Descripcion=request.form['txtDescripcion']
        Fecha=request.form['dtFecha']
        r=controller.NoticiaGuardar(Encabezado,Descripcion, Fecha)
        response=controller.NoticiaListar()        
        return render_template('noticias.html',lista=response)
    else:
        response=controller.NoticiaListar()        
        return render_template('noticias.html',lista=response)

# programacion de RUTA personas  realizado por: LERKIS
@app.route('/personas',methods=('GET','POST'))
def personas():
    if request.method == 'POST':
        Nombre=request.form['txtNombre']
        Telefono=request.form['txtTelefono']
        Direccion=request.form['txtDireccion']
        Correo=request.form['txtCorreo']
        Roles=request.form.get('cboRol')   
        r=controller.PersonaGuardar(Nombre,Telefono,Correo, Direccion, Roles)
    response=controller.RolesListar()        
    return render_template('personas.html',lista=response)

# programacion de RUTA EDITAR ESTUDIANTE  realizado por: LERKIS
@app.route('/estudiantes_editar',methods=('GET','POST'))
def EstudiantesEditar():
    if request.method == 'POST':
        editar=request.form['txtEditar']
        IdEstudiante=request.form['txtIdEstudiante']
        if editar=='1':            
            Nombre=request.form['txtNombre']
            Telefono=request.form['txtTelefono']
            Direccion=request.form['txtDireccion']
            Correo=request.form['txtCorreo']                        
            return render_template('estudiantes_editar.html',id=IdEstudiante,Nombre=Nombre, Telefono=Telefono,Direccion=Direccion,Correo=Correo)        
        else:                                    
            Nombre=request.form['txtNombre']
            Telefono=request.form['txtTelefono']
            Direccion=request.form['txtDireccion']
            Correo=request.form['txtCorreo']
            r=controller.PersonaActualizar(Nombre,Telefono,Correo, Direccion,IdEstudiante)
            response=controller.DatosUsuarios('ESTUDIANTE')
            return render_template('estudiantes.html',lista=response)

# programacion de RUTA EDITAR CURSO  realizado por: LERKIS
@app.route('/cursos_editar',methods=('GET','POST'))
def CursoEditar():
    if request.method == 'POST':
        editar=request.form['txtEditar']
        IdCurso=request.form['txtIdCurso']
        if editar=='1':            
            Nombre=request.form['txtNombre']            
            return render_template('cursos_editar.html',id=IdCurso,Nombre=Nombre)        
        else:                                    
            Nombre=request.form['txtNombre']            
            r=controller.CursoActualizar(Nombre,IdCurso)
            response=controller.CursosListar()        
            return render_template('cursos.html',lista=response)

# programacion de RUTA CURSO DETALLE  realizado por: LERKIS
@app.route('/cursos_detalle',methods=('GET','POST'))
def CursoDetalle():
    if request.method == 'POST':
        editar=request.form['txtEditar']
        IdCurso=request.form['txtIdCurso']        
        if editar=='1':
            NombreCurso=request.form['txtNombre']
            listaMaterias=controller.MateriasListar()
            listaDocentes=controller.DatosUsuarios('DOCENTE')
            lista=controller.CursosListarDetalle(IdCurso)
            return render_template('cursos_detalle.html',id=IdCurso,nombre=NombreCurso,listaMaterias=listaMaterias,listaDocentes=listaDocentes,lista=lista)        
        else:
            idMateria=request.form['cboMaterias']
            IdDocente=request.form['cboDocentes']
            r=controller.CursosGuardarDetalle(IdCurso,idMateria,IdDocente)
            response=controller.CursosListar()
            return render_template('cursos.html',lista=response)
            
        

# programacion de RUTA EDITAR ESTUDIANTE  realizado por: Gustavo and Hans
@app.route('/docentes_editar',methods=('GET','POST'))
def DocentesEditar():
    if request.method == 'POST':
        editar=request.form['txtEditar']
        IdDocente=request.form['txtIdDocente']
        if editar=='1':            
            Nombre=request.form['txtNombre']
            Telefono=request.form['txtTelefono']
            Direccion=request.form['txtDireccion']
            Correo=request.form['txtCorreo']                        
            return render_template('docentes_editar.html',id=IdDocente,Nombre=Nombre, Telefono=Telefono,Direccion=Direccion,Correo=Correo)        
        else:                                    
            Nombre=request.form['txtNombre']
            Telefono=request.form['txtTelefono']
            Direccion=request.form['txtDireccion']
            Correo=request.form['txtCorreo']
            r=controller.PersonaActualizar(Nombre,Telefono,Correo, Direccion,IdDocente)
            response=controller.DatosUsuarios('DOCENTE')
            return render_template('docentes.html',lista=response) 

# programacion de RUTA materias  realizado por: LERKIS
@app.route('/materias',methods=('GET','POST'))
def materias():
    if request.method == 'POST':
        materia=request.form['txtMateria']
        r=controller.MateriaGuardar(materia)
        response=controller.MateriasListar()        
        return render_template('materias.html',lista=response)
    else:
        response=controller.MateriasListar()        
        return render_template('materias.html',lista=response)

# programacion de RUTA EDITAR ESTUDIANTE  realizado por: Gustavo, Hans and Alex
@app.route('/materias_editar',methods=('GET','POST'))
def MateriaEditar():
    if request.method == 'POST':
        editar=request.form['txtEditar']
        IdMateria=request.form['txtIdMateria']
        if editar=='1':            
            Nombre=request.form['txtNombre']                      
            return render_template('materias_editar.html',id=IdMateria,Nombre=Nombre)        
        else:                                    
            Nombre=request.form['txtNombre']
            r=controller.MateriaActualizar(Nombre,IdMateria)
            response=controller.MateriasListar()
            return render_template('materias.html',lista=response)


# programacion de RUTA cursos  realizado por: HANS
@app.route('/cursos',methods=('GET','POST'))
def cursos():
    if request.method == 'POST':
        curso=request.form['txtCurso']
        r=controller.CursosGuardar(curso)
        response=controller.CursosListar()        
        return render_template('cursos.html',lista=response)
    else:
        response=controller.CursosListar()        
        return render_template('cursos.html',lista=response)

@app.route('/notas')
def notas():
    ejemplo='bienvenido Hans aqui puedes verificar tus notas'
    usuario='Hans'
    return render_template('notas.html',ejemplo=ejemplo,usuario=usuario)

# programacion de RUTA ACTIVIDADES ralizado por: LERKIS
@app.route('/actividades')
def Actividades():
    response=controller.ActividadesListar(str(session['idUser']))
    return render_template('actividades.html',lista=response)

@app.route('/actividades_crear',methods=('GET','POST'))
def ActividadesCrear():
    if request.method == 'POST':
        editar=request.form['txtEditar']
        IdCurso=request.form['txtIdCurso']        
        IdMateria=request.form['txtIdMateria']        
        idUser=session['idUser']
        if editar=='1':
            NombreCurso=request.form['txtNombreCurso']
            NombreMateria=request.form['txtNombreMateria']
            response=controller.ActividadesListarMateria(IdCurso,IdMateria,str(idUser))
            return render_template('actividades_crear.html',IdCurso=IdCurso,IdMateria=IdMateria,idUser=idUser,NombreCurso=NombreCurso,NombreMateria=NombreMateria,lista=response)        
        else:                                    
            Nombre=request.form['txtNombre']
            Descripcion=request.form['txtDescripcion']            
            r=controller.ActividadesGuardar(IdCurso,IdMateria,str(idUser),Nombre,Descripcion)
            response=controller.ActividadesListar(str(session['idUser']))
            return render_template('actividades.html',lista=response)   

@app.route('/actividades_notas',methods=('GET','POST'))
def ActividadesNotas():
    response=controller.ActividadesListar(str(session['idUser']))
    return render_template('actividades.html',lista=response)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/sesion', methods=('GET','POST'))
def sesion():    
    if request.method == 'POST':
        usuario=request.form['user']
        clave=request.form['pass']        
        # inicio base de datos
        response=controller.Ingreso(usuario,clave)
        if response:
            #traemos el ID y ROL del LOGIN
            resultado=response[0]
            idUser=response[1]
            session['idUser'] = idUser
            session['NombreUser'] = response[2]
            usuario=response[2]            
            if resultado=='ESTUDIANTE':
                # enviamos a ruta estudiantes                
                return render_template('home_estudiantes.html',usuario=usuario)
            elif resultado=='DOCENTE':
                return render_template('home_docente.html',usuario= usuario)
            else:
                return render_template('home.html',usuario= usuario)
        else:
            resultado='visible'
            return render_template('login.html',resultado= resultado)        
            
    else:
        return ('Usuario y contrase??a mala')


if __name__=='__main__':
    app.run(debug=True)