"""AI-powered LeetCode Coach for interview prep.
This script provides a curriculum-based coaching system inspired by NeetCode.io.
It guides the user through problems, tracks progress, and simulates interviews.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
import json
import time
import os

# Simple problem representation
@dataclass
class Problem:
    title: str
    topic: str
    difficulty: str
    prompt: str
    solution: str
    hints: List[str]
    time_complexity: str
    space_complexity: str


# Main coach class
@dataclass
class LeetCodeCoach:
    curriculum: Dict[str, List[Problem]] = field(default_factory=dict)
    progress_file: str = "progress.json"
    progress: Dict[str, Dict[str, bool]] = field(default_factory=dict)

    def __post_init__(self):
        self._load_default_curriculum()
        self._load_progress()

    def _load_default_curriculum(self):
        # Minimal curriculum example
        self.curriculum = {
            "arrays": [
                Problem(
                    title="Two Sum",
                    topic="arrays",
                    difficulty="easy",
                    prompt="Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
                    solution="Use a hash map to store each value's index as you iterate.",
                    hints=[
                        "Can you do it in one pass?",
                        "Think about using extra space to remember numbers you've seen."
                    ],
                    time_complexity="O(n)",
                    space_complexity="O(n)"
                ),
                Problem(
                    title="Contains Duplicate",
                    topic="arrays",
                    difficulty="easy",
                    prompt="Given an integer array nums, return true if any value appears at least twice in the array.",
                    solution="Use a set to track values as you iterate.",
                    hints=["What data structure lets you check for membership quickly?"],
                    time_complexity="O(n)",
                    space_complexity="O(n)"
                )
            ],
            "linked-lists": [
                Problem(
                    title="Merge Two Sorted Lists",
                    topic="linked-lists",
                    difficulty="easy",
                    prompt="Merge two sorted linked lists and return it as a new list.",
                    solution="Iterate through both lists and build a new sorted list.",
                    hints=["Use a dummy head to simplify edge cases."],
                    time_complexity="O(n+m)",
                    space_complexity="O(1)"
                )
            ]
        }

    def _load_progress(self):
        if os.path.exists(self.progress_file):
            with open(self.progress_file, "r") as f:
                self.progress = json.load(f)
        else:
            self.progress = {}

    def _save_progress(self):
        with open(self.progress_file, "w") as f:
            json.dump(self.progress, f, indent=2)

    def assess_skill(self):
        print("--- Skill Assessment ---")
        level = input("Rate your algorithm skill (beginner/intermediate/advanced): ")
        self.progress.setdefault("skill_level", level)
        self._save_progress()
        print(f"Skill level recorded as {level}.")

    def list_topics(self):
        print("Available topics:")
        for t in self.curriculum.keys():
            print(f" - {t}")

    def next_problem(self, topic: Optional[str] = None) -> Optional[Problem]:
        if not topic:
            topic = next(iter(self.curriculum.keys()))
        problems = self.curriculum.get(topic, [])
        for p in problems:
            if not self.progress.get(p.title):
                return p
        return None

    def start_problem(self, topic: Optional[str] = None):
        problem = self.next_problem(topic)
        if not problem:
            print("No more problems in this topic!")
            return
        print(f"\n--- {problem.title} ({problem.difficulty}) ---")
        print(problem.prompt)
        for idx, hint in enumerate(problem.hints, 1):
            show = input(f"Need hint {idx}? (y/n): ")
            if show.lower().startswith('y'):
                print(f"Hint {idx}: {hint}")
            else:
                break
        input("Attempt the problem now. Press Enter when done to see the solution.")
        print("Solution:")
        print(problem.solution)
        print(f"Time Complexity: {problem.time_complexity}")
        print(f"Space Complexity: {problem.space_complexity}")
        self.progress[problem.title] = True
        self._save_progress()

    def simulate_interview(self):
        print("\n--- Mock Interview ---")
        problem = self.next_problem()
        if not problem:
            print("You have solved all problems!")
            return
        print(f"Problem: {problem.title}")
        print(problem.prompt)
        start = time.time()
        input("You have 20 minutes. Press Enter when you have an answer...")
        duration = int(time.time() - start)
        print(f"You took {duration} seconds.")
        print("Let's review your approach.")
        code = input("Paste your code here (or describe):\n")
        self.review_code(code, problem)
        self.progress[problem.title] = True
        self._save_progress()

    def review_code(self, code: str, problem: Problem):
        print("Reviewing your code for edge cases and clarity...")
        length = len(code.splitlines())
        if length < 3:
            print("Your solution seems short; ensure you've handled all cases.")
        if "for" in code and "while" in code:
            print("Nested loops detected; consider time complexity.")
        print(f"Expected Time Complexity: {problem.time_complexity}")
        print(f"Expected Space Complexity: {problem.space_complexity}")

    def show_progress(self):
        solved = [p for p, done in self.progress.items() if done is True]
        print(f"Problems solved: {len(solved)}")
        for title in solved:
            print(f" - {title}")


def main():
    coach = LeetCodeCoach()
    while True:
        print("\nCommands: assess, topics, practice, interview, progress, quit")
        cmd = input("Choose command: ").strip()
        if cmd == "assess":
            coach.assess_skill()
        elif cmd == "topics":
            coach.list_topics()
        elif cmd == "practice":
            topic = input("Enter topic (or leave blank): ") or None
            coach.start_problem(topic)
        elif cmd == "interview":
            coach.simulate_interview()
        elif cmd == "progress":
            coach.show_progress()
        elif cmd == "quit":
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
