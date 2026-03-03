# file for classifiyng mental  conditions

import json
import re
from utils import logging


class MentalClassifier:


    def __init__(self,keywordfile = "keywords.json"):

        logging.Debug("Loading keyword json file....")
        with open(keywordfile, 'r') as f:
            self.keywords = json.load(f)

    
    def _split_sentences(self,text):
        sentences = re.split(r'[.!?]\s',text)
        return [s.strip()for s in sentences if s.strip()]

    # classifier 
    def classify(self, text):
        results = {category: [] for category in self.keywords}

        sentences = self._split_sentences(text)

        for sentence in sentences:
            lower_sentence = sentence.lower()

            for category, keywords in self.keywords.items():
                for keyword in keywords:
                    if keyword.lower() in lower_sentence:
                        results[category].append({
                            "sentence": sentence,
                            "matched_keyword": keyword
                        })

        return results



