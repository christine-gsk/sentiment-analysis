from textblob import TextBlob

text = "The high cost of the drug is a Barrier, but the improved standard of care in the absence of corticosteroid overprescription is an Enabler."
blob = TextBlob(text)

# Analyze sentiment
sentiments = {
    "Barrier": 0,
    "Enabler": 0,
    "Driver": 0
}

for sentence in blob.sentences:
    polarity = sentence.sentiment.polarity
    if polarity > 0:
        sentiments["Driver"] += 1
    elif polarity < 0:
        sentiments["Barrier"] += 1
    else:
        sentiments["Enabler"] += 1

print("BED Sentiment Analysis Results:")
for sentiment, count in sentiments.items():
    print(f"{sentiment}: {count} sentences")
