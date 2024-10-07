# Text to Speech Converter

## In this ReadMe:
- [About this project](#about-this-project)
- [How to use the app](#how-to-use-the-app)
- [How to contribute ](#how-to-contribute)
- [Resourses](#resourses)

### About this project 

Text to Speech Converter is a fully responsive web application built with Flask that converts text into speech in just one click. It uses the gTTS (Google Text-to-Speech API) library for generating the speech and langdetect for auto-detecting the language of the input text.

<img width="1723" alt="Text to Speech Converter main page" src="https://github.com/trushmi/text-to-speech-converter/assets/88466266/21f1a006-ac73-4f99-8c84-1c9b8905c23b">

### How to use the app

To use the application, follow these steps:

- Enter the text you want to convert to speech in the text area.
- The application will automatically detect the language of the input text.
- Click the "Convert and listen" button.
- Wait for the audio to load.
- Click the play button to listen to the audio.

### How to run the app

Before running the application, ensure you have Python installed on your system. This application was developed with Python 3.

1. #### Start by cloning the repository to your local machine:

   ```
   git clone https://github.com/trushmi/text-to-speech-converter.git
   ```
   
2. #### Navigate to your project directory:

   ```
   cd your-project-directory-name
   ```

3. #### Setup the virtual environment:

   Create a virtual environment to manage your project's dependencies separately:

   ```
   virtualenv env
   ```

4. #### Activate virtual environment

   ```
   source env/bin/activate
   ```

5. #### Install all requirements 
   ```
   pip3 install -r requirements.txt
   ```
6. #### Run the app

   Now, start the server:

   ```
   python3 app.py
   ```
7. #### Access the app
   Open your web browser and navigate to the following address to access the app:
   ```
   http://localhost:5000/
   ```

### How to contribute 

If you would like to contribute to the project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive commit messages.
- Push your changes to your fork.
- Submit a pull request to the main repository.

### Resourses 

See my other project, [Text Summarizer](https://github.com/trushmi/ai-text-summarizer), a web application designed to provide quick and efficient summaries of large texts. 

