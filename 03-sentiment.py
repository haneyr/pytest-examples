from textblob import TextBlob
import pytest

def extract_sentiment(text: str):
    '''Extract sentiment using textblob. 
    Polarity is within range [-1, 1]'''
    text = TextBlob(text)
    return text.sentiment.polarity

testdata = [('I think today will be a great day',True),
     ('I do not think this will turn out well', False)]

@pytest.mark.parametrize('sample, expected_output', testdata)

def test_extract_sentiment(sample, expected_output):
    sentiment = extract_sentiment(sample)
    assert (sentiment > 0) == expected_output
