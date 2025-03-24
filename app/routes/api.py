from flask import Flask, jsonify
from app.database.models import Candidate, SessionLocal

app = Flask(__name__)

@app.route("/rankings", methods=["GET"])
def get_rankings():
    """
    Returns a JSON list of candidate rankings.
    This example fetches candidates from the database.
    """
    db = SessionLocal()
    candidates = db.query(Candidate).order_by(Candidate.score.desc()).all()
    db.close()
   
    candidate_list = []
    for candidate in candidates:
        candidate_list.append({
            "name": candidate.name,
            "email": candidate.email,
            "score": candidate.score,
            "screening_answer": candidate.screening_answer,
            "resume_link": candidate.resume_link
        })
    
    return jsonify(candidate_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
