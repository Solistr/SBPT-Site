from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__, template_folder='./pages/', static_folder='./pages/') 
app.secret_key = "teste"

def checkLanguage():
    if not "lang" in session:
        session["lang"] = "pt"
    return session["lang"]


@app.route("/")
def index():
    lang = checkLanguage();
    return render_template(lang + "/index.html")

@app.route("/changeLanguage/")
def change_language():
    if session["lang"] == "pt":
        session["lang"] = "en"
    else:
        session["lang"] = "pt"
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
