# from app.database.models import init_db, SessionLocal, Candidate
# from app.services import google_sheets, google_drive, openai_service, email_service

# def extract_file_id(url):
#     """
#     Extract the file ID from a Google Drive URL.
#     Expected URL format:
#     https://drive.google.com/file/d/<file_id>/view?usp=sharing
#     """
#     parts = url.split("/")
#     file_id = ""
#     if "d" in parts:
#         try:
#             d_index = parts.index("d")
#             file_id = parts[d_index + 1]
#         except IndexError:
#             file_id = ""
#     return file_id

# def main():
#     init_db()

#     candidates = google_sheets.fetch_candidate_data()
#     print("Fetched candidate data:", candidates)
    

#     db = SessionLocal()
    
#     for candidate in candidates:
#         full_name = candidate.get("Full Name", "")
#         email = candidate.get("Email", "")
#         resume_link = candidate.get("Resume Link", "")
#         screening_answer = candidate.get("Screening Q1 (What are your key strengths?)", "")
        
#         file_id = extract_file_id(resume_link)
        
#         if file_id:
#             resume_content = google_drive.download_resume(file_id)
#             score = openai_service.evaluate_candidate(str(resume_content), screening_answer)
#             print(f"Candidate {full_name} scored {score}.")
            
#             new_candidate = Candidate(
#                 name=full_name,
#                 email=email,
#                 screening_answer=screening_answer,
#                 resume_link=resume_link,
#                 score=score
#             )
#             db.add(new_candidate)
#             db.commit()
#             db.refresh(new_candidate)
#             print(f"Stored candidate {new_candidate.name} with ID {new_candidate.id}.")
            
#             if score >= 70:
#                 email_service.send_email(email, full_name, score)
    
#     db.close()

# if __name__ == "__main__":
#     main()

from app.database.models import init_db, SessionLocal, Candidate
from app.services import google_sheets, google_drive, openai_service, email_service

def extract_file_id(url):
    """
    Extract the file ID from a Google Drive URL.
    Expected URL format:
    https://drive.google.com/file/d/<file_id>/view?usp=sharing
    """
    parts = url.split("/")
    file_id = ""
    if "d" in parts:
        try:
            d_index = parts.index("d")
            file_id = parts[d_index + 1]
        except IndexError:
            file_id = ""
    return file_id

def main():
    # Initialize the database (creates tables if they don't exist)
    init_db()

    candidates = google_sheets.fetch_candidate_data()
    print("Fetched candidate data:", candidates)

    db = SessionLocal()
    
    for candidate in candidates:
        full_name = candidate.get("Full Name", "")
        email = candidate.get("Email", "")
        resume_link = candidate.get("Resume Link", "")
        screening_answer = candidate.get("Screening Q1 (What are your key strengths?)", "")
        
        file_id = extract_file_id(resume_link)
        
        if file_id:
            resume_content = google_drive.download_resume(file_id)
            score = openai_service.evaluate_candidate(str(resume_content), screening_answer)
            print(f"Candidate {full_name} scored {score}.")

            # Check if candidate with this email already exists
            existing_candidate = db.query(Candidate).filter_by(email=email).first()
            if existing_candidate:
                print(f"Candidate with email {email} already exists. Skipping insertion.")
            else:
                new_candidate = Candidate(
                    name=full_name,
                    email=email,
                    screening_answer=screening_answer,
                    resume_link=resume_link,
                    score=score
                )
                db.add(new_candidate)
                db.commit()
                db.refresh(new_candidate)
                print(f"Stored candidate {new_candidate.name} with ID {new_candidate.id}.")
            
            if score >= 70:
                email_service.send_email(email, full_name, score)
    
    db.close()

if __name__ == "__main__":
    main()
