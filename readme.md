# LeetCode Coach

This repository contains a simple AI-powered coach designed to help you prepare for technical coding interviews using a curriculum inspired by **NeetCode.io**.

## Features

- Assess your current algorithmic skill level
- Identify weaknesses through targeted practice questions
- Curate a personalized problem list that increases in difficulty
- Simulate mock interviews with timed challenges and behavioral tips
- Provide step-by-step hints before revealing solutions
- Explain the time and space complexity for each problem
- Track progress over time in `progress.json`
- Review user-submitted code for clarity and efficiency

## Usage

Run the coach from the command line using Python 3:

```bash
python3 leetcode_coach.py
```

Available commands:

- `assess` – record your skill level
- `topics` – list available topics
- `practice` – work through the next problem in a topic
- `interview` – start a timed mock interview
- `progress` – view solved problems
- `quit` – exit the program

Progress is saved automatically in `progress.json`.
