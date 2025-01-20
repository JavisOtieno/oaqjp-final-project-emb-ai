"""
This module serves to detect emotion.
 It uses the EmotionDetection package 
to analyze the emotions in a given text with results.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector
app = Flask(__name__)
@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Detects the emotion from the given text 
    then returns the result as a response.

    Args:
        None.

    Returns:
        A JSON response containing the emotion 
        analysis or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if isinstance(result, dict):
        anger = result.get('anger', 0)
        disgust = result.get('disgust', 0)
        fear = result.get('fear', 0)
        joy = result.get('joy', 0)
        sadness = result.get('sadness', 0)
        dominant_emotion = result.get('dominant_emotion', 'unknown')
    else:
        raise ValueError("Unexpected result format")
            # Check if dominant emotion is None (error handling)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    # Format the output as required
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return response_text
# except Exception as e:
#     return jsonify({"error": str(e)}), 500
    # Catching more specific exceptions



@app.route("/")
def index():
    """
    Renders the index page of the application.
    Returns:
        The rendered HTML page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5005)
