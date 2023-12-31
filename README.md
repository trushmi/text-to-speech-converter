# Text to Speech Converter

This is a fully responsive web application built with Flask that converts text into speech in just one click. It uses the gTTS (Google Text-to-Speech API) library for generating the speech and langdetect for auto-detecting the language of the input text.
<img width="1723" alt="Screenshot 2023-11-07 at 9 54 58 AM" src="https://github.com/trushmi/text-to-speech-converter/assets/88466266/21f1a006-ac73-4f99-8c84-1c9b8905c23b">

### Usage

To use the application, follow these steps:

- Enter the text you want to convert to speech in the text area.
- The application will automatically detect the language of the input text.
- Click the "Convert and listen" button.
- Wait for the audio to load.
- Click the play button to listen to the audio.

### Installation

Before running the application, ensure you have Python installed on your system. This application was developed with Python 3.

1. ### Start by cloning the repository to your local machine:
   ```
   git clone https://github.com/trushmi/text-to-speech-converter.git
   ```
2. ### Navigate to your project directory:

   ```
   cd your-project-directory-name
   ```

3. ### Setup the virtual environment:

   - Create a virtual environment to manage your project's dependencies separately:

   ```
   virtualenv env
   ```

4. ### Activate virtual environment

   ```
   source env/bin/activate
   ```

5. ### Install all requirements

   Install the project requirements:

   ```
   pip3 install -r requirements.txt
   ```

6. ### Run the Application
   Now, start the server:
   ```
   python3 app.py
   ```
7. ### Access the App
   Open your web browser and navigate to the following address to access the app:
   ```
   http://localhost:5000/
   ```

### Contributing

If you would like to contribute to the project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive commit messages.
- Push your changes to your fork.
- Submit a pull request to the main repository.

```

```
