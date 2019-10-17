from flask import Flask, render_template

app = Flask(__name__)

# define routes

@app.route('/')
def index():
    #return "estas en el index"
    return render_template("index.html")






# server stuff

if __name__ == "__main__":
    app.run(debug=True)