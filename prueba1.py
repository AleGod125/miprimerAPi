from flask import Flask

app = Flask(__name__)

nombres_personas = ["Alejandro", "Juan", "Carlos", "Ana", "Pedro"]

@app.route('/personas')
def obtener_personas():
    return nombres_personas

if __name__ == '__main__':
    app.run(debug=True)
