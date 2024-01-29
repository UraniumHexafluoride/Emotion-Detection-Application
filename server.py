"""
This module defines a Flask web application for emotion detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app = Flask("Emotion Detection")

def run_emotion_detection():
    """Run the Flask application."""
    app.run(host="0.0.0.0", port=5000)

def get_response_text(text_to_analyze):
    """Get the response text for emotion detection."""
    response = emotion_detector(text_to_analyze)
    formatted_response = emotion_predictor(response)

    if formatted_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is 'anger': {formatted_response['anger']} "
        f"'disgust': {formatted_response['disgust']}, 'fear': {formatted_response['fear']}, "
        f"'joy': {formatted_response['joy']}, 'sadness': {formatted_response['sadness']}. "
        f"The dominant emotion is {formatted_response['dominant_emotion']}."
    )

@app.route('/emotionDetector')
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    text_to_detect = request.args.get('textToAnalyze', '')
    return get_response_text(text_to_detect)

@app.route('/')
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    run_emotion_detection()