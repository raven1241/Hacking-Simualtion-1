import time
import random
import sys
from colorama import Fore, Style  # For text color (install with `pip install colorama`)

# Function to simulate typing with random delays
def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(0.01, 0.1))
    print()

# Function to simulate loading with random delays
def loading():
    for _ in range(20):
        print(".", end='', flush=True)
        time.sleep(random.uniform(0.1, 0.5))
    print()

# Function to display a counting progress
def count_up(total_count):
    for i in range(total_count + 1):
        sys.stdout.write(f'\rCounting: {i}/{total_count}')
        sys.stdout.flush()
        time.sleep(0.0001)  # Adjust the sleep time for speed

# Function to ask for user input with customization
def get_user_input(prompt, valid_responses):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_responses:
            return user_input
        else:
            print("ERROR: Please enter a valid response.")

# Simulate the hacking sequence
print("Initializing hacking sequence...")
time.sleep(2)

# Ask for user customization
target_server = input("Enter the target server: ")
target_id = input("Enter the target server's ID (3-digit number): ")

# User Interaction: Ask whether to initialize the hack
initiate_hack = get_user_input("Initialize the hack? [y/n]: ", ['y', 'n'])

if initiate_hack == "y":
    print(f"Connecting to target server {target_server}...")
    loading()
    time.sleep(1)

    # Randomized Responses
    access_responses = [
        "Access granted. Downloading files...",
        "Access authorized. Initiating download...",
        "Security bypassed. Commencing data transfer...",
    ]
    print(random.choice(access_responses))
    loading()
    time.sleep(1)

    print("Cracking encryption codes...")
    loading()
    time.sleep(1)

    # Visuals: Colorize the text
    print(Fore.GREEN + "Encryption codes cracked." + Style.RESET_ALL)
    loading()
    time.sleep(1)

    # Visuals: Customize the progress bar color
    print(Fore.YELLOW + "Downloading sensitive data..." + Style.RESET_ALL)
    count_up(15450)
    print("\nSensitive data downloaded.")

    # Randomized Responses
    completion_responses = [
        "Hacking complete. Exiting...",
        "Mission accomplished. Terminating operation...",
        "Data successfully retrieved. Wrapping up...",
    ]
    print(random.choice(completion_responses))
else:
    print("Hack Terminated")

# Simulate some additional activity
time.sleep(2)
print("\nTarget system compromised.")
print("Deleting logs...")
for i in range(10):
    loading()
    time.sleep(0.5)
print("\nCovering tracks...")
for i in range(10):
    loading()
    time.sleep(0.5)
print("\n" + "Operation complete.")
