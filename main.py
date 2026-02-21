"""PromptSpark - Main CLI entry point."""

from api import generate_idea
from prompts import build_prompt


def main():
    print("=" * 50)
    print("🚀 Welcome to PromptSpark")
    print("=" * 50)

    categories = ["Startup", "Game", "Story", "App", "Marketing"]

    print("\nChoose a category:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")

    try:
        choice = int(input("\nEnter number: "))
        category = categories[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    idea = input("\nEnter your base idea: ")

    print("\n✨ Generating creative concept...\n")

    prompt = build_prompt(category, idea)
    result = generate_idea(prompt)

    print("=" * 50)
    print("💡 Generated Concept")
    print("=" * 50)
    print(result)


if __name__ == "__main__":
    main()