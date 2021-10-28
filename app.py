from flask import Flask, render_template, request
import controller

app= Flask(__name__)

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

# programacion de RUTA cursos  realizado por: HANS
@app.route('/cursos',methods=('GET','POST'))
def cursos():
    if request.method == 'POST':
        cursos=request.form['txtCursos']
        r=controller.CursosGuardar(cursos)
        response=controller.CursosListar()        
        return render_template('cursos.html',lista=response)
    else:
        response=controller.MateriasListar()        
        return render_template('cursos.html',lista=response)

@app.route('/notas')
def notas():
    ejemplo='bienvenido Hans aqui puedes verificar tus notas'
    usuario='Hans'
    return render_template('notas.html',ejemplo=ejemplo,usuario=usuario)

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
        return ('Usuario y contraseña mala')


if __name__=='__main__':
    app.run(debug=True)