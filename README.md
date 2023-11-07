# Text to Speech Converter

This is a web application built with Flask that converts text into speech. It uses the `gTTS` (Google Text-to-Speech) library for generating the speech and `langdetect` for auto-detecting the language of the input text.

### Usage

To use the application, follow these steps:

- Enter the text you want to convert to speech in the text area.
- The application will automatically detect the language of the input text.
- Click the "Convert and listen" button.
- Wait for the audio to load.
- Click the play button to listen to the audio.

### Installation

Before running the application, ensure you have Python installed on your system. This application was developed with Python 3.

1. Start by cloning the repository to your local machine:
   ```
   Clone this repository or download the source code.
   cd your-project-directory-name
   ```
2. Setup the virtual environment:
   Create a virtual environment to manage your project's dependencies separately:

```
virtualenv env
```

3. Activate virtual environment

```
source env/bin/activate   # On Windows use `env\Scripts\activate`
```

4. Install all requirements
   Install the project requirements:

```
pip3 install -r requirements.txt
```

### Contributing

If you would like to contribute to the project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive commit messages.
- Push your changes to your fork.
- Submit a pull request to the main repository.
