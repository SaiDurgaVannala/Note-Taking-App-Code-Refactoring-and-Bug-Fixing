from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary to store notes associated with user IP addresses
user_notes = {}

@app.route('/', methods=["GET", "POST"])
def index():
    user_ip = request.remote_addr  # Get user's IP address

    if request.method == "POST":
        note = request.form.get("note")
        if note:
            if user_ip not in user_notes:
                user_notes[user_ip] = []  # Initialize notes list for the user

            user_notes[user_ip].append(note)

    return render_template("home.html", notes=user_notes.get(user_ip, []))

if __name__ == '__main__':
    app.run(debug=True)

