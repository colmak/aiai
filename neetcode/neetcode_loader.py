import json
from typing import List, Dict, Optional

import requests
from bs4 import BeautifulSoup

NEETCODE_API_URL = "https://neetcode.io/roadmap"  # Fallback HTML or API endpoint
NEETCODE_GITHUB_JSON = "https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json"


def _parse_json(data: List[dict]) -> List[Dict[str, str]]:
    problems = []
    for item in data:
        title = item.get("problem")
        topic = item.get("pattern") or ""
        difficulty = item.get("difficulty") or ""
        link = item.get("link", "").lstrip("/")
        url = f"https://neetcode.io/problems/{link}"
        problems.append(
            {
                "title": title,
                "topic": topic,
                "difficulty": difficulty,
                "url": url,
            }
        )
    return problems


def fetch_neetcode_curriculum() -> Optional[List[Dict[str, str]]]:
    """Fetch NeetCode problems via the site or fall back to GitHub."""
    try:
        resp = requests.get(NEETCODE_API_URL, timeout=10)
        resp.raise_for_status()
        if "application/json" in resp.headers.get("Content-Type", ""):
            data = resp.json()
            return _parse_json(data)
        else:
            soup = BeautifulSoup(resp.text, "html.parser")
            scripts = soup.find_all("script", id="__NEXT_DATA__")
            if scripts:
                json_data = json.loads(scripts[0].string)
                data = json_data.get("props", {}).get("pageProps", {}).get("data")
                if data:
                    return _parse_json(data)
    except Exception:
        pass
    try:
        resp = requests.get(NEETCODE_GITHUB_JSON, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return _parse_json(data)
    except Exception:
        return None
