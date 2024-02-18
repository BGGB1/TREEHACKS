import openai
import re

# Your OpenAI API key
openai.api_key = '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'

def initialPrompt():
    questioningOver = False
    # Start the conversation with a series of questions
    prompt = "You will create a text file of medical records. Start with Step 1. Step 1: Output an text array of 5 new questions written in the format ['question 1', 'question 2', 'question 3', 'question 4 ', 'question 5'], do not respond anything else other than these questions stored in square brackets and each separated by a comma. Move to Step 2, wait for the prompt before saying anything else. Step 2: You will recieve an input prompt with the data stored in the format ['stop condition', 'answer 1', 'answer 2', 'answer 3', 'answer 4', 'answer 5'], do not ask for the answers.  If the field in 'stop condition' == 'stop' then move to Step 3. If the field in 'stop condition' == 'continue' then move to Step 1: Step 3: Output the records stored as a text file where each line has the matching question and answer separated by a colon."
    # Send the initial prompt to the API
    response = openai.Completion.create(
        engine="text-davinci-003",  # or "text-davinci-004" depending on your access
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    # Store the answers
    generatedQuestions = response.choices[0].text.strip()

    # Remove the brackets at the beginning and the end
    stripped_string = answers.strip("[]")

    # Use regex to split the string by comma, accounting for potential spaces
    questions = re.split(r'\s*,\s*', stripped_string)
    return questions

def processData(questions)
    print("Type 'stop' to stop answering questions")
    
    answers = ["resume"]

    for (question in questions):
        print(question)
        response = input()
        if response == "stop":
            answers[0] == "stop"
            questioningOver = True
            break
        else:
            answers.append(response)
    return answers

def sendData(answers):
    formatted_answers = f"[{', '.join(answers)}]"
    follow_up_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=formatted_answers,
        temperature=0.7,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
    response = follow_up_response.choices[0].text.strip()
    # Store the answers
    generatedQuestions = response.choices[0].text.strip()

    # Remove the brackets at the beginning and the end
    stripped_string = answers.strip("[]")

    # Use regex to split the string by comma, accounting for potential spaces
    questions = re.split(r'\s*,\s*', stripped_string)
    return questions

if __name__ == "__main__":
    ## response is the first set of questions
    questions = initialPrompt()
    allQuestions = questions

    ## answers is answers the user provides
    answers = processData(questions)
    allAnswers = answers[0:]
    
    while answers[0] != "stop":
        questions = sendData(answers)
        allQuestions.append(questions)

        answers = processData(questions)
        allAnswers.append(answers[0:])

    with open('MedicalData.txt', 'w') as file:
    for question, answer in zip(allQuestions, allAnswers):
        file.write(f"{question}: {answer}\n")
    
    
    
    
