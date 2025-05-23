from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from flask_session import Session 
import smtplib
from email.mime.text import MIMEText
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Send survey email
def send_mail(name, surname, education, gender, ai_models, daily_life_benefits):
    body = f"""
AI Survey Submission
---------------------
Name         : {name} {surname}
Education    : {education}
Gender       : {gender}

AI Models & Their Cons or Defects:
"""
    for model in ai_models:
        body += f" - {model['modelName']}: {model['cons']}\n"

    body += f"\nDaily Life Benefits:\n{daily_life_benefits}"

    msg = MIMEText(body)
    msg["Subject"] = "AI Survey"
    msg["From"] = "atomkalemdar@gmail.com"
    msg["To"] = "validation458@proton.me"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("atomkalemdar@gmail.com", "sbac mlxp dzgw sgmh")
        server.send_message(msg)

@app.route('/survey', methods=['POST'])
def submit_survey():
    data = request.json
    required_fields = ['name', 'surname', 'educationLevel', 'gender', 'genderValue', 'selectedAIModels', 'dailyLifeBenefits']

    # Validate incoming data
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        send_mail(
            name=data['name'],
            surname=data['surname'],
            education=data['educationLevel'],
            gender=data['gender'],
            ai_models=data['selectedAIModels'],
            daily_life_benefits=data['dailyLifeBenefits']
        )
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

app.secret_key = "your-strong-secret-key"
app.config["SESSION_TYPE"] = "filesystem"  
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_KEY_PREFIX"] = "oauth_"
Session(app)  

oauth = OAuth(app)

app.config['GOOGLE_CLIENT_ID'] = "395889624025-auvbub026chb33h5sqmooi3plmmpcs9o.apps.googleusercontent.com"
app.config['GOOGLE_CLIENT_SECRET'] = "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"
google = oauth.register(
    name='google',  
    client_id=app.config['GOOGLE_CLIENT_ID'],
    client_secret=app.config['GOOGLE_CLIENT_SECRET'],
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        'scope': 'openid email profile',
        'redirect_uri': 'http://localhost:5000/auth/google'
    }
)

users = {
    "user@example.com": "password123",
    "1234567890": "mypassword"
}

@app.route('/', methods=['GET', 'POST'])
def login():
    """Handles manual login with email/password"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = {"email": username}
            return jsonify({"status": "success", "message": "Login successful"}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid email/phone number or password"}), 401
    
    return jsonify({"status": "error", "message": "Method not allowed"}), 405

@app.route('/login/google')
def login_google():
    """Redirect user to Google for authentication"""
    return google.authorize_redirect(url_for('google_auth', _external=True))

@app.route('/auth/google', methods=['POST'])
def google_auth():
    """Handles Google OAuth callback for Flutter app"""
    try:
        token = google.authorize_access_token()
        user_info = google.get('https://www.googleapis.com/oauth2/v3/userinfo').json()
        session['user'] = user_info
        return jsonify({
            "status": "success",
            "user": user_info
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

@app.route('/success')
def success():
    """Displays success message after login with a Logout button"""
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    
    return f"""
        <h2>Login Successful</h2>
        <p>Welcome, {user.get('email', 'Guest')}!</p>
        <br>
        <a href="{url_for('logout')}">
            <button style="padding: 10px; font-size: 16px; cursor: pointer;">Logout</button>
        </a>
    """

@app.route('/logout')
def logout():
    """Logs out user"""
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
