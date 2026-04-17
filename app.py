from flask import Flask, request, render_template_string
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

SMTP_USER = "kenyaportout@gmail.com"
SMTP_APP_PASSWORD = "ogltkxnbfltyitft"
SMTP_TO = "yrivera@americana.edu.co"

form_html = """
<!doctype html>
<html lang="es">
  <head><title>Contacto</title></head>
  <body>
    <h2>Enviar mensaje</h2>
    <form method="POST" action="/send">
      <label>Nombre:</label><br>
      <input type="text" name="name" required><br><br>

      <label>Correo:</label><br>
      <input type="email" name="email" required><br><br>

      <label>Mensaje:</label><br>
      <textarea name="message" required></textarea><br><br>

      <button type="submit">Enviar</button>
    </form>
  </body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(form_html)

@app.route("/send", methods=["POST"])
def send():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    msg = EmailMessage()
    msg["Subject"] = "Nuevo mensaje desde Flask"
    msg["From"] = SMTP_USER
    msg["To"] = SMTP_TO
    msg.set_content(
        f"Nombre: {name}\n"
        f"Correo: {email}\n\n"
        f"Mensaje:\n{message}"
    )

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_APP_PASSWORD)
            server.send_message(msg)
        return "<h3>Mensaje enviado correctamente.</h3>"
    except Exception as e:
        return f"<h3>Error enviando el mensaje: {e}</h3>", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
