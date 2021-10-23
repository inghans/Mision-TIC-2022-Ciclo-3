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
    return render_template('estudiantes.html')

@app.route('/docentes')
def docentes():
    return render_template('docentes.html')

@app.route('/materias')
def materias():
    return render_template('materias.html')

@app.route('/notas')
def notas():
    return render_template('notas.html')

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
            resultado=response[0]
            option=['DOCENTE','DOCENTEE','ADMIN']
            if resultado=='ESTUDIANTE':
                #return response
                return render_template('home.html',resultado= resultado)
            elif resultado=='DOCENTE':
                return render_template('prueba.html',resultado= resultado,option=option)
            else:
                return render_template('prueba.html',resultado= resultado)
        else:
            resultado='visible'
            return render_template('login.html',resultado= resultado)        
            
    else:
        return ('Usuario y contraseña mala')


if __name__=='__main__':
    app.run(debug=True)