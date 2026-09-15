# === Stage 34: Add support for multiple local user profiles ===
# Project: BillWatch
import os
import json
from pathlib import Path

USER_DATA_DIR = Path(__file__).parent / "user_profiles"
USER_DATA_DIR.mkdir(exist_ok=True)

def get_user_profile(username: str = "default") -> dict:
    profile_path = USER_DATA_DIR / f"{username}.json"
    if profile_path.exists():
        return json.loads(profile_path.read_text())
    return {"username": username, "bills": [], "monthly_summary": {}}

def save_user_profile(username: str, profile: dict) -> None:
    profile["username"] = username
    profile_path = USER_DATA_DIR / f"{username}.json"
    profile_path.write_text(json.dumps(profile, indent=2))
