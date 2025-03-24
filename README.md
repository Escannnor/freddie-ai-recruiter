# Freddie AI Recruiter

Welcome to Freddie AI Recruiter – a project that automates parts of the recruitment process using Google APIs and OpenAI.

## What It Does
Freddie:
- Pulls candidate data from a Google Sheet.
- Downloads resumes from Google Drive.
- Uses OpenAI to score each candidate based on their resume and screening responses.
- Saves candidate info in an SQLite database.
- Sends an email to candidates who score above a set threshold.

## Tech Stack
- **Language:** Python 3.9+
- **Libraries:** Flask, SQLAlchemy, OpenAI, google-auth, google-auth-oauthlib
- **Database:** SQLite
- **Containerization:** Docker (optional)

## Getting Started
1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Escannnor/freddie-ai-recruiter.git
   cd freddie-ai-recruiter

2.**Set Up Your Environment:**

Create a virtual environment:
python -m venv venv

**Activate it:**

source venv/bin/activate

**Install dependencies:**

pip install -r requirements.txt

3 **.Configuration**

Copy the example environment file and add your OpenAI API key:

.env

Place your client_secret.json (Google OAuth credentials) in the project root.

**Database:**

The database (freddie.db) is created automatically when you run the app.

If you ever need to start fresh, just delete the file and run the app again.

Running Freddie

**Locally:**

Simply run:

python -m app.main

Freddie will pull the candidate data, process everything, store the results, and send emails where needed.

**Using Docker (Optional):**

If you prefer containerization:

docker build -t freddie-ai-recruiter .
docker run --env-file .env -p 8000:8000 freddie-ai-recruiter

LICENSE

This version has a more conversational tone while still providing all the necessary details. Feel free to adjust anything to better suit your style!
## License

This project is licensed under the MIT License.
