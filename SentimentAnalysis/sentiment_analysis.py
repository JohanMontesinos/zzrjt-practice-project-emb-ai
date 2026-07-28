"""
Analysis of the sentiment of a given text using a sentiment analysis API.
Uses IBM Watson's NLP service to predict the sentiment of the text and
returns the sentiment label and score.
"""

import json

import requests


def sentiment_analyzer(text_to_analyze):
    """This function takes a text input and sends it to a sentiment analysis API.
    It returns the sentiment label and score for the provided text.
    """
    # Define the URL for the sentiment analysis API
    url = (
        "https://sn-watson-sentiment-bert.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    )
    # Create the payload with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Set the headers with the required model ID for the API
    header = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header, timeout=6.0)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        label = formatted_response["documentSentiment"]["label"]
        score = formatted_response["documentSentiment"]["score"]

        # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None

    # For any other unexpected status codes, set label and score to None
    else:
        label = None
        score = None

    # Return the label and score in a dictionary
    return {"label": label, "score": score}
