## This program prompts the user to enter their medical data. It then prepares it in a format ready for their data to be used to fill out a form.
import openai
import re

# Your OpenAI API key
openai.api_key = 'insert-api-key-here'

def initialPrompt(numQuestions):
    questioningOver = False
    # Start the conversation with a series of questions
    prompt = "You will create a text file of medical records. Output an text array of " + numQuestions + " new questions written in the format ['question 1', 'question 2', 'question 3', ... , 'questions" + numQuestions + "], do not respond anything else other than these questions stored in square brackets and each separated by a comma, the questions themselves must not contain commas - the commas should only come in between questions. The first question should be what is your name."
    full_prompt = [ {"role": "system", "content": prompt} ]
    # Send the initial prompt to the API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=full_prompt
    )
    # Store the answers
    generatedQuestions = response.choices[0].message.content

    # Remove the brackets at the beginning and the end
    stripped_string = generatedQuestions.strip("[]")

    # Use regex to split the string by comma, accounting for potential spaces
    questions = re.split(r'\s*,\s*', stripped_string)
    return questions

def processData(questions):
    answers = []

    for question in questions:
        print(question)
        response = input()
        answers.append(response)
    return answers

if __name__ == "__main__":
    ## response is the first set of questions
    print("How many questions do you want to answer?")
    numQuestions = input()
    questions = initialPrompt(numQuestions)

    ## answers is answers the user provides
    answers = processData(questions)

    with open('openai-env/Code/MedicalData.txt', 'w') as file:
        for question, answer in zip(questions, answers):
            file.write(f"{question}: {answer}\n")
    
    