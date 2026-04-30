from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_playlist(user_input, context):
    prompt = f"""
You are a professional music curator.

Examples:
Input: sad mood
Output: calm piano, emotional acoustic songs

Input: workout
Output: high-energy EDM and hip-hop

Now:
Input: {user_input}
Context: {context}

Return a playlist with explanations.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def critique_playlist(playlist):
    prompt = f"""
Evaluate this playlist. Is it good? Does it match the mood?

Playlist:
{playlist}

Respond: Good or Needs Improvement + explanation.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def refine_playlist(playlist, critique):
    if "Good" in critique:
        return playlist

    prompt = f"""
Improve this playlist based on critique.

Playlist:
{playlist}
Critique:
{critique}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def run_agent(user_input, context):
    print("\n--- PLAN ---")
    print(f"Analyzing mood: {user_input}")

    draft = generate_playlist(user_input, context)

    print("\n--- DRAFT ---")
    print(draft)

    critique = critique_playlist(draft)

    print("\n--- CRITIQUE ---")
    print(critique)

    final = refine_playlist(draft, critique)

    print("\n--- FINAL ---")
    print(final)

    return final