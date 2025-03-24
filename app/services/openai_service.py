import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
def evaluate_candidate(resume_content, screening_answer):
    max_length = 4000
    if len(resume_content) > max_length:
        resume_content = resume_content[:max_length]
    
    prompt = (
        f"Rate this candidate's fit for a marketing officer role based on the following information:\n\n"
        f"Resume (truncated if necessary): {resume_content}\n"
        f"Screening Answer: {screening_answer}\n\n"
        "Provide a score from 0 to 100. Return only the number without any additional text."
        # "Provide a score from 0 to 100. Return only the number."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that only returns a single number representing the candidate's suitability."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=10,
        temperature=0.0,
    )

    print("Raw OpenAI response:", response)
    
    score_text = response["choices"][0]["message"]["content"].strip()
    try:
        score = int(score_text)
    except ValueError:
        print(f"Failed to convert response '{score_text}' to int.")
        score = 0
    return score
