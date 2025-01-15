import os
import requests
import json
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables (with defaults set directly in the script)
GITHUB_TOKEN = os.getenv("_GITHUB_TOKEN")
SMTP_PASSWORD = os.getenv("_SMTP_PASSWORD")
REPO_OWNER = os.getenv("_REPO_OWNER", "bw-gaming")  # Default: "bw-gaming"
REPO_NAME = os.getenv("_REPO_NAME", "bluewindow-toolkit-nodejs")  # Default: "bluewindow-toolkit-nodejs"

SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
EMAIL_SENDER = "monitoring@bluewindowltd.com"
EMAIL_RECEIVER = "release-notifications@bluewindowltd.com"

GITHUB_API_URL = "https://api.github.com"


def fetch_latest_release():
    """
    Fetch the latest release from the repository.
    """
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/releases/latest"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    print("Fetching the latest release from the repository...")
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Return the latest release data
    elif response.status_code == 404:
        print("No releases found. Will need to create one.")
        return None
    else:
        response.raise_for_status()


def create_release(tag_name):
    """
    Create a new release for the given tag.
    """
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/releases"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "tag_name": tag_name,
        "name": f"Release {tag_name}",
        "body": f"Automatically generated release for {tag_name}"
    }

    print(f"Creating a new release for the tag: {tag_name}...")
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Failed to create release. {response.status_code}: {response.text}")


def send_email(subject, body):
    """
    Send an email notification with the release details.
    """
    try:
        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"] = subject
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        print("Sending email notification...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, SMTP_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")


def main():
    try:
        # Fetch the latest release
        latest_release = fetch_latest_release()
        if latest_release:
            release_name = latest_release['name']
            release_tag = latest_release['tag_name']
            release_url = latest_release['html_url']
            release_body = latest_release['body']
            print(f"Existing release found: {release_name}")
        else:
            # No release exists, create one using the latest tag
            latest_tag = datetime.now().strftime('%Y%m%d')  # Auto-generate tag based on date
            release = create_release(latest_tag)
            release_name = release['name']
            release_tag = release['tag_name']
            release_url = release['html_url']
            release_body = release['body']
            print(f"New release created: {release_name}")

        # Prepare email content
        date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        expected_downtime = "0 minutes"  # Default expected downtime

        email_body = f"""
        Dear Team,

        A production release has started.

        **Details:**
        - **Release Name:** {release_name}
        - **Tag Name:** {release_tag}
        - **Release URL:** {release_url}
        - **Start Time:** {date_str}
        - **Expected Downtime:** {expected_downtime}

        **Release Notes:**
        {release_body}

        Regards,
        Automatic Notification System
        """
        send_email(f"Production Release Notification - {release_name}", email_body)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
