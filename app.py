from __future__ import annotations

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


def claim_payload() -> dict[str, str]:
    return {
        "amount": request.form.get("amount", "").strip(),
        "category": request.form.get("category", "").strip(),
        "project_code": request.form.get("project_code", "").strip(),
        "note": request.form.get("note", "").strip(),
    }


@app.get("/")
def index():
    return render_template("index.html", step="form", submitted=False)


@app.post("/claims/review")
def review_claim():
    claim = claim_payload()
    if not claim["amount"] or not claim["category"]:
        return render_template(
            "index.html",
            step="form",
            submitted=False,
            error="Amount and category are required.",
            **claim,
        ), 400

    return render_template(
        "index.html",
        step="review",
        submitted=False,
        **claim,
    )


@app.post("/claims/submit")
def submit_claim():
    claim = claim_payload()
    project_code = claim["project_code"]
    if project_code and not project_code.isalnum():
        return render_template(
            "index.html",
            step="review",
            submitted=False,
            error="Project code can only contain letters and numbers.",
            **claim,
        ), 400

    return redirect(url_for("confirmation"))


@app.get("/confirmation")
def confirmation():
    return render_template("index.html", step="confirmed", submitted=True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4183, debug=False)
