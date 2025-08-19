from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Use one consistent path for your CSV (same folder as this file)
CSV_PATH = os.path.join(os.path.dirname(__file__), "cafe-data.csv")

AM_PM_TIMES = [
    "6AM","7AM","8AM","9AM","10AM","11AM","12PM",
    "1PM","2PM","3PM","4PM","5PM","6PM","7PM","8PM","9PM","10PM","11PM"
]

def emoji_scale(symbol: str):
    return [("", "— Select —")] + [(symbol * i, symbol * i) for i in range(1, 6)]

class CafeForm(FlaskForm):
    # ✅ names match add.html exactly
    name = StringField('Name', validators=[DataRequired()])
    location = StringField('Location (URL)', validators=[DataRequired(), URL()])
    open_time = SelectField('Open', choices=[("", "— Select —")] + [(t, t) for t in AM_PM_TIMES],
                            validators=[DataRequired()])
    close_time = SelectField('Close', choices=[("", "— Select —")] + [(t, t) for t in AM_PM_TIMES],
                             validators=[DataRequired()])
    coffee = SelectField('Coffee', choices=emoji_scale("☕"), validators=[DataRequired()])
    wifi = SelectField('Wifi', choices=emoji_scale("💪"), validators=[DataRequired()])
    power = SelectField('Power', choices=emoji_scale("🔌"), validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_row = [
            form.name.data.strip(),
            form.location.data.strip(),
            form.open_time.data.strip(),
            form.close_time.data.strip(),
            form.coffee.data,
            form.wifi.data,
            form.power.data,
        ]

        # Ensure file ends with a newline before appending
        needs_newline = False
        if os.path.exists(CSV_PATH) and os.path.getsize(CSV_PATH) > 0:
            with open(CSV_PATH, 'rb') as fb:
                fb.seek(-1, os.SEEK_END)
                last_byte = fb.read(1)
                needs_newline = last_byte not in (b'\n', b'\r')

        with open(CSV_PATH, mode='a', newline='', encoding='utf-8') as f:
            if needs_newline:
                f.write('\n')
            csv.writer(f).writerow(new_row)

        flash("Cafe added!", "success")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open(CSV_PATH, newline='', encoding='utf-8') as f:
        rows = [r for r in csv.reader(f) if r]
    return render_template('cafes.html', cafes=rows)

if __name__ == '__main__':
    app.run(debug=True)
