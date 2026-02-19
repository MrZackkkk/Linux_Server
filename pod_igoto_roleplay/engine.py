import os
import re

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

class RoleplayEngine:
    def __init__(self, book_path):
        self.book_path = book_path
        self.context_text = ""
        # Simple list of anachronisms for demonstration
        self.anachronisms = [
            "phone", "internet", "car", "computer", "television", "radio",
            "plane", "airplane", "mobile", "wifi", "ok", "okay", "cool",
            "laptop", "smartphone", "tablet", "email"
        ]

    def load_text(self):
        if not os.path.exists(self.book_path):
            print(f"Warning: Book file not found at {self.book_path}. Proceeding with limited context.")
            return False

        if not PdfReader:
             print("Warning: pypdf not installed. Cannot read PDF.")
             return False

        try:
            reader = PdfReader(self.book_path)
            text = ""
            # Limit to first 50 pages to save time/memory if the book is huge during testing
            # In production, we'd index this properly (e.g. RAG)
            for i, page in enumerate(reader.pages):
                if i > 50: break
                text += page.extract_text() + "\n"
            self.context_text = text
            print(f"Successfully loaded {len(reader.pages)} pages (processed first 50).")
            return True
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return False

    def analyze_input(self, text):
        """
        Checks if the input contains anachronisms.
        Returns (is_valid, offending_word)
        """
        text_lower = text.lower()
        words = text_lower.split()
        for word in self.anachronisms:
            if word in words: # Use split to avoid matching parts of other words
                return False, word
        return True, None

    def generate_response(self, user_input, context_valid, offending_word=None):
        if not context_valid:
            return f"I know not of this '{offending_word}' you speak of. Is it some strange Frankish invention? Here in Byala Cherkva, we concern ourselves with the freedom of Bulgaria! Speak plainly, friend."

        # Enhanced Logic: Search in context_text
        if self.context_text:
            # Find the user input words in the text
            # Simple retrieval: Find the first occurrence of a significant word
            words = [w for w in user_input.split() if len(w) > 3] # Ignore short words
            for word in words:
                # Search for the word in the text (case insensitive)
                try:
                    match = re.search(r'([^.]*?\b' + re.escape(word) + r'\b[^.]*\.)', self.context_text, re.IGNORECASE)
                    if match:
                        excerpt = match.group(1).strip().replace('\n', ' ')
                        return f"The chronicles speak of this... \"{excerpt}\" ... but what is your part in this?"
                except Exception:
                    continue # Ignore regex errors for special chars

        # Fallback Mocked Logic
        response = "The air is heavy with the scent of revolution. "
        if "turk" in user_input.lower():
            response += "Hush! The Zaptiehs might hear you. We must meet at the convent tonight."
        elif "rada" in user_input.lower():
            response += "Ah, Rada... her heart is as pure as the mountain snow."
        elif "oganov" in user_input.lower() or "boycho" in user_input.lower():
            response += "Boycho Ognyanov? A true hero. But danger follows him."
        else:
            response += f"You say '{user_input}'... but are you ready to give your life for the cause?"

        return response
