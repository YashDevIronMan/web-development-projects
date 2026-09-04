from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index' )
def index():
    return render_template('index.html')

@app.route('/table' , methods = ["POST"])
def table():
    number = request.form.get("number")
    if number == "" or not number.isdigit():
        return render_template("index.html")
    else:
         result = []
         n = int(number)

         for i in range(1,11):
          s = n * i
          result.append((f"{n}x{i} = {s}"))
         return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
