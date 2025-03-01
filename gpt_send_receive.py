from openai import OpenAI
from pathlib import Path

def send_to_gpt():
    prompt = input("Enter your prompt here: ")
    str_file = input("Enter filepath here: ")

    file = Path(str_file)

    # add cool chatgpt stuff here

def receive_from_gpt(output):
    print("Receiving from chatgpt...")

    print(output)