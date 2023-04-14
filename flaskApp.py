from flask import Flask, render_template, request

app = Flask(__name__)

# Function to read in details our name
def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message)

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/next", methods=['GET', 'POST'])
def questionForm():
    name = None
    if request.method =='POST':
        name = request.form['name']
    return render_template("page2.html", name = name)

if __name__ == '__main__':
    app.run(debug=True)
    