''' Unit tests for the sentiment analysis function'''

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class test_sentiment_analysis(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Test case 1: Positive sentiment
        text1 = "I love this product! It's amazing."
        result1 = sentiment_analyzer(text1)
        self.assertEqual(result1["label"], 'SENT_POSITIVE')
        #self.assertGreater(result1["score"], 0)

        # Test case 2: Negative sentiment
        text2 = "This is the worst experience I've ever had."
        result2 = sentiment_analyzer(text2)
        self.assertEqual(result2["label"], 'SENT_NEGATIVE')
        #self.assertLess(result2["score"], 0)

        # Test case 3: Neutral sentiment
        text3 = "The weather is okay today."
        result3 = sentiment_analyzer(text3)
        self.assertEqual(result3["label"], "SENT_NEUTRAL")
        #self.assertEqual(result3["score"], 0)

unittest.main()
