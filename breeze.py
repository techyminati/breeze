#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# (c) Aryan Sinha, Ashutosh Mishra, Aviral Jain

import re
from typing import List

def preprocess_text(text: str) -> str:
    """
    Preprocess the text by converting it to lowercase, removing punctuation and special characters, and 
    replacing multiple whitespaces with a single space.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def get_sentiment(text: str, positive_words: List[str], negative_words: List[str]) -> str:
    """
    Analyze the sentiment of the given text by counting the number of positive and negative words and 
    returning the overall sentiment (positive, negative, or neutral).
    """
    text = preprocess_text(text)
    words = text.split()
    
    positive_count = 0
    negative_count = 0
    
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1
    
    if positive_count > negative_count:
        return 'positive'
    elif positive_count < negative_count:
        return 'negative'
    else:
        return 'neutral'


positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'awesome', 
                  'outstanding', 'superb', 'delightful', 'brilliant', 'terrific', 'splendid', 'perfect']
negative_words = ['bad', 'poor', 'terrible', 'awful', 'horrible', 'disappointing', 'mediocre',
                  'disastrous', 'dreadful', 'appalling', 'atrocious', 'inferior', 'unsatisfactory', 'subpar']


text1 = "I had a bad experience with the product."
text2 = "The product is great and I'm really satisfied with it."
text3 = "This product is just okay, not bad but not great either."

sentiment1 = get_sentiment(text1, positive_words, negative_words)
sentiment2 = get_sentiment(text2, positive_words, negative_words)
sentiment3 = get_sentiment(text3, positive_words, negative_words)

print(f"Text1: {text1}\nSentiment: {sentiment1}\n")
print(f"Text2: {text2}\nSentiment: {sentiment2}\n")
print(f"Text3: {text3}\nSentiment: {sentiment3}\n")
