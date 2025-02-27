import os
import json
from datetime import datetime
from typing import Dict, List, Any

def ensure_directories():
    """Ensure necessary directories exist."""
    directories = [
        "data",
        "data/research_papers",
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def save_to_json(data: Any, filename: str) -> bool:
    """Save data to a JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving to JSON: {str(e)}")
        return False

def load_from_json(filename: str) -> Any:
    """Load data from a JSON file."""
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    except Exception as e:
        print(f"Error loading from JSON: {str(e)}")
        return None

def sanitize_filename(name: str) -> str:
    """Convert a string to a safe filename."""
    return "".join(c for c in name if c.isalnum() or c in "._- ").replace(" ", "_")

def format_timestamp(timestamp_str: str) -> str:
    """Format a timestamp string to a more readable format."""
    try:
        dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return timestamp_str