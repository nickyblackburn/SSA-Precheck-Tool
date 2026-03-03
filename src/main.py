
from mental_classifier import MentalClassifier
from utils import logging
with open("/home/nicky/Documents/ssa-precheck-tool/data/keywords.json", "r") as f:
    text = f.read()

classifier = MentalClassifier()
results = classifier.classify(text)

for category, matches in results.items():
    logging.Warning(f"\n--- {category.upper()} ---")
    for match in matches:
        logging.PipeLine_Data(f"Sentence: {match['sentence']}")
        logging.PipeLine_Data(f"Matched: {match['matched_keyword']}")