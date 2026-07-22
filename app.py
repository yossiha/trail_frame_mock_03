from __future__ import annotations

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", submitted=False)


@app.post("/claims")
def submit_claim():
    amount = request.form.get("amount", "").strip()
    category = request.form.get("category", "").strip()
    if not amount or not category:
        return render_template(
            "index.html",
            submitted=False,
            error="Amount and category are required.",
            amount=amount,
            category=category,
        ), 400
    return redirect(url_for("confirmation"))


@app.get("/confirmation")
def confirmation():
    return render_template("index.html", submitted=True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4183, debug=False)
