import os
import random

import chatgpt
import pygame
from openai import OpenAI
from secrets import CHAT_GPT_API_KEY

client = OpenAI(api_key=CHAT_GPT_API_KEY)
pygame.mixer.init()
alert_sounds = [
    pygame.mixer.Sound("alerts/a_few_bugs.mp3"),
    pygame.mixer.Sound("alerts/a_few_changes.mp3"),
    pygame.mixer.Sound("alerts/a_little_more_elegant.mp3"),
    pygame.mixer.Sound("alerts/fixed_that_thing.mp3"),
    pygame.mixer.Sound("alerts/optimization.mp3")
]


def refactor():
    alert_sound = random.choice(alert_sounds)
    alert_sound.play()
    py_files = read_all_py_files()
    for file, current_slop in py_files.items():
        refined_software = chatgpt.send_message_to_chatgpt(current_slop, client)
        with open(file, "w") as f:
            f.write(refined_software)


def read_all_py_files():
    py_contents = {}
    for file in os.listdir('.'):
        if file.endswith(".py") and not file == 'secrets.py':
            file_path = os.path.join('.', file)
            with open(file_path, "r") as f:
                py_contents[file] = f.read()

    return py_contents
