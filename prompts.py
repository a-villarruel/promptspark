"""Prompt templates and building logic for PromptSpark."""

def build_prompt(category: str, idea: str) -> str:
    return f"""
You are a creative innovation engine.

Category: {category}
Base Idea: {idea}

Generate:

1. Product Name
2. Tagline
3. Description (3-4 sentences)
4. 3 Key Features
5. Target Audience
6. A Unique Creative Twist

Be creative but realistic.
Avoid generic ideas.
Make it innovative and structured clearly.
"""