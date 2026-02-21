"""PromptSpark - Main CLI entry point."""

from api import generate_idea
from prompts import build_prompt

def main():
    categories = {
        "1": "App",
        "2": "Game",
        "3": "Startup",
        "4": "AI Tool",
        "5": "Physical Product"
    }

    print("\n" + "=" * 50)
    print("🚀 PromptSpark – AI Idea Generator")
    print("=" * 50 + "\n")

    print("Choose a category:")
    for key, value in categories.items():
        print(f"{key}. {value}")

    choice = input("\nEnter category number: ").strip()

    if choice not in categories:
        print("\n❌ Invalid choice. Please restart and try again.\n")
        return

    category = categories[choice]
    idea = input("Enter a base idea or theme: ").strip()

    if not idea:
        print("\n❌ Idea cannot be empty. Please restart.\n")
        return

    print("\n⏳ Generating your AI-powered idea...\n")

    prompt = build_prompt(category, idea)
    result = generate_idea(prompt)

    print("\n" + "=" * 50)
    print("💡 GENERATED IDEA")
    print("=" * 50 + "\n")
    print(result)

    print("\n" + "=" * 50)
    print("✨ Powered by AI – PromptSpark")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()