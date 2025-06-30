# Emotion Detection Web Application

![Emotion Detection](https://img.shields.io/badge/AI-Emotion%20Detection-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![Watson](https://img.shields.io/badge/API-Watson%20NLP-orange)

## Project Overview

The Emotion Detection Application is a web-based tool that analyzes text input to identify and quantify emotions. Using Watson AI's natural language processing capabilities, the application detects emotions such as joy, sadness, anger, fear, and disgust in user-provided text. This solution demonstrates how AI can understand nuanced human emotions beyond simple sentiment analysis.

### Key Features

- **Text Analysis**: Analyzes any text input for emotional content
- **Multiple Emotion Detection**: Identifies five core emotions (joy, sadness, anger, fear, disgust)
- **Dominant Emotion Recognition**: Highlights the strongest emotion present in the text
- **Web Interface**: User-friendly interface for easy interaction
- **RESTful API**: Backend API for integration with other applications

## Technical Architecture

The application follows a layered architecture with each component building upon previous ones:

1. **Core Detection Layer** (`EmotionDetection/1_core_detector.py`)
   - Handles communication with the Watson NLP service
   - Processes raw API responses into structured emotion data

2. **Web Service Layer** (`2_web_server.py`)
   - Flask-based web server implementation
   - Exposes REST API endpoints
   - Manages template rendering

3. **Frontend Layer** (`templates/3_main.html`, `static/3_emotion_interface.js`)
   - User interface for text input and result display
   - Client-side request handling

4. **Testing Layer** (`4_test_suite.py`)
   - Comprehensive test suite for validation

### Dependency Flow

```
External Dependencies (Flask, requests) → Core Detection Module → Web Server → Frontend
```

## Installation Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection for Watson API access

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/emotion-detection-application.git
   cd emotion-detection-application
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask requests
   ```

## Usage Guide

### Running the Application

1. **Start the web server**
   ```bash
   python 2_web_server.py
   ```

2. **Access the application**
   - Open your web browser and navigate to: `http://localhost:5000`
   - The web interface will load automatically

### Using the Web Interface

1. Enter text in the provided input field
2. Click the "Analyze" button
3. View the results showing:
   - Individual emotion scores
   - The dominant emotion detected

## API Documentation

The application provides a RESTful API endpoint for emotion detection:

### Endpoint: `/emotionDetector`

- **Method**: GET
- **Parameters**:
  - `textToAnalyze` (string, required): Text to analyze for emotions
- **Response**: 
  - Text description of detected emotions with scores
  - Dominant emotion identification
- **Example Request**:
  ```
  GET /emotionDetector?textToAnalyze=I%20am%20very%20happy%20today
  ```
- **Example Response**:
  ```
  For the given statement, the system response is 'anger': 0.031, 'disgust': 0.022, 'fear': 0.033, 'joy': 0.589 and 'sadness': 0.067. The dominant emotion is joy.
  ```

## Testing Instructions

Run the test suite to verify the application's functionality:

```bash
python 4_test_suite.py
```

The test suite validates:
- Emotion detection for various emotional statements
- Correct identification of dominant emotions
- Error handling for invalid inputs

## Directory Structure

```
emotion-detection-application/
├── EmotionDetection/
│   ├── __init__.py                # Module initialization
│   └── 1_core_detector.py         # Core emotion detection functionality
├── static/
│   └── 3_emotion_interface.js     # Client-side JavaScript
├── templates/
│   └── 3_main.html                # HTML template for web interface
├── 2_web_server.py                # Flask web server
├── 4_test_suite.py                # Unit tests
└── README.md                      # Documentation
```

## Dependencies

- **Flask**: Web framework for hosting the application
- **Requests**: HTTP library for API communication
- **Watson NLP Service**: IBM's natural language processing service for emotion detection

## Development Setup

For developers who want to extend or modify the application:

1. **Fork the repository**

2. **Set up your development environment**
   - Follow the installation instructions above
   - Install additional development tools:
     ```bash
     pip install pylint pytest
     ```

3. **Code structure understanding**
   - `1_core_detector.py`: Contains the core API interaction functions
   - `2_web_server.py`: Defines routes and Flask application setup
   - Frontend files: Handle user interaction and display

4. **Making changes**
   - Modify the core detection logic in `1_core_detector.py`
   - Add new routes in `2_web_server.py`
   - Adjust frontend appearance in `3_main.html` and behavior in `3_emotion_interface.js`

5. **Testing changes**
   - Add new test cases to `4_test_suite.py`
   - Run tests to verify your changes

6. **Code quality**
   - Run linting: `pylint EmotionDetection 2_web_server.py 4_test_suite.py`

## Troubleshooting

- **API Connection Issues**: Verify your internet connection and Watson service availability
- **Application Not Starting**: Check for Python errors in the console
- **Empty Results**: Ensure the text input is not empty and contains emotional content

## License

This project is licensed under the MIT License - see the LICENSE file for details.
