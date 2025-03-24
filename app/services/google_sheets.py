from googleapiclient.discovery import build
from app.services.google_auth import get_credentials

def fetch_candidate_data():
    """
    Connects to Google Sheets using OAuth credentials and retrieves candidate data.
    """
    creds = get_credentials()
    service = build("sheets", "v4", credentials=creds)
    spreadsheet_id = "1TPntAcoFPZVCFp-4kYgnqcaWGn5BGeuadU0okc6yWvs"
    range_name = "Sheet1!A1:D10"
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get("values", [])
    
    candidates = []
    if values:
        header = values[0]
        for row in values[1:]:
            candidate = {header[i]: row[i] if i < len(row) else "" for i in range(len(header))}
            candidates.append(candidate)
    return candidates
