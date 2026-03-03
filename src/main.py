
from mental_classifier import MentalClassifier
from utils import logging
with open("sample_report.txt", "r") as f:
    text = f.read()

classifier = MentalClassifier()
results = classifier.classify(text)

for category, matches in results.items():
    logging.Warning(f"\n--- {category.upper()} ---")
    for match in matches:
        logging.PipeLine_Data(f"Sentence: {match['sentence']}")
        logging.PipeLine_Data(f"Matched: {match['matched_keyword']}")