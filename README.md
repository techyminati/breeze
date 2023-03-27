# Breeze AI #
---------------------------------------------------------------------------------------
* This is a Python code that performs sentiment analysis on text data using a simple approach of counting the number of positive and negative words in the text.

The code defines two functions:

```
preprocess_text - a function that preprocesses the text data by converting it to lowercase, removing punctuation and special characters, and replacing multiple whitespaces with a single space. It takes a string input and returns a preprocessed string.
get_sentiment - a function that analyzes the sentiment of the given text by counting the number of positive and negative words and returning the overall sentiment (positive, negative, or neutral). It takes three inputs:
getinp: a string representing the text data to analyze
positive_words: a list of strings representing positive words to count in the text
negative_words: a list of strings representing negative words to count in the text
```
* It returns a string representing the sentiment of the text as either "positive", "negative", or "neutral".

-----------------------------------------------------------------------------------------

### Approach/Algorithms

* This code uses a simple approach of counting the number of positive and negative words in the text and comparing their counts to determine the overall sentiment. This is often referred to as a lexicon-based approach, 
  which relies on pre-defined lists of positive and negative words (in this case, positive_words and negative_words lists)
  to determine the sentiment of the text.

* While this approach is not as sophisticated as some of the more advanced AI algorithms used in sentiment analysis,
  such as machine learning models and neural networks, it can be useful for simple sentiment analysis tasks
   and can provide quick insights into the overall sentiment of a text.



-------------------------------------------------------------------------------------------

### Contributions and LICENSING

* Contributions via pull requests are welcome!
* This project is licensed under GPL v3.





