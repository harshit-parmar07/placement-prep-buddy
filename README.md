# Placement Prep Buddy

## What it is

Placement Prep Buddy is a lightweight Streamlit application that generates a focused, 15-minute interview practice set tailored to a specific topic. It leverages the power of Gemma, accessed through the Gemini API, to create high-quality, relevant practice questions on the fly.

## Who it is for

This tool was originally built for a friend who was preparing for software-engineering interviews and feeling overwhelmed by massive, unfocused question banks. It is designed for learners who want to target specific concepts and practice efficiently.

## The problem

When preparing for technical interviews, it's easy to get lost in an endless sea of general questions. A short, topic-specific practice session helps candidates drill down into the exact areas they need to improve, reinforcing learning through immediate, focused application without the distraction of unrelated topics.

## Features

- Interview topic input
- Difficulty selection
- Optional weak-area input
- Three focused questions
- Hints
- Short explanations
- One follow-up challenge
- Loading and error states

## How it works

1. The learner enters a topic, difficulty, and optional weak area.
2. The Python app sends a structured prompt to Gemma.
3. Gemma returns the practice set.
4. Streamlit displays the result.

## Why Gemma and open innovation matter

Gemma is central to this project because it is responsible for generating the personalized practice content that makes the tool effective. As an open-weight model, Gemma offers a flexible foundation for the future of this application. While this current prototype accesses Gemma through an API for speed and rapid development, the underlying open nature of the model means the interface could later be connected to a locally served or self-hosted Gemma model. A local version could significantly improve user privacy by keeping all study data on-device and reduce dependence on a hosted service. Note that the current API-based version requires an active internet connection to function.

## Tech stack

- Python
- Streamlit
- Google GenAI SDK
- Gemma through the Gemini API
- python-dotenv

## Setup

Follow these commands to get the app running locally:

```bash
# 1. Create a virtual environment
python3 -m venv venv

# 2. Activate the virtual environment
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Copy .env.example to .env
cp .env.example .env

# 5. Add your GEMINI_API_KEY to the .env file

# 6. Run the application
streamlit run app.py
```

## Security

The `.env` file is explicitly ignored by Git (via `.gitignore`) to ensure your secrets are not uploaded to version control. Your API keys must never be committed to a public repository.

## Limitations

- Internet is required for the API version to function.
- Generated content is produced by AI and should be reviewed; accuracy is not guaranteed.
- There is no progress tracking, login, or database to store your history.

## Future improvements

- Local Gemma inference
- Progress tracking
- Retrieval from personal study notes
- Answer evaluation
- Voice input
