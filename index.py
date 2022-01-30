# importing modules
from flask import Flask, render_template
# from flask_minify import minify

# declaring app name
app = Flask(__name__, template_folder='./src')

# making list of options
Operaciones = ["Suma (Adición)", "Resta (Sustracción)",
    "Multiplicación (Suma abreviada)", "División", "Potenciación", "Radicación"]

# defining home page Routes to Render
@app.route('/')
def home():

    # returning index.html and list
    # and length of list to html page
    return render_template("pages/home.html", len = len(Operaciones), Operaciones = Operaciones)

@app.route('/about', strict_slashes=False)
def about():
    return render_template("pages/about.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    # All parameters are opcional for run method
    app.run(host='0.0.0.0', port='5000', debug=True, use_reloader = True) # Default port: 5000
