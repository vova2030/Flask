from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html", title="Jinja and Flask")

  
max_score = 100   
test_name = "Python Challenge"  
students = [  
    {"name": "Любомир", "score": 100},
    {"name": "Юра", "score": 87}, 
    {"name": "Володя", "score": 92},   
    {"name": "Віталій", "score": 40},
    {"name": "Денис", "score": 75},   
] 


@app.route("/results")
def results():
    context = {
        "title": "Results",
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }
    return render_template("results.html", **context)


if __name__ == "__main__":
    app.run(debug=True)