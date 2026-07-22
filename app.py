from __future__ import annotations

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

DRAFT_ID = "RLY-D17"
DRAFTS: dict[str, dict[str, str]] = {}


def claim_payload() -> dict[str, str]:
    return {
        "amount": request.form.get("amount", "").strip(),
        "category": request.form.get("category", "").strip(),
        "project_code": request.form.get("project_code", "").strip(),
        "note": request.form.get("note", "").strip(),
    }


@app.get("/")
def index():
    return render_template("index.html", step="form", submitted=False, restored=False)


@app.post("/claims")
def submit_claim():
    claim = claim_payload()
    if not claim["amount"] or not claim["category"]:
        return render_template(
            "index.html",
            step="form",
            submitted=False,
            restored=False,
            error="Amount and category are required.",
            **claim,
        ), 400

    return redirect(url_for("confirmation"))


@app.post("/drafts")
def save_draft():
    claim = claim_payload()
    DRAFTS[DRAFT_ID] = claim
    return redirect(url_for("draft_list", saved="1"))


@app.get("/drafts")
def draft_list():
    return render_template(
        "index.html",
        step="drafts",
        submitted=False,
        saved=request.args.get("saved") == "1",
        draft=DRAFTS.get(DRAFT_ID),
        draft_id=DRAFT_ID,
    )


@app.get("/drafts/<draft_id>")
def restore_draft(draft_id: str):
    draft = DRAFTS.get(draft_id)
    if draft is None:
        return redirect(url_for("draft_list"))

    restored = {**draft, "category": ""}
    return render_template(
        "index.html",
        step="form",
        submitted=False,
        restored=True,
        draft_id=draft_id,
        **restored,
    )


@app.get("/confirmation")
def confirmation():
    return render_template("index.html", step="confirmed", submitted=True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4183, debug=False)
