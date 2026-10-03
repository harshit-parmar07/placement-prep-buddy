import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMMA_MODEL = "gemma-4-26b-a4b-it"


def generate_practice_set(client, topic, difficulty, weak_area):
    """Calls the Gemini API to generate a practice set using Gemma."""
    system_instruction = (
        "You are a concise interview-preparation coach. Create a short practice set for one learner. "
        "Use these exact markdown section headings: '### Practice Questions', '### Hints', "
        "'### Answers / Explanations', and '### Follow-up Question'. "
        "Return exactly: 1. Three questions. 2. One hint for each question. 3. A short answer or "
        "explanation for each. 4. One follow-up question. Do not invent personal facts. "
        "Keep the language beginner-friendly."
    )

    wa = weak_area if weak_area else "No specific weak area provided."

    prompt = (
        f"Topic: {topic}\n"
        f"Difficulty: {difficulty}\n"
        f"Weak area: {wa}\n\n"
        f"Make the questions appropriate for the {difficulty} level. "
        "Use short, actionable hints. "
        "Give technically correct but beginner-friendly explanations — avoid long, vague answers. "
        "The entire set should be completable in about 15 minutes. "
        "Where appropriate for this topic, include one practical coding, SQL, or conceptual question."
    )

    try:
        response = client.models.generate_content(
            model=GEMMA_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction
            ),
        )
        return response.text
    except Exception as e:
        print(f"API Error during generation: {e}")
        st.error("Failed to generate the practice set. Check the terminal for details.")
        return None


def main():
    st.set_page_config(page_title="Placement Prep Buddy")

    # Sidebar
    with st.sidebar:
        st.header("About this tool")
        st.write(
            "Built for a friend preparing for software-engineering interviews. "
            "Choose one topic, practise for 15 minutes, and focus on the concepts "
            "that need attention."
        )
        st.markdown(
            "- Three focused questions\n"
            "- Hints when you need them\n"
            "- Short explanations\n"
            "- One follow-up challenge"
        )

    st.title("Placement Prep Buddy")
    st.write("Get a focused practice set for your next interview.")
    st.write("Designed for a friend who wanted short, focused practice instead of a long question bank.")

    # API key check
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        st.error("Add GEMINI_API_KEY to your .env file and restart the app.")
        st.stop()

    client = genai.Client(api_key=api_key)

    topic = st.text_input("Interview topic", value="Arrays")
    difficulty = st.selectbox("Difficulty", options=["Beginner", "Intermediate", "Advanced"])
    weak_area = st.text_input("Weak area (optional)")

    if st.button("Generate practice set"):
        # Input validation — topic must not be blank
        cleaned_topic = topic.strip()
        if not cleaned_topic:
            st.warning("Please enter an interview topic first.")
            st.stop()

        cleaned_weak_area = weak_area.strip()

        with st.spinner("Gemma is creating your personalized practice set..."):
            result = generate_practice_set(client, cleaned_topic, difficulty, cleaned_weak_area)

        if result:
            st.success("Practice set ready — good luck!")
            st.divider()
            st.subheader("Your 15-minute practice set")
            st.markdown(result)

            with st.expander("How to use this practice set"):
                st.write(
                    "Try each question before opening the explanation. "
                    "Use the hints only when you are stuck, then attempt the "
                    "follow-up question without looking back."
                )

    # Footer captions
    st.caption(
        "Generated with Gemma through the Gemini API. "
        "Do not enter private, sensitive, or confidential information."
    )
    st.caption(
        "This prototype uses an API for fast access; Gemma's open-weight availability "
        "makes local or self-hosted inference a possible future version."
    )


if __name__ == "__main__":
    main()
