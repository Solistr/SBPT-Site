from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__, template_folder='./pages/', static_folder='./pages/') 
app.secret_key = "gukV4&Ls6!"

def checkLanguage():
    if not "lang" in session:
        session["lang"] = "pt"
    return session["lang"]


@app.route("/")
def index():
    lang = checkLanguage()
    session["lastPage"] = "index"
    return render_template(lang + "/index.html")

@app.route("/setLanguage/<lang>")
def change_language(lang):
    if lang == "pt" or lang == "en":
        session["lang"] = lang
    return redirect(url_for(session["lastPage"]))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
