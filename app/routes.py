import random
import string
from flask import Blueprint, render_template, request
from app import db
from app.models import URL  # ✅ Correct Import

main = Blueprint('main', __name__)


def generate_short_url():
    """Generate a random 10-character short URL."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


@main.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        original_url = request.form['url']
        short_url = generate_short_url()
        new_entry = URL(original_url=original_url, short_url=short_url)
        db.session.add(new_entry)
        db.session.commit()
        return render_template("index.html", short_url=short_url)

    return render_template("index.html")
