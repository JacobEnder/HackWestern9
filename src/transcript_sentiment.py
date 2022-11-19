
# Return an average sentiment score given a list of sentiments for each phrase
#   cohere_classification is a list of Classification objects
def sentiment_from_phrases(cohere_classifications):
    total_score = 0
    net_conf = 0
    for classification in cohere_classifications:
        prediction = classification.prediction
        confidence = classification.confidence
        score = 0
        if prediction == 'negative':
            score = -10
        elif prediction == 'positive':
            score = 1
        score *= confidence
        net_conf += confidence
        total_score += score
    return total_score / net_conf