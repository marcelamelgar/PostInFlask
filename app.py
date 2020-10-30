from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)





app = Flask(__name__)
with open ('data.json')as json_file:
  jsonfile = json.load(json_file)

def mensaje():
  mensaje = 'Registro de Estudiantes UFM'
  return "alert('" + mensaje + "')"

@app.route('/')
def index():
  template = env.get_template('index.html')
  return template.render(my_data = jsonfile['data'], headers = jsonfile['headers'])

@app.route('/Add', methods = ['GET', 'POST'])
def crear():
  if request.method == 'POST':
    _ID = request.form['ID']
    _estudiante = request.form['Estudiante']
    _carrera = request.form['Carrera']
    _image = request.form['image']
    _thumbnail = request.form['thumbnail']
    print (f'{_ID} {_estudiante} {_carrera} {_image} {_thumbnail}')

    jsonfile['data'].append({"ID":_ID, 'Estudiante': _estudiante, "Carrera": _carrera, "image":{"url":_image}, "thumbnail":{"url":_thumbnail}})
    return redirect(url_for('index'))
  template = env.get_template('form.html')
  return template.render()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)