from typing import List, Dict

from .neetcode_loader import fetch_neetcode_curriculum


class LeetCodeCoach:
    """Simple coach that stores the NeetCode curriculum."""

    def __init__(self) -> None:
        self.curriculum: List[Dict[str, str]] = []
        self._load_default_curriculum()

    def _load_default_curriculum(self) -> None:
        problems = fetch_neetcode_curriculum()
        if not problems:
            problems = [
                {
                    "title": "Two Sum",
                    "topic": "Arrays",
                    "difficulty": "Easy",
                    "url": "https://leetcode.com/problems/two-sum/",
                },
                {
                    "title": "Valid Parentheses",
                    "topic": "Stack",
                    "difficulty": "Easy",
                    "url": "https://leetcode.com/problems/valid-parentheses/",
                },
            ]
        self.curriculum = problems

    def get_curriculum(self) -> List[Dict[str, str]]:
        return self.curriculum
