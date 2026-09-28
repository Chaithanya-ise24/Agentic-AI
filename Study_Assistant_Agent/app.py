from google import genai
from google.genai import types

# Initialize client with your API key
# Replace the hardcoded string with an empty client call:
client = genai.Client()


# --- 1. ZERO-SHOT PROMPTING ---
print("=== 1. ZERO-SHOT PROMPTING ===")
res1 = client.models.generate_content(
    model=MODEL,
    contents="Explain what a Binary Search Tree is in 2 sentences.",
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful study assistant."
    )
)
print(res1.text)


# --- 2. FEW-SHOT PROMPTING ---
print("\n=== 2. FEW-SHOT PROMPTING ===")
few_shot_prompt = """
Q: What is Big O notation?
A: A mathematical notation used to describe the execution time or space complexity of an algorithm.

Q: What is a Stack?
A: A linear data structure that follows the Last-In-First-Out (LIFO) principle.

Q: What is a Binary Search Tree?
A:"""

res2 = client.models.generate_content(
    model=MODEL,
    contents=few_shot_prompt,
    config=types.GenerateContentConfig(
        system_instruction="You are an academic tutor providing short definitions based on patterns."
    )
)
print(res2.text)


# --- 3. ROLE PROMPTING ---
print("\n=== 3. ROLE PROMPTING ===")
res3 = client.models.generate_content(
    model=MODEL,
    contents="Explain Binary Search Trees.",
    config=types.GenerateContentConfig(
        system_instruction="You are a friendly computer science professor. Keep explanations super clear and simple."
    )
)
print(res3.text)


# --- 4. INTELLIGENT FAQ ASSISTANT ---
print("\n=== 4. INTELLIGENT FAQ ASSISTANT ===")
faq_context = """
Campus FAQ:
- Exam starts: Dec 1, 2026
- Attendance needed: 85%
- Library timing: 8 AM to 8 PM
"""

student_question = "What is the attendance percentage needed?"

res4 = client.models.generate_content(
    model=MODEL,
    contents=f"{faq_context}\nAnswer this query: {student_question}",
    config=types.GenerateContentConfig(
        system_instruction="Answer strictly using only the provided FAQ context."
    )
)
print(res4.text)