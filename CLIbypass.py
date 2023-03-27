#!/usr/bin/env python3

'''
Purpose: Interactive ChatGPT bypass based on the original bash script from https://github.com/GrimOutlaw/ChatGPT-Bypass
Author: Bryan (hxhBroFessor)


'''

import requests
import json
import logging
import datetime
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)

# Configure logging
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"chat_log_{timestamp}.txt"
logging.basicConfig(filename=log_filename, level=logging.INFO, format="%(asctime)s - %(message)s")

# Function to get a completion response from the OpenAI API
def get_completion(prompt):
    # Set the API endpoint, headers, and data
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer <Put API Key here>",
    }
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 4000,
        "temperature": 1.0,
    }

    # Make a POST request to the API and store the response
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    
    # Check the response status code and return the generated text or an error message
    if response.status_code == 200:
        result = response.json()
        text = result["choices"][0]["text"]
        return text
    else:
        print("Error:", response.status_code, response.text)
        return None


# Main function to interact with the ChatGPT via CLI
def main():
    # Print instructions for the user
    print("ChatGPT Interactive CLI\n")
    print("Type 'exit' to quit the program.\n")
    print("Enter your text and finish with 'END' on a new line to submit.\n")

    # Continuously read user input and send it to the API
    while True:
        input_lines = []
        print("You: ")

        # Read multiple lines of input until the user types 'END'
        while True:
            line = input()
            if line.lower() == "end":
                break
            input_lines.append(line)

        input_text = "\n".join(input_lines)

        # Exit the loop if the user types 'exit'
        if input_text.lower() == "exit":
            break

        # Log the user's question
        logging.info("You: %s", input_text)

        # Get the API response and print it
        output_text = get_completion(input_text)

        if output_text is not None:
            print(f"ChatGPT: {output_text}")

            # Log the API response
            logging.info("ChatGPT: %s", output_text.strip())

if __name__ == "__main__":
    main()