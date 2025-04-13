from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from flask_session import Session 
import os
import base64
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Gmail API scope
GMAIL_SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Authenticate with Gmail API
def get_gmail_service():
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', GMAIL_SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', GMAIL_SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

# Create raw email message
def create_message(sender, to, subject, body_text):
    message = MIMEText(body_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': encoded_message}

# Send survey email
def send_mail(name, surname, birth, education, city, gender, ai_defects, freetext):
    body = f"""
AI Survey Submission
---------------------
Name         : {name} {surname}
Birth Date   : {birth}
Education    : {education}
City         : {city}
Gender       : {gender}

AI Models Tried & Defects:
"""
    for item in ai_defects:
        body += f" - {item['model']}: {item['defect']}\n"

    body += f"\nBeneficial AI Use Case:\n{freetext}"

    msg = MIMEText(body)
    msg["Subject"] = "AI Survey"
    msg["From"] = "atomkalemdar@gmail.com"
    msg["To"] = "validation458@proton.me"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("atomkalemdar@gmail.com", "sbac mlxp dzgw sgmh")
        server.send_message(msg)

@app.route('/submit-survey', methods=['POST'])
def submit_survey():
    data = request.json
    required_fields = ['name', 'surname', 'birth', 'education', 'city', 'gender', 'ai_defects', 'freetext']

    # Validate incoming data
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        send_mail(
            name=data['name'],
            surname=data['surname'],
            birth=data['birth'],
            education=data['education'],
            city=data['city'],
            gender=data['gender'],
            ai_defects=data['ai_defects'],
            freetext=data['freetext']
        )
        return jsonify({"status": "success"}), 200
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
    client_kwargs={'scope': 'openid email profile'},
    userinfo_endpoint="https://www.googleapis.com/oauth2/v3/userinfo"
)

users = {
    "user@example.com": "password123",
    "1234567890": "mypassword"
}

@app.route('/', methods=['GET', 'POST'])
def login():
    """Handles manual login with email/password"""
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = {"email": username}
            return redirect(url_for('success'))
        else:
            error = "Invalid email/phone number or password."
    
    return render_template('login.html', error=error)

@app.route('/login/google')
def login_google():
    """Redirect user to Google for authentication"""
    return google.authorize_redirect(url_for('google_auth', _external=True))

@app.route('/auth/google')
def google_auth():
    """Handles Google OAuth callback"""
    token = google.authorize_access_token()
    user_info = google.get('https://www.googleapis.com/oauth2/v3/userinfo').json()
    session['user'] = user_info
    return redirect(url_for('success'))

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
