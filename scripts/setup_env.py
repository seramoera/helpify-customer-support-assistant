import nltk
import subprocess

print("Downloading NLTK resources...")
nltk.download("punkt")
nltk.download("stopwords")

print("Downloading spaCy model...")
subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])

print("Environment setup complete.")