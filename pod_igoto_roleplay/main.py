import os
import sys
from engine import RoleplayEngine

def main():
    print("Initializing 'Pod igoto' Roleplay Engine...")

    # Path to the book
    # Assuming run from root or within the module, let's make it robust
    base_dir = os.path.dirname(os.path.abspath(__file__))
    book_path = os.path.join(base_dir, "books", "pod_igoto.pdf")

    engine = RoleplayEngine(book_path)
    engine.load_text()

    print("\n--- Welcome to 1876, Byala Cherkva ---")
    print("You are now part of the story. Speak, patriot.")
    print("(Type 'exit' or 'quit' to leave)")

    while True:
        try:
            user_input = input("\n> ")
            if user_input.lower() in ["exit", "quit"]:
                print("Farewell. Long live Bulgaria!")
                break

            if not user_input.strip():
                continue

            is_valid, offending_word = engine.analyze_input(user_input)
            response = engine.generate_response(user_input, is_valid, offending_word)

            print(f"\n{response}")

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
