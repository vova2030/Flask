from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html", title="Моя сторінка")

  
max_score = 10  
test_name = "Мої друзі"  
students = [  
    {"name": "Любомир", "score": 10},
    {"name": "Юра", "score": 8}, 
    {"name": "Володя", "score": 9},   
    {"name": "Віталій", "score": 4},
    {"name": "Денис", "score": 7},   
] 


@app.route("/results")
def results():
    context = {
        "title": "найкращі!!",
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }
    return render_template("results.html", **context)


if __name__ == "__main__":
    app.run(debug=True)