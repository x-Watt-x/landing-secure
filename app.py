from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Clé de session

# Définir ici le mot de passe à valider
PASSWORD = "monmotdepasse"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            session['authenticated'] = True
            return redirect(url_for('landing'))
        else:
            return render_template('login.html', error="Mot de passe incorrect.")
    return render_template('login.html')

@app.route('/landing')
def landing():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('landing.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
