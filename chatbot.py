import datetime
import json
import random
from selenium import webdriver
import time
from main import pyttsx3

def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate',150)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"error: {str(e)}")


def simple_chat():
    print("Simple chat program")
    print("Type 'exit' to exit the loop")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye! Exiting the chat.")
            break

        response = generate_response(user_input)
        print("Bot:", response)


def calc():
    num1 = float(input("enter the first number:"))
    num2 = float(input("Enter the second  number:"))
    sum_result = num1 + num2
    diff_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2

    print(f"Sum: {sum_result}")
    print(f"Difference: {diff_result}")
    print(f"Product: {product_result}")
    print(f"Quotient: {quotient_result}")


def play_number_game():
    print("welcome to number gussing game :")
    print("im thinking number between 1 to 9")

    secret_number = random.randint(1, 9)  # randint function of random module
    attempts = 0  # initializes the variable

    while True:
        guess = int(input("Guess the number (1-9): "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")


def get_current_datetime():
    current_datetime = datetime.datetime.now()
    return f"The current date and time is: {current_datetime}"


def load_local_responses(file_path):
    try:
        with open(file_path, 'r') as file:
            responses = json.load(file)
        return responses
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Eror loading local responses: {str(e)}")
        return {}


def save_local_responses(responses, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(responses, file, indent=4)
        print(f"local responses saved to {file_path}")
    except Exception as e:
        print(f"error saving local responses :{str(e)}")


def learn_from_user_input(user_input, responses, file_path):
    if user_input.lower() in responses:
        current_responses = responses[user_input.lower()]
        print(f"Current responses for '{user_input}': {current_responses}")
        update_option = input("Do you want to update the list of responses? (yes/no): ").lower()
        if update_option == 'yes': new_responses = input(
            "Enter the updated list of responses (comma-separated): ").split(',')
        responses[user_input.lower()] = [response.strip() for response in new_responses]
        save_local_responses(responses, file_path)
        return f"List of responses for '(user_input)' updated successfully."
    updated_response = input("Enter the updated response for this input: ")
    responses[user_input.lower()] = [updated_response]
    save_local_responses(responses, file_path)
    return f"List of responses for '{user_input}' updated successfully."


def edit_existing_response(responses, file_path):
    user_input_to_edit = input("enter the excisting input to edit:")
    if user_input_to_edit.lower() in responses:
        updated_response = input("enter the updated response for this input:")
        responses[user_input_to_edit.lower()] = updated_response
        save_local_responses(responses, file_path)
        return f"rsponse for '{user_input_to_edit}'edited sucessfully"
    else:
        return f"no existing rsponse found for'{user_input_to_edit}'."


def delete_existing_response(responses, file_path):
    user_input_to_delete = input("enter the existing input to delete:")
    if user_input_to_delete.lower() in responses:
        del responses[user_input_to_delete.lower()]
        save_local_responses(responses, file_path)
        return f"responses for '{user_input_to_delete}'deleted sucessfuly"
    else:
        return f"no existing responses found for '{user_input_to_delete}'."


def add_new_response(responses, file_path):
    new_Input = input("Enter a new input: ")
    new_response = input("Enter the response for this input: ")
    responses[new_Input.lower()] = new_response
    save_local_responses(responses, file_path)
    return f"new response added for '{new_Input}' successfully."


def manage_responses(responses, file_path):
    while True:
        print("\nManage Responses Menu:")
        print("1. Update an existing response")
        print("2. Edit an existing response")
        print("3. Delete an existing response")
        print("4. Add a new response")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            user_input_to_update = input("Enter the existing input to update: ")
            if user_input_to_update.lower() in responses:
                print(learn_from_user_input(user_input_to_update, responses, file_path))
            else:
                print(f"No existing response found for '{user_input_to_update}'.")
        elif choice == '2':
            print(edit_existing_response(responses, file_path))
        elif choice == '3':
            print(delete_existing_response(responses, file_path))
        elif choice == '4':
            print(add_new_response(responses, file_path))
        elif choice == '5':
            print("Exiting the Manage Responses Menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


def generate_response(user_input, responses, file_path):
    if user_input.lower() in responses:
        response_list = responses[user_input.lower()]
        return random.choice(response_list)

    else:
        response = learn_from_user_input(user_input, responses, file_path)
    speak(response)


def generate_response(user_input):
    if any(keyword in user_input.lower() for keyword in ['hello', 'hi']):
        speak('Hi there! How can I help you?')
    elif 'playgame' in user_input.lower():
        play_number_game()
    elif 'how are you' in user_input.lower():
        speak( 'I\'m just a computer program.')
    elif 'how is the weather today' in user_input.lower():
        speak( 'Today\'s weather is sunny.')
    elif 'tell me a joke' in user_input.lower():
        speak( 'How do you prevent a Summer cold? Catch it in the Winter!')
    elif 'your favorite color' in user_input.lower():
        speak( 'I don\'t have a favorite color, but I like the concept of rainbow colors.')
    elif 'who created you' in user_input.lower():
        speak( 'I was created by talented developers at OpenAI.')
    elif 'your age' in user_input.lower():
        speak( 'I don\'t have an age. I\'m always up-to-date!')
    elif 'where are you from' in user_input.lower():
        speak( 'I exist in the digital realm, so you could say I\'m from the world of computer programming.')
    elif 'thank you' in user_input.lower():
        speak( 'You\'re welcome! If you have more questions, feel free to ask.')
    elif 'good morning' in user_input.lower():
        speak( 'Good morning! How can I assist you today?')
    elif 'good night' in user_input.lower():
        speak( 'Good night! If you have more to chat about, I\'ll be here.')
    elif 'introduce family' in user_input.lower():
        speak('lokesh,nagarthnamma,yashwanth,jashwanth.')
    elif 'introduce yourself' in user_input.lower():
        speak('jashwanth from bangalore qualification BE graduate')
    elif 'bye' in user_input.lower():
        speak( 'Goodbye.')
    elif 'date and time' in user_input.lower():
        print('Bot:', get_current_datetime())
    elif 'calculator' in user_input.lower():
        calc()


if __name__ == '__main__':
    user_input = input("Enter the text you want the program to speak: ")
    speak(user_input)
    simple_chat()