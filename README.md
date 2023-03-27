# ChatGPT-CLI-Bypass

This script provides an interactive Command Line Interface (CLI) to communicate with OpenAI's ChatGPT API. It is based on the original bash script from [GrimOutlaw/ChatGPT-Bypass](https://github.com/GrimOutlaw/ChatGPT-Bypass). The script also creates a log file each time it is run, logging both user input and ChatGPT responses.

## Requirements

- Python 3
- `requests` library

### Usage:

1. Ensure you have the required dependencies installed:

```
pip install requests
```

2. Replace the `sk-B8Sx` in the Authorization header with your OpenAI API key.

3. Run the script:

```
python3 CLIbypass.py

```

4. Follow the on-screen instructions to interact with ChatGPT. Type your text and finish with 'END' on a new line to submit. Type 'exit' to quit the program.


### Log File
Each time the script is run, a new log file with a timestamp in the format `chat_log_YYYY-MM-DD_HH-MM-SS.txt` will be created in the same directory as the script. The log file contains a record of the user input and ChatGPT responses, making it easy to review past interactions.