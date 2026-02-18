from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "mrtechnician_secret_key" # Required for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_report', methods=['POST'])
def submit_report():
    if request.method == 'POST':
        # Collect data from the form
        subject = request.form.get('subject')
        location = request.form.get('location')
        description = request.form.get('description')
        contact = request.form.get('contact')

        # Logic: Here you would save to a database (SQLAlchemy)
        print(f"New Report: {subject} at {location}")

        # Show a success message
        flash("तपाईंको उजुरी सफलतापूर्वक प्राप्त भयो। धन्यवाद!")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
