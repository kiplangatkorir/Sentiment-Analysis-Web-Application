# Sentiment Analysis Web Application

This project is a simple web application that performs sentiment analysis on user-provided text. It uses Flask for the backend, TextBlob for sentiment analysis, and a basic HTML/JavaScript frontend.

## Features

- Web interface for text input
- Real-time sentiment analysis
- Classification of text as positive, neutral, or negative

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.7 or later
- You have a basic understanding of Python, Flask, and web development

## Installing Sentiment Analysis Web Application

To install the Sentiment Analysis Web Application, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/sentiment-analysis-app.git
   cd sentiment-analysis-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Using Sentiment Analysis Web Application

To use the Sentiment Analysis Web Application, follow these steps:

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Enter text in the provided text area and click "Analyze" to see the sentiment analysis result

## Deploying to Render

Render is a cloud platform that offers free hosting for web services. Here's how to deploy your application to Render:

1. Sign up for a free account at [render.com](https://render.com)

2. From your dashboard, click on "New +" and select "Web Service"

3. Connect your GitHub repository or manually specify your repository URL

4. Configure your web service:
   - Name: Choose a name for your service
   - Environment: Select "Python 3"
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

5. Click "Create Web Service"

Render will automatically deploy your application. Once the deployment is complete, you'll receive a URL where your app is hosted.

### Additional Configuration

1. Create a `render.yaml` file in your project root:

```yaml
services:
  - type: web
    name: sentiment-analysis-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.0
```

## Contributing to Sentiment Analysis Web Application

To contribute to the Sentiment Analysis Web Application, follow these steps:

1. Fork this repository
2. Create a branch: `git checkout -b <branch_name>`
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact

If you want to contact me, you can reach me at `<korirkiplangat22@gmail.com>`.

## License

This project uses the following license: [MIT License](<link_to_license>).