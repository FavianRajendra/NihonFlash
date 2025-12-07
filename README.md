🇯🇵 JpLearn - Japanese Mastery App

Master Hiragana, Katakana, Kanji, and Grammar from N5 to N2.

JpLearn is a cross-platform mobile application built entirely in Python using the Flet framework. It is designed to be a lightweight, distraction-free study companion for Japanese language learners preparing for the JLPT (Japanese-Language Proficiency Test).

✨ Features

🔤 Complete Kana Charts: Master all 46 basic Hiragana and Katakana characters.

📚 Extensive Kanji Database: Over 600+ Kanji flashcards covering JLPT levels N5, N4, N3, and N2.

📖 Grammar Library: Detailed grammar points for N5-N2, including:

Formation Rules: Exactly how to connect verbs/adjectives.

Usage Notes: When and how to use specific particles.

Example Sentences: Real-world context with translations.

🧠 Smart Flashcards:

Front: Kanji/Word + Furigana (reading aid).

Back: Meaning, Romaji, and detailed explanations.

3D Flip Animation: Smooth, native-feeling interactions.

🔀 Shuffle Mode: Randomize your deck to test your true memory retention.

📱 Cross-Platform: One codebase runs natively on Android, iOS, and Desktop.

🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites

Python 3.9+ installed on your system.

(Optional) VS Code or PyCharm for editing.

Installation

Clone the repository:

git clone [https://github.com/YOUR_USERNAME/JpLearn.git](https://github.com/YOUR_USERNAME/JpLearn.git)
cd JpLearn


Create a virtual environment (Recommended):

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate


Install dependencies:

pip install flet


Run the app locally:

flet run main.py


📱 Building for Android (APK)

You can turn this Python code into a native Android app (.apk) completely for free.

1. Setup Tools

You need the Flutter SDK and Android Studio installed.

Run flet doctor in your terminal to verify your setup.

2. Build Command

Run the following command in your terminal:

flet build apk --project-name "JpLearn" --description "Japanese Flashcards N5-N2"


First run: This may take 10-15 minutes to download necessary SDKs.

Output: The APK file will be located in: build/apk/app-release.apk.

3. Install

Transfer the app-release.apk file to your Android phone via USB, Google Drive, or WhatsApp and install it!

🛠️ Tech Stack

Language: Python 3.11+

Framework: Flet (Powered by Flutter)

Icons: Material Icons

📂 Project Structure

JpLearn/
├── main.py              # The core application logic and UI
├── flashcard_data.py    # Database for Hiragana, Katakana, and Kanji
├── grammar_data.py      # Database for Grammar rules and examples
├── assets/              # Icons and images
├── README.md            # Project documentation
└── .gitignore           # Files to exclude from Git


🤝 Contributing

Contributions are welcome! If you want to add more Kanji or fix a grammar explanation:

Fork the Project.

Create your Feature Branch (git checkout -b feature/AddN1Kanji).

Commit your Changes (git commit -m 'Add 50 new N1 Kanji').

Push to the Branch (git push origin feature/AddN1Kanji).

Open a Pull Request.

📝 License

This project is open-source and available under the MIT License.

Made with ❤️ and Python.