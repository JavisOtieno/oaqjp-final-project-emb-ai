import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze:  # Check for blank input
        # Return a dictionary with None for all emotion values if input is blank
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    # Send a POST request to the Watson EmotionPredict function
    response = requests.post(url, json=payload, headers=headers)
    # Raise an exception if the request failed
    response.raise_for_status()
    if response.status_code == 400:
    # Return a dictionary with None values for unsuccessful status code
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    # Return the 'text' attribute of the response JSON
    result = response.json()
        # Extract the emotion predictions (we assume there is only one prediction in the response)
    emotions = result['emotionPredictions'][0]['emotion']
    # Extract the individual emotions and their scores
    emotion_scores = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0)
    }
    # Find the dominant emotion by selecting the one with the highest score
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    dominant_score = emotion_scores[dominant_emotion]
    # Return the result in the required format
    return {
        'dominant_emotion': dominant_emotion,
        'dominant_score': dominant_score,
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0)
    }

if __name__ == "__main__":
    # Example text to analyze
    text_to_analyze = "I'm so excited about the upcoming project! It's going to be amazing."
    
    try:
        # Run the emotion detector
        result = emotion_detector(text_to_analyze)
        
        # Print the results
        print("Emotion Detection Result:")
        print(result)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")