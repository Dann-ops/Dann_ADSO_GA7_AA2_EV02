from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    # Capturamos los datos del formulario
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    
    # Por ahora, solo confirmamos la recepción
    return f"""
        <h1>¡Datos Recibidos!</h1>
        <p>Producto: {nombre}</p>
        <p>Cantidad: {cantidad}</p>
        <a href='/'>Volver al formulario</a>
    """

if __name__ == '__main__':
    app.run(debug=True)