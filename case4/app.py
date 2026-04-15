# Flask вместо Delphi/IIS, причины в README.MD
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB = "tours.db"


def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tours (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            country TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT
        )
    """)
    cur = conn.execute("SELECT COUNT(*) FROM tours")
    if cur.fetchone()[0] == 0:
        conn.execute("INSERT INTO tours (title, country, price, description) VALUES (?, ?, ?, ?)",
                     ("Анталья все включено", "Турция", 85000, "10 дней отдыха на море"))
        conn.execute("INSERT INTO tours (title, country, price, description) VALUES (?, ?, ?, ?)",
                     ("Пхукет 12 дней", "Таиланд", 110000, "Пляжи и экскурсии"))
    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db()
    tours = conn.execute("SELECT * FROM tours ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", tours=tours)


@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        title = request.form["title"]
        country = request.form["country"]
        price = float(request.form["price"])
        desc = request.form.get("description", "")
        conn = get_db()
        conn.execute("INSERT INTO tours (title, country, price, description) VALUES (?, ?, ?, ?)",
                     (title, country, price, desc))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    return render_template("new.html")


@app.route("/<int:tid>")
def view(tid):
    conn = get_db()
    tour = conn.execute("SELECT * FROM tours WHERE id = ?", (tid,)).fetchone()
    conn.close()
    return render_template("view.html", tour=tour)


@app.route("/<int:tid>/delete", methods=["POST"])
def delete(tid):
    conn = get_db()
    conn.execute("DELETE FROM tours WHERE id = ?", (tid,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
