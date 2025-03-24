from googleapiclient.discovery import build
from app.services.google_auth import get_credentials
import io
from googleapiclient.http import MediaIoBaseDownload

def download_resume(file_id):
    """
    Downloads a resume PDF from Google Drive using the file ID.
    Note: You may need to adjust permissions/sharing for the file.
    """
    creds = get_credentials()
    drive_service = build("drive", "v3", credentials=creds)
    
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")
    
    fh.seek(0)
    return fh.read()
